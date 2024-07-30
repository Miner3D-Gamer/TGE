from..import SYSTEM_NAME
if SYSTEM_NAME=='windows':import ctypes;USER32=ctypes.windll.user32;KERNEL32=ctypes.windll.kernel32