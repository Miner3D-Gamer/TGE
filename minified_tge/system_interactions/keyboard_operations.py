#type: ignore
from typing import Protocol
from..import SYSTEM_NAME
class KeyboardModule(Protocol):
 def is_key_pressed(A,key):...
 def press_key(A,key):...
 def hold_key(A,key):...
 def release_key(A,key):...
 def key_to_virtual_key(A,key):...
 keys:0
if SYSTEM_NAME=='windows':from.keyboard import windows as keyboard_module
elif SYSTEM_NAME=='linux':from.keyboard import linux as keyboard_module
else:raise NotImplementedError
is_key_pressed=keyboard_module.is_key_pressed
press_key=keyboard_module.press_key
hold_key=keyboard_module.hold_key
release_key=keyboard_module.release_key
key_to_virtual_key=keyboard_module.key_to_virtual_key
keys=keyboard_module.keys
__all__=['is_key_pressed','press_key','hold_key','release_key','key_to_virtual_key','keys']