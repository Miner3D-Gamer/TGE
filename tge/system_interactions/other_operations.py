from .. import SYSTEM_NAME

if SYSTEM_NAME == "windows":
    from .other import windows as other # type: ignore

elif SYSTEM_NAME == "linux":
    from .other import linux as other # type: ignore


elif SYSTEM_NAME == "darwin":
    from .other import mac as other # type: ignore
else:
    ...  # ¯\_(ツ)_/¯
