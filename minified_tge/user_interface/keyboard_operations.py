from.cursor_operations import WINDOWS
import pyautogui as pygui
from.clipboard_operations import get_clipboard
def hold_key(key):pygui.keyDown(key)
def release_key(key):pygui.keyUp(key)
def press_key(key):pygui.press(key)
def press_keys(keys):
	for A in keys:pygui.press(A)
def paste(x):pygui.typewrite(x)
def paste_clipboard():pygui.typewrite(get_clipboard())
def press_keys_from_clipboard():
	for A in get_clipboard():press_key(A)