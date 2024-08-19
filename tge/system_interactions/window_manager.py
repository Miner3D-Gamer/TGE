from .. import SYSTEM_NAME


if SYSTEM_NAME == "windows":
    from .window.windows import *
elif SYSTEM_NAME == "linux":
    from .window.linux import *
elif SYSTEM_NAME == "darwin":
    from .window.mac import *
else:
    ...
    # Nope, sorry. No idea what you're running. Can't help you.
