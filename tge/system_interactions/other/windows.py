import os, subprocess
from typing import Optional


def create_virtual_drive(
    drive_letter: str, folder_path: str, size_mb: Optional[int] = None
):
    """Creates a virtual drive that appears as a drive letter on Windows. The drive though is just a shortcut to the specified folder."""
    command = f"subst {drive_letter}: {folder_path}"
    subprocess.run(command, shell=True)


def remove_virtual_drive(drive_letter: str):
    """Removes a virtual drive that appears as a drive letter on Windows."""
    command = f"subst {drive_letter}: /d"
    subprocess.run(command, shell=True)


def add_to_path_to_system_path_variables(path: str):
    """
    Adds a new path to the system PATH environment variable on Windows.

    Args:
        path (str): The path to add to the system PATH.

    Note:
        Uses the `setx` command to update the PATH environment variable permanently.
    """
    current_path = os.getenv("PATH")
    new_path = f"{current_path};{path}"
    os.system(f'setx PATH "{new_path}"')
