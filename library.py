import importlib.util
from typing import List, Union, Tuple , Any, Optional, Dict
import subprocess

# Function to Test for Library Existence
def test_for_library(library_name:str) -> bool:
    """
    Tests for the accessability of a library using a custom mini 
    version of "import_lib" mostly only using the essential 
    functions needed for existence a library.
    """

    spec = importlib.util.find_spec(library_name)
    return spec is not None


def download_library(library_name: str) -> Tuple[bool, str]:
    """
    Downloads and installs a Python library using pip.

    Parameters:
        library_name (str): The name of the library to be installed.

    Returns:
        tuple: A tuple containing a boolean indicating whether the installation was successful
        and a message string providing additional information in case of an error.
    """
    command = ['python', '-m', 'pip', 'install', library_name]

    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        error_message = (
            f"Failed to install {library_name}. "
            f"Return code: {e.returncode}. "
            f"Output: {e.output}. "
            f"Error: {e.stderr}."
        )
        return False, error_message
    except Exception as e:
        return False, f"An unexpected error occurred: {str(e)}"


import os

def get_installed_python_versions()->list:
    """Get a list of installed Python executables in the system PATH."""
    paths = os.getenv('PATH').split(os.pathsep)
    python_versions = []
    for path in paths:
        try:
            for entry in os.listdir(path):
                if entry.startswith('python'):
                    full_path = os.path.join(path, entry)
                    if os.access(full_path, os.X_OK):
                        python_versions.append(full_path)
        except FileNotFoundError:
            continue
    return python_versions

def install_library_from_github(github_repo_url:str)->None:
    """Install the library from the given GitHub repository URL to all installed Python versions."""
    python_versions = get_installed_python_versions()
    for python in python_versions:
        try:
            version_info = subprocess.check_output([python, '--version'], stderr=subprocess.STDOUT).decode().strip()
            print(f"Installing for {version_info} ({python})")
            subprocess.check_call([python, '-m', 'pip', 'install', 'git+' + github_repo_url])
        except subprocess.CalledProcessError as e:
            print(f"Failed to install for {python}: {e}")