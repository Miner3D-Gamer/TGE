import ctypes
from ctypes import wintypes
from . import windows_virtual_keys as keys
from typing import Optional

user32 = ctypes.WinDLL("user32")
user32.GetAsyncKeyState.restype = wintypes.SHORT

__all__ = ['is_key_pressed', 'press_key', 'hold_key', 'release_key', 'key_to_virtual_key']
def is_key_pressed(key_code: int) -> bool:
    """Checks if the inputted key is currently pressed"""
    state = user32.GetAsyncKeyState(key_code)
    return (state & 0x8000) != 0


KEYEVENTF_KEYDOWN = 0x0000
KEYEVENTF_KEYUP = 0x0002


def press_key(key_code: int) -> None:
    "Simulate pressing a key."
    user32.keybd_event(key_code, 0, KEYEVENTF_KEYDOWN, 0)
    user32.keybd_event(key_code, 0, KEYEVENTF_KEYUP, 0)


def hold_key(key_code: int) -> None:
    "Simulates holding the key corresponding to inputted key_code."
    user32.keybd_event(key_code, 0, KEYEVENTF_KEYDOWN, 0)


def release_key(key_code: int) -> None:
    "Simulates releasing the key corresponding to inputted key_code."
    user32.keybd_event(key_code, 0, KEYEVENTF_KEYUP, 0)


def key_to_virtual_key(key: str) -> Optional[int]:
    "Converts a keyboard button to their corresponding virtual key"
    if key == "\n":
        key = "enter"
    elif key == "\t":
        key = "tab"
    return keys.__dict__.get(key)
