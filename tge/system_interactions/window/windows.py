import ctypes.wintypes
from ..shared import *
from ctypes import wintypes

class RECT(ctypes.Structure):
    _fields_ = [
        ("left", wintypes.LONG),
        ("top", wintypes.LONG),
        ("right", wintypes.LONG),
        ("bottom", wintypes.LONG)
    ]

def is_window_minimized(hwnd:int, user32 = USER32):
    return user32.IsIconic(hwnd) != 0

def minimize_window(hwnd:int, user32 = USER32):
    user32.ShowWindow(hwnd, 2)

def maximize_window(hwnd:int):
    ctypes.windll.user32.ShowWindow(hwnd, 9)

def get_window_position(hwnd:int):
    rect = RECT()
    ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
    
    # Check if the window is minimized
    if rect.left == -32000 and rect.top == -32000:
        return None
    
    return (rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top)

def set_window_position(hwnd:int, x, y, width, height):
    SWP_NOSIZE = 0x0001
    SWP_NOZORDER = 0x0004
    flags = SWP_NOZORDER | SWP_NOSIZE
    return ctypes.windll.user32.SetWindowPos(hwnd, None, x, y, width, height, flags)

def get_window_by_title(title:str):
    return ctypes.windll.user32.FindWindowW(None, title)