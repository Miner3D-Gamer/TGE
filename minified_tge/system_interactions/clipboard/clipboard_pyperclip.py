#type: ignore
import pyperclip
_A=None
def copy_to_clipboard(text,user32=_A,kernel32=_A):pyperclip.copy(text)
def get_clipboard(user32=_A,kernel32=_A):return pyperclip.paste()
def clear_clipboard(user32=_A):pyperclip.copy('')
__all__=['copy_to_clipboard','get_clipboard','clear_clipboard']