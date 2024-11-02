import subprocess, os


def create_virtual_drive(drive_letter: str, folder_path: str, size_mb: int = 100):
    """Creates a virtual drive that appears as a drive letter on macOS. The drive though is just a shortcut to the specified folder."""
    # Create an empty DMG file
    subprocess.run(
        [
            "hdiutil",
            "create",
            "-size",
            f"{size_mb}m",
            "-fs",
            "HFS+",
            "-volname",
            "VirtualDrive",
            drive_letter,
        ]
    )

    # Mount the DMG file
    subprocess.run(["hdiutil", "attach", drive_letter, "-mountpoint", folder_path])


def remove_virtual_drive(folder_path: str):
    """Removes a virtual drive that appears as a drive letter on macOS."""
    subprocess.run(["hdiutil", "detach", folder_path])


def add_to_path_to_system_path_variables(path: str):
    """
    Adds a new path to the system PATH environment variable on macOS (Darwin).

    Args:
        path (str): The path to add to the system PATH.

    Notes:
        Appends the path to the `~/.bash_profile` file and reloads it using the `source` command.
    """
    with open(os.path.expanduser("~/.bash_profile"), "a") as file:
        file.write(f'\nexport PATH="{path}:$PATH"\n')
    subprocess.run(["source", "~/.bash_profile"], shell=True, check=True)
