from .. import SYSTEM_NAME
from typing import Protocol

class KeyboardModule(Protocol):
    def is_key_pressed(self, key: str) -> bool: ...
    def press_key(self, key: str) -> None: ...
    def hold_key(self, key: str) -> None: ...
    def release_key(self, key: str) -> None: ...
    def key_to_virtual_key(self, key: str) -> int: ...
    keys: dict[str, int]

# keyboard_module: KeyboardModule

if SYSTEM_NAME == "windows":
    from .keyboard import windows as keyboard_module
elif SYSTEM_NAME == "linux":
    from .keyboard import linux as keyboard_module
else:
    raise NotImplementedError

        
        
is_key_pressed = keyboard_module.is_key_pressed
press_key = keyboard_module.press_key
hold_key = keyboard_module.hold_key
release_key = keyboard_module.release_key
key_to_virtual_key = keyboard_module.key_to_virtual_key
keys = keyboard_module.keys

__all__ = ['is_key_pressed', 'press_key', 'hold_key', 'release_key', 'key_to_virtual_key', 'keys']
