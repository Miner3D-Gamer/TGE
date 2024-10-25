# type: ignore
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID  # type: ignore
from AppKit import NSWorkspace, NSApplication, NSApp, NSWindow  # type: ignore

from typing import Optional, Tuple


def is_window_minimized(window: NSWindow):
    """Check if the window is minimized."""
    return window.isMiniaturized()


def minimize_window(window: NSWindow):
    """Minimize the specified window."""
    window.performMiniaturize_(None)


def get_window_position(window: NSWindow) -> Optional[Tuple[int, int, int, int]]:
    """Get the position and size of the window. Return None if minimized."""
    try:
        frame = window.frame()
        x, y = frame.origin.x, frame.origin.y
        return x, y, frame.size.width, frame.size.height
    except:
        return None


def maximize_window(window: NSWindow):
    """Maximize the specified window."""
    screen_frame = window.mainScreen().frame()
    window.setFrame_display_(screen_frame, True)


def set_window_position(window: NSWindow, x: int, y: int, width: int, height: int):
    """Set the position and size of the window."""
    frame = window.frame()
    frame.origin.x = x
    frame.origin.y = y
    frame.size.width = width
    frame.size.height = height
    window.setFrame_display_(frame, True)


def get_window_by_title(title: str) -> Optional[NSWindow]:
    """Find a window by its title and return its NSWindow handle."""
    windows_info = CGWindowListCopyWindowInfo(
        kCGWindowListOptionOnScreenOnly, kCGNullWindowID
    )
    for window_info in windows_info:
        window_title = window_info.get("kCGWindowName", "")
        if title in window_title:
            window_id = window_info["kCGWindowNumber"]
            window = NSApp.windowWithWindowNumber_(window_id)
            return window
    return None
