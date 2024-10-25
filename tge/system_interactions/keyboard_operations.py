from .. import SYSTEM_NAME
if SYSTEM_NAME == "windows":
    from .keyboard.windows import * # type: ignore
elif SYSTEM_NAME == "linux":
    from .keyboard.linux import * # type: ignore
    