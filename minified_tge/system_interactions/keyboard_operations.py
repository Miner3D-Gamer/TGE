#type: ignore
from..import SYSTEM_NAME
if SYSTEM_NAME=='windows':from.keyboard.windows import is_key_pressed,press_key,hold_key,release_key,key_to_virtual_key,keys
elif SYSTEM_NAME=='linux':from.keyboard.linux import is_key_pressed,press_key,hold_key,release_key,key_to_virtual_key,keys
__all__=['is_key_pressed','press_key','hold_key','release_key','key_to_virtual_key','keys']