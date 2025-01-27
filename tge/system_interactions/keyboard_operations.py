from .. import SYSTEM_NAME
from typing import Protocol, Dict

class KeyboardModule(Protocol):
    def is_key_pressed(self, key: str) -> bool: 
        """Checks if the inputted key is currently pressed"""
        ...
    def press_key(self, key: str) -> None: 
        """Simulates pressing the key corresponding to inputted key"""
        ...
    def hold_key(self, key: str) -> None: 
        """Simulates holding the key corresponding to inputted key"""
        ...
    def release_key(self, key: str) -> None: 
        """Simulates releasing the key corresponding to inputted key"""
        ...
    def key_to_virtual_key(self, key: str) -> int: 
        """Converts a keyboard button to their corresponding virtual key"""
        ...
    keys: Dict[str, int]

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
