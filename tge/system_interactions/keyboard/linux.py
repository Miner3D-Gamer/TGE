from Xlib import X, XK, display
from . import linux_virtual_keys as keys
from typing import Optional

d = display.Display()
root = d.screen().root
__all__ = ['is_key_pressed', 'press_key', 'hold_key', 'release_key', 'key_to_virtual_key']

def is_key_pressed(key_code: int) -> bool:
    "Checks if the inputted key is currently pressed"
    keys = root.query_pointer()._data["mask"]
    return keys & (1 << (key_code - 8)) != 0


def press_key(key_code: int)->None:
    "Simulate pressing a key."
    root.warp_pointer(0, 0)
    root.fake_input(X.KeyPress, key_code)
    d.sync()


def hold_key(key_code: int)->None:
    "Simulates holding the key corresponding to inputted key_code."
    root.warp_pointer(0, 0)
    root.fake_input(X.KeyPress, key_code)
    d.sync()


def release_key(key_code: int)->None:
    "Simulates releasing the key corresponding to inputted key_code."
    root.warp_pointer(0, 0)
    root.fake_input(X.KeyRelease, key_code)
    d.sync()


def key_to_virtual_key(key: str) -> Optional[int]:
    "Converts a keyboard button to their corresponding virtual key"
    key_symbol = XK.string_to_keysym(key)
    if key_symbol == 0:
        raise ValueError(f"Invalid key: {key}")
    k = d.keysym_to_keycode(key_symbol)
    return k if k else None
