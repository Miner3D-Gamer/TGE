import ctypes.wintypes
from ..shared import *
from ctypes import wintypes
from typing import Tuple, Optional

class RECT(ctypes.Structure):
    _fields_ = [
        ("left", wintypes.LONG),
        ("top", wintypes.LONG),
        ("right", wintypes.LONG),
        ("bottom", wintypes.LONG)
    ]

def is_window_minimized(hwnd: int, user32 = USER32) -> bool:
    """Check if the window is minimized."""
    return user32.IsIconic(hwnd) != 0

def minimize_window(hwnd: int, user32 = USER32) -> None:
    """Minimize the specified window."""
    user32.ShowWindow(hwnd, 6)  # 6 = SW_MINIMIZE

def maximize_window(hwnd: int) -> None:
    """Maximize the specified window."""
    ctypes.windll.user32.ShowWindow(hwnd, 3)  # 3 = SW_MAXIMIZE

def get_window_position(hwnd: int) -> Optional[Tuple[int, int, int, int]]:
    """Get the position and size of the window. Return None if minimized."""
    rect = RECT()
    ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
    
    if rect.left == -32000 and rect.top == -32000:
        return None
    
    return (rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top)

def set_window_position(hwnd: int, x: int, y: int, width: int, height: int) -> bool:
    """Set the position and size of the window."""
    SWP_NOSIZE = 0x0001
    SWP_NOZORDER = 0x0004
    flags = SWP_NOZORDER | SWP_NOSIZE
    return ctypes.windll.user32.SetWindowPos(hwnd, None, x, y, width, height, flags)

def get_window_by_title(title: str) -> int:
    """Find a window by its title and return its handle."""
    return ctypes.windll.user32.FindWindowW(None, title)