import os
import subprocess
import argparse
from typing import List, Optional

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

def generate_stubs(
    files: List[str], 
    output_dir: str, 
    include_private: bool = False,
    quiet: bool = False
) -> None:
    """
    Generate stubs for the given Python files.
    
    Args:
        files: List of Python file paths
        output_dir: Directory where stubs should be generated
        include_private: Whether to include private members in stubs
        quiet: Whether to suppress output
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    for file_path in files:
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
            
            if not quiet:
                if result.returncode == 0:
                    print(f"✓ Generated stub for: {file_path}")
                else:
                    print(f"✗ Failed to generate stub for: {file_path}")
                    print(f"Error: {result.stderr}")
                    
        except Exception as e:
            if not quiet:
                print(f"✗ Error processing {file_path}: {str(e)}")

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
        args.quiet
    )

if __name__ == '__main__':
    main()

#python generate_stubs.py -o stubs tge