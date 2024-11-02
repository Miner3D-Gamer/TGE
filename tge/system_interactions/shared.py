from .. import SYSTEM_NAME


if SYSTEM_NAME == "windows":
    import ctypes
    USER32: ctypes.WinDLL = ctypes.windll.user32
    KERNEL32: ctypes.WinDLL = ctypes.windll.kernel32
    CF_UNICODETEXT = 13
    GMEM_DDESHARE = 0x2000
    GMEM_MOVEABLE = 0x0002
    GHND = GMEM_DDESHARE | GMEM_MOVEABLE
    win_dll_type = ctypes.WinDLL