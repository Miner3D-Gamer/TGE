#type: ignore
from..shared import USER32,KERNEL32,ctypes,CF_UNICODETEXT,GHND
def get_clipboard(user32=USER32,kernel32=KERNEL32):B=kernel32;A=user32;A.OpenClipboard(0);C=A.GetClipboardData(CF_UNICODETEXT);E=B.GlobalLock(C);D=ctypes.c_wchar_p(E).value;B.GlobalUnlock(C);A.CloseClipboard();return''if D is None else D
def copy_to_clipboard(text,user32=USER32,kernel32=KERNEL32):C=kernel32;B=text;A=user32;A.OpenClipboard(0);A.EmptyClipboard();D=C.GlobalAlloc(GHND,(len(B)+1)*ctypes.sizeof(ctypes.c_wchar));E=C.GlobalLock(D);ctypes.memmove(E,B.encode('utf-16le'),(len(B)+1)*ctypes.sizeof(ctypes.c_wchar));C.GlobalUnlock(D);A.SetClipboardData(CF_UNICODETEXT,D);A.CloseClipboard()
def clear_clipboard(user32=USER32):A=user32;A.OpenClipboard(0);A.EmptyClipboard();A.CloseClipboard()
__all__=['copy_to_clipboard','get_clipboard','clear_clipboard']