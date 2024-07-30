from .. import SYSTEM_NAME
if SYSTEM_NAME == "windows":
    from .keyboard.windows.keyboard import *
elif SYSTEM_NAME == "linux":
    from .keyboard.linux.keyboard import *
    