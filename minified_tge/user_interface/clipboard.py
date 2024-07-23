_A=None
from.cursor_operations import WINDOWS,USER32,KERNEL32,ctypes,CF_UNICODETEXT,GHND
if WINDOWS:
	def get_clipboard(user32=USER32,kernel32=KERNEL32):B=kernel32;A=user32;A.OpenClipboard(0);C=A.GetClipboardData(CF_UNICODETEXT);D=B.GlobalLock(C);E=ctypes.c_wchar_p(D).value;B.GlobalUnlock(C);A.CloseClipboard();return E
	def copy_to_clipboard(text,user32=USER32,kernel32=KERNEL32):C=kernel32;B=text;A=user32;A.OpenClipboard(0);A.EmptyClipboard();D=C.GlobalAlloc(GHND,(len(B)+1)*ctypes.sizeof(ctypes.c_wchar));E=C.GlobalLock(D);ctypes.memmove(E,B.encode('utf-16le'),(len(B)+1)*ctypes.sizeof(ctypes.c_wchar));C.GlobalUnlock(D);A.SetClipboardData(CF_UNICODETEXT,D);A.CloseClipboard()
	def clear_clipboard(user32=USER32):A=user32;A.OpenClipboard(0);A.EmptyClipboard();A.CloseClipboard()
else:
	import pyperclip
	def copy_to_clipboard(text,user32=_A,kernel32=_A):pyperclip.copy(text)
	def get_clipboard(user32=_A,kernel32=_A):return pyperclip.paste()
	def clear_clipboard(user32=_A):pyperclip.copy('')
from..file_operations import get_file_extension
def save_clipboard_to_file(file_path):
	try:A=open(file_path,'w',encoding='utf-8');A.write(get_clipboard());A.close();return True
	except:return False
def load_clipboard_from_file(file_path):
	try:A=open(file_path,'r',encoding='utf-8');B=A.read();A.close();copy_to_clipboard(B);return True
	except:return False
def append_to_clipboard(text):A=get_clipboard();A+=text;copy_to_clipboard(A)
def prepend_to_clipboard(text):A=get_clipboard();A=text+A;copy_to_clipboard(A)
def get_clipboard_size():return len(get_clipboard())
def get_clipboard_file_extension():return get_file_extension(get_clipboard())