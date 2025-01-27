from .. import SYSTEM_NAME


if SYSTEM_NAME == "windows":
    import ctypes
    USER32: ctypes.WinDLL = ctypes.windll.user32
    KERNEL32: ctypes.WinDLL = ctypes.windll.kernel32
    CF_UNICODETEXT: int = 13
    GMEM_DDESHARE: int = 0x2000
    GMEM_MOVEABLE: int = 0x0002
    GHND: int = GMEM_DDESHARE | GMEM_MOVEABLE
    win_dll_type = ctypes.WinDLL