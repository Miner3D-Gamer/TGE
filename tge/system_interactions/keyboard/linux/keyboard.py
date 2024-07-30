from Xlib import X, XK, display
from . import virtual_keys as keys

# Connect to the display
d = display.Display()
root = d.screen().root

def is_key_pressed(key_code):
    keys = root.query_pointer()._data["mask"]
    return keys & (1 << (key_code - 8)) != 0

def press_key(key_code):
    """Simulate pressing a key."""
    root.warp_pointer(0, 0)
    root.fake_input(X.KeyPress, key_code)
    d.sync()

def hold_key(key_code):
    root.warp_pointer(0, 0)
    root.fake_input(X.KeyPress, key_code)
    d.sync()

def release_key(key_code):
    root.warp_pointer(0, 0)
    root.fake_input(X.KeyRelease, key_code)
    d.sync()

def key_to_virtual_key(key: str) -> int:
    key_symbol = XK.string_to_keysym(key)
    if key_symbol == 0:
        raise ValueError(f"Invalid key: {key}")
    return d.keysym_to_keycode(key_symbol)