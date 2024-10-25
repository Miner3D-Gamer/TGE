from Xlib import X,XK,display
from.import linux_virtual_keys as keys
d=display.Display()
root=d.screen().root
def is_key_pressed(key_code):A=root.query_pointer()._data['mask'];return A&1<<key_code-8!=0
def press_key(key_code):root.warp_pointer(0,0);root.fake_input(X.KeyPress,key_code);d.sync()
def hold_key(key_code):root.warp_pointer(0,0);root.fake_input(X.KeyPress,key_code);d.sync()
def release_key(key_code):root.warp_pointer(0,0);root.fake_input(X.KeyRelease,key_code);d.sync()
def key_to_virtual_key(key):
 A=XK.string_to_keysym(key)
 if A==0:raise ValueError(f"Invalid key: {key}")
 B=d.keysym_to_keycode(A);return B if B else None