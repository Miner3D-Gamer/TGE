import os
import subprocess
import argparse
import typing
import concurrent.futures
import time
import ast

import tge


def get_typing_types() -> set:
    return set(name for name in dir(typing) if not name.startswith("_"))


def extract_typealiases(source_file: str) -> typing.List[typing.Tuple[str, str]]:
    with open(source_file, encoding="utf-8") as f:
        tree = ast.parse(f.read())

    aliases = []
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.annotation, ast.Name)
            and node.annotation.id == "TypeAlias"
        ):
            source_lines = []
            start_lineno = node.lineno - 1
            with open(source_file, encoding="utf-8") as f:
                lines = f.readlines()
                line = lines[start_lineno].strip()
                source_lines.append(line)
                # Handle multiline type aliases
                while line.count("[") > line.count("]") or line.count("(") > line.count(
                    ")"
                ):
                    start_lineno += 1
                    line = lines[start_lineno].strip()
                    source_lines.append(line)
            aliases.append((node.target.id, " ".join(source_lines)))  # type: ignore
    return aliases


def extract_used_types(aliases: typing.List[typing.Tuple[str, str]]) -> set:
    used_types = set()
    for _, alias_definition in aliases:
        # Parse the type alias definition to extract type names
        tree = ast.parse(alias_definition)
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                used_types.add(node.id)
    return used_types


def insert_typealiases(
    stub_file: str, aliases: typing.List[typing.Tuple[str, str]]
) -> None:
    if not aliases:
        return

    # Extract all used types from aliases
    used_types = extract_used_types(aliases)

    # Get valid types from `typing` module
    valid_typing_types = get_typing_types()

    # Only keep types that are valid from typing
    used_types = used_types.intersection(valid_typing_types)

    with open(stub_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Check and add necessary imports
    imports = set()
    if "TypeAlias" not in content:
        imports.add("TypeAlias")
    imports.update(used_types)

    if imports:
        import_line = "from typing import " + ", ".join(sorted(imports)) + "\n"
        if import_line not in content:
            content = import_line + content

    with open(stub_file, "w", encoding="utf-8") as f:
        f.write(content)
        f.write("\n\n# Extra\n")
        for name, definition in aliases:
            f.write(f"{definition}\n")

    # Future improvement suggestion
    # TODO: Improve handling to dynamically include other libraries if needed (e.g., from `collections` or `typing_extensions`).


def extract_and_insert_typealiases(source_file: str, stub_file: str) -> None:
    aliases = extract_typealiases(source_file)
    insert_typealiases(stub_file, aliases)


def find_python_files(directory: str) -> typing.List[str]:
    """
    Recursively find all Python files in the given directory and its subdirectories.

    Args:
        directory: Root directory to start searching from

    Returns:
        List of Python file paths relative to the current directory
    """
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                # Convert path to module format
                file_path = os.path.join(root, file)
                python_files.append(file_path)
    return python_files


def generate_stub_for_file(
    file_path: str, output_dir: str, include_private: bool = False, quiet: bool = False
) -> tuple:
    """
    Generate stub for a single Python file.

    Args:
        file_path: Path to the Python file
        output_dir: Directory where stubs should be generated
        include_private: Whether to include private members in stubs
        quiet: Whether to suppress output

    Returns:
        Tuple of (file_path, success_status, error_message)
    """
    try:
        # Construct stubgen command
        cmd = ["stubgen"]
        if include_private:
            cmd.append("--include-private")
        cmd.extend(["-o", output_dir, file_path])

        # Run stubgen
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            return (file_path, True, None)
        else:
            return (file_path, False, result.stderr)

    except Exception as e:
        return (file_path, False, str(e))


def smallen_file(path: str):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    with open(path, "w", encoding="utf-8") as f:
        f.write(
            tge.tbe.minify(
                "\n".join(tge.tbe.compress_imports_in_code(content.split("\n"))),
                remove_annotations=False,
                rename_globals=False,
                rename_locals=False,
            )
        )


def process_file(
    file_path: str, output_dir: str, include_private: bool = False, quiet: bool = False
):
    o = generate_stub_for_file(file_path, output_dir, include_private, quiet)
    stub_file_path = os.path.join(output_dir, os.path.splitext(file_path)[0] + ".pyi")
    extract_and_insert_typealiases(file_path, stub_file_path)
    smallen_file(stub_file_path)
    return o


def generate_stubs(
    files: typing.List[str],
    output_dir: str,
    include_private: bool = False,
    quiet: bool = False,
    max_workers: typing.Optional[int] = None,
) -> None:
    """
    Generate stubs for the given Python files.

    Args:
        files: List of Python file paths
        output_dir: Directory where stubs should be generated
        include_private: Whether to include private members in stubs
        quiet: Whether to suppress output
        max_workers: Number of threads to use (None for default)
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    start = time.time()

    # Use ThreadPoolExecutor for parallel processing
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Prepare futures for stub generation
        futures = [
            executor.submit(process_file, file_path, output_dir, include_private, quiet)
            for file_path in files
        ]

        # Process results
        for future in concurrent.futures.as_completed(futures):
            file_path, success, error = future.result()

            if not quiet:
                if success:
                    print(f"✓ Generated stub for: {file_path}")
                else:
                    print(f"✗ Failed to generate stub for: {file_path}")
                    print(f"Error: {error}")

    end = time.time()
    if not quiet:
        print(
            f"Generated stubs for {len(files)} files in {end - start:.2f} seconds ({len(files) / (end - start):.2f} files per second)"
        )


def main():
    parser = argparse.ArgumentParser(
        description="Recursively generate stubs for Python files"
    )
    parser.add_argument("directory", help="Root directory containing Python files")
    parser.add_argument(
        "-o",
        "--output-dir",
        default="out",
        help="Output directory for generated stubs (default: 'out')",
    )
    parser.add_argument(
        "--include-private",
        action="store_true",
        help="Include private members in generated stubs",
    )
    parser.add_argument("-q", "--quiet", action="store_true", help="Suppress output")
    parser.add_argument(
        "-t",
        "--threads",
        type=int,
        default=None,
        help="Number of threads to use for parallel stub generation (default: number of CPUs)",
    )

    args = parser.parse_args()

    # Find all Python files
    python_files = find_python_files(args.directory)

    if not python_files:
        print(f"No Python files found in {args.directory}")
        return

    if not args.quiet:
        print(f"Found {len(python_files)} Python files")

    # Generate stubs
    generate_stubs(
        python_files, args.output_dir, args.include_private, args.quiet, args.threads
    )


if __name__ == "__main__":
    main()

# Process:
# stubgen generate stubs
# Go back, look for type aliases, and add them to the stub
# Go back again and smalled file


# python generate_stubs.py -o stubs tge
