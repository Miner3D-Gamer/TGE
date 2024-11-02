#type: ignore
from..import SYSTEM_NAME
if SYSTEM_NAME=='windows':import ctypes;USER32=ctypes.windll.user32;KERNEL32=ctypes.windll.kernel32;CF_UNICODETEXT=13;GMEM_DDESHARE=8192;GMEM_MOVEABLE=2;GHND=GMEM_DDESHARE|GMEM_MOVEABLE;win_dll_type=ctypes.WinDLL