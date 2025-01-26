import subprocess, sys
from typing import Union, Optional, Tuple

def is_window_minimized(window_id: Optional[Union[int, str]]) -> bool:
    """Check if the window is minimized."""
    if window_id is None:
        return False

    result = subprocess.run(["wmctrl", "-lG"], stdout=subprocess.PIPE, text=True)
    lines = result.stdout.splitlines()
    for line in lines:
        if str(window_id) in line:
            parts = line.split()
            state = parts[8]
            return state == "0"  # 0 means the window is not minimized
    return False


def minimize_window(window_id: Optional[Union[int, str]]):
    """Minimize the specified window."""
    if window_id is None:
        raise ValueError("Window not found")

    subprocess.run(["wmctrl", "-i", "-r", str(window_id), "-b", "add,hidden"])


def get_window_position(window_id:Optional[int])->Optional[Tuple[int, int, int, int]]:
    """Get the position and size of the window. Return None if minimized."""
    if window_id is None:
        return None

    result = subprocess.run(["wmctrl", "-lG"], stdout=subprocess.PIPE, text=True)
    lines = result.stdout.splitlines()
    for line in lines:
        if str(window_id) in line:
            parts = line.split()
            x, y = int(parts[2]), int(parts[3])
            return x, y, int(parts[4]), int(parts[5])
    return None


def maximize_window(window_id: Optional[Union[int, str]]):
    """Maximize the specified window."""
    if window_id is None:
        raise ValueError("Window not found")

    subprocess.run(
        ["wmctrl", "-i", "-r", str(window_id), "-b", "add,maximized_vert,maximized_horz"]
    )


def set_window_position(window_id: Optional[Union[int, str]], x:int, y:int, width:int, height:int):
    """Set the position and size of the window."""
    if window_id is None:
        raise ValueError("Window not found")

    subprocess.run(
        ["wmctrl", "-i", "-r", str(window_id), "-e", f"0,{x},{y},{width},{height}"]
    )


def get_window_by_title(title: str) -> Union[str, None]:
    """Find a window by its title and return its window ID."""
    try:
        result = subprocess.run(
            ["xdotool", "search", "--name", title],
            capture_output=True,
            text=True,
            check=True,
        )
        window_id = result.stdout.strip()
        return window_id
    except subprocess.CalledProcessError:
        return None


def is_xdotool_installed():
    """Check if xdotool is installed"""
    try:
        subprocess.run(
            ["xdotool", "version"], capture_output=True, text=True, check=True
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False
    else:
        return True


def install_xdotool():
    """Installs xdotool"""
    try:
        if sys.platform.startswith("linux"):
            subprocess.run(["sudo", "apt-get", "update"], check=True)
            subprocess.run(["sudo", "apt-get", "install", "-y", "xdotool"], check=True)
            return ""
        else:
            return "Unsupported platform for automatic installation of xdotool."
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        return f"An error occurred while installing xdotool: {e}"


if not is_xdotool_installed() and (error := install_xdotool()):
    print(error)
