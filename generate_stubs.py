import os
import subprocess
import argparse
from typing import List, Optional
import concurrent.futures

def find_python_files(directory: str) -> List[str]:
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
            if file.endswith('.py'):
                # Convert path to module format
                file_path = os.path.join(root, file)
                python_files.append(file_path)
    return python_files

def generate_stub_for_file(
    file_path: str, 
    output_dir: str, 
    include_private: bool = False,
    quiet: bool = False
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
        cmd = ['stubgen']
        if include_private:
            cmd.append('--include-private')
        cmd.extend(['-o', output_dir, file_path])
        
        # Run stubgen
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            return (file_path, True, None)
        else:
            return (file_path, False, result.stderr)
            
    except Exception as e:
        return (file_path, False, str(e))

def generate_stubs(
    files: List[str], 
    output_dir: str, 
    include_private: bool = False,
    quiet: bool = False,
    max_workers: Optional[int] = None
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
    
    # Use ThreadPoolExecutor for parallel processing
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Prepare futures for stub generation
        futures = [
            executor.submit(
                generate_stub_for_file, 
                file_path, output_dir, include_private, quiet
            ) for file_path in files
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

def main():
    parser = argparse.ArgumentParser(description="Recursively generate stubs for Python files")
    parser.add_argument(
        'directory',
        help="Root directory containing Python files"
    )
    parser.add_argument(
        '-o', '--output-dir',
        default='out',
        help="Output directory for generated stubs (default: 'out')"
    )
    parser.add_argument(
        '--include-private',
        action='store_true',
        help="Include private members in generated stubs"
    )
    parser.add_argument(
        '-q', '--quiet',
        action='store_true',
        help="Suppress output"
    )
    parser.add_argument(
        '-t', '--threads',
        type=int,
        default=None,
        help="Number of threads to use for parallel stub generation (default: number of CPUs)"
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
        python_files,
        args.output_dir,
        args.include_private,
        args.quiet,
        args.threads
    )

if __name__ == '__main__':
    main()
#python generate_stubs.py -o stubs tge