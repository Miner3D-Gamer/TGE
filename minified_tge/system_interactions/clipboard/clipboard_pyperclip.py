_A=None
import pyperclip
def copy_to_clipboard(text,user32=_A,kernel32=_A):pyperclip.copy(text)
def get_clipboard(user32=_A,kernel32=_A):return pyperclip.paste()
def clear_clipboard(user32=_A):pyperclip.copy('')