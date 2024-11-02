from .. import SYSTEM_NAME

if SYSTEM_NAME == "windows":
    from .windows import screenshot, get_pixel_color

__all__ = ["screenshot", "get_pixel_color"]