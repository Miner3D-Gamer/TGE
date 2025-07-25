import importlib.util
from typing import Tuple, NoReturn, List, Optional
import subprocess
from collections.abc import Sequence
import os

from .tbe import get_current_pip_path

__all__ = ["install_library", "is_library_installed", "install_missing_tge_libraries"]


def is_library_installed(library_name: str) -> bool:
    """
    Tests for the accessability of a library using a custom mini
    version of "import_lib" mostly only using the essential
    functions needed for existence a library.
    """

    spec = importlib.util.find_spec(library_name)
    return spec is not None


def install_library(
    library_name: str,
    pip_path: Optional[str] = get_current_pip_path(),
    tried_commands: Optional[List[List[str]]] = None,
) -> Tuple[bool, str]:
    """
    Downloads and installs a Python library using pip.

    Parameters:
        library_name (str): The name of the library to be installed.
        pip_path (Optional[str]): The specific pip path to use for installation.
        tried_commands (Optional[List[List[str]]]): A list of commands that were tried in previous attempts.

    Returns:
        tuple: A tuple containing a boolean indicating whether the installation was successful
        and a message string providing additional information in case of an error.
    """
    # Default command list if none provided
    if tried_commands is None:
        tried_commands = (
            [[pip_path, "install", library_name]]
            if pip_path
            else [
                ["python", "-m", "pip", "install", library_name],
                ["python3", "-m", "pip", "install", library_name],
                ["pip", "install", library_name],
                ["pip3", "install", library_name],
            ]
        )

    last_error_message = None

    for command in tried_commands:
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            # On success, return True with the output
            return True, result.stdout
        except subprocess.CalledProcessError as e:
            last_error_message = (
                f"Failed to install {library_name} using command: {' '.join(command)}. "
                f"Return code: {e.returncode}. "
                f"Output: {e.output.strip()}. "
                f"Error: {e.stderr.strip()}."
            )
        except FileNotFoundError:
            # Ignore commands that can't be found
            continue
        except Exception as e:
            return False, f"An unexpected error occurred: {str(e)}"

    # Return False with the last error message if all attempts fail
    return False, f"All installation attempts failed. Last error: {last_error_message}"


# Honestly no idea what these functions do and I'm way too tired to try and figure out
def get_installed_python_versions() -> List[str]:
    """Get a list of installed Python executables in the system PATH."""
    path = os.getenv("PATH")
    if path is None:
        return []
    paths = path.split(os.pathsep)
    python_versions: List[str] = []
    for path in paths:
        try:
            for entry in os.listdir(path):
                if entry.startswith("python") and (
                    entry.endswith(".exe") or entry.endswith(".bat")
                ):
                    full_path = os.path.join(path, entry)
                    if os.access(full_path, os.X_OK):
                        try:
                            version_info = (
                                subprocess.check_output(
                                    [full_path, "--version"], stderr=subprocess.STDOUT
                                )
                                .decode()
                                .strip()
                            )
                            if "Python" in version_info:
                                python_versions.append(full_path)
                        except subprocess.SubprocessError:
                            continue
        except FileNotFoundError:
            continue
    return python_versions


def install_library_from_github(github_repo_url: str) -> None:
    """Install the library from the given GitHub repository URL to all installed Python versions."""
    python_versions = get_installed_python_versions()
    for python in python_versions:
        print(f"Python executable: {python}")
        try:
            version_info = (
                subprocess.check_output([python, "--version"], stderr=subprocess.STDOUT)
                .decode()
                .strip()
            )
            print(f"Installing for {version_info} ({python})")
            subprocess.check_call(
                [python, "-m", "pip", "install", "git+" + github_repo_url]
            )
        except subprocess.CalledProcessError as e:
            print(f"Failed to install for {python}: {e}")


def install_all_libraries(libs: "Sequence[str]") -> List[Tuple[bool, str]]:
    """
    Install a list of libraries and return a list of installation results.

    This function attempts to install each library from the provided list. It skips libraries that are already installed,
    and it collects the results of the installation attempts.

    Args:
        libs ("Sequence[str]"): An iterable containing the names of libraries to be installed.

    Returns:
        list[tuple[bool, str]]: A list of tuples where each tuple contains:
            - A boolean indicating whether the installation was successful (True) or failed (False).
            - A string message describing the result of the installation attempt.

    Examples:
        >>> install_all_libraries(["numpy", "pandas"])
        [(True, "Successfully installed numpy"), (True, "Successfully installed pandas")]
    """
    output: List[Tuple[bool, str]] = []
    for lib in libs:
        if is_library_installed(lib):
            continue
        output.append(install_library(lib))

    return output


def install_missing_tge_libraries() -> Optional[NoReturn]:
    """
    Check if all libraries listed in the 'requirements.txt' file are installed.

    This function reads the 'requirements.txt' file, which should contain a list of library names. It checks whether
    each library is installed and raises a `ModuleNotFoundError` if any library is missing.

    Raises:
        ModuleNotFoundError: If any library listed in 'requirements.txt' is not installed.
    """
    with open(os.path.dirname(__file__) + "/requirements.txt", "r") as f:
        libs = f.readlines()
    for lib in libs:
        if not is_library_installed(lib.strip()):
            install_library(lib.strip())
    return None
