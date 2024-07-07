import importlib.util
from typing import List, Union, Tuple , Any, Optional, Dict
import subprocess

# Function to Test for Library Existence
def test_for_library(library_name) -> bool:
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