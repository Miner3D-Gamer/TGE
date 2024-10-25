import subprocess, os


def create_virtual_disk(drive_letter: str, folder_path: str, size_mb:int=100):
    # Create an empty file to act as the virtual disk
    subprocess.run(
        ["dd", "if=/dev/zero", f"of={drive_letter}", "bs=1M", f"count={size_mb}"]
    )

    # Format the file as ext4 (or any other filesystem)
    subprocess.run(["mkfs.ext4", drive_letter])

    subprocess.run(["mkdir", "-p", folder_path])

    # Mount the file as a loopback device
    subprocess.run(["sudo", "mount", "-o", "loop", drive_letter, folder_path])


def remove_virtual_disk(folder_path: str):

    subprocess.run(["sudo", "umount", folder_path])


def add_to_path_to_system_path_variables(path: str):
    """
    Adds a new path to the system PATH environment variable on Linux.

    Args:
        path (str): The path to add to the system PATH.

    Notes:
        Appends the path to the `~/.bashrc` file and reloads it using the `source` command.
    """
    with open(os.path.expanduser("~/.bashrc"), "a") as file:
        file.write(f'\nexport PATH="{path}:$PATH"\n')
    subprocess.run(["source", "~/.bashrc"], shell=True, check=True)
