import ctypes
from ctypes import wintypes
from . import virtual_keys as keys

user32 = ctypes.WinDLL('user32')
user32.GetAsyncKeyState.restype = wintypes.SHORT


def is_key_pressed(key_code):
    state = user32.GetAsyncKeyState(key_code)
    return (state & 0x8000) != 0