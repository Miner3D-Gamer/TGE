from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID
from AppKit import NSWorkspace, NSApplication, NSApp

def is_window_minimized_mac(window_name):
    workspace = NSWorkspace.sharedWorkspace()
    windows = workspace.activeSpace().windows()
    for window in windows:
        if window_name in window.title():
            return window.isMiniaturized()
    return False

def minimize_window_mac(window_name):
    workspace = NSWorkspace.sharedWorkspace()
    windows = workspace.activeSpace().windows()
    for window in windows:
        if window_name in window.title():
            window.performMiniaturize_(None)
            return
    raise ValueError("Window not found")

def get_window_position_mac(window_name):
    workspace = NSWorkspace.sharedWorkspace()
    windows = workspace.activeSpace().windows()
    for window in windows:
        if window_name in window.title():
            frame = window.frame()
            x, y = frame.origin.x, frame.origin.y
            return x, y
    raise ValueError("Window not found")

def maximize_window_mac(window_name):
    workspace = NSWorkspace.sharedWorkspace()
    windows = workspace.activeSpace().windows()
    for window in windows:
        if window_name in window.title():
            screen_frame = NSScreen.mainScreen().frame()
            window.setFrame_display_(screen_frame, True)
            return
    raise ValueError("Window not found")

def set_window_position_mac(window_name, x, y, width, height):
    workspace = NSWorkspace.sharedWorkspace()
    windows = workspace.activeSpace().windows()
    for window in windows:
        if window_name in window.title():
            frame = window.frame()
            frame.origin.x = x
            frame.origin.y = y
            frame.size.width = width
            frame.size.height = height
            window.setFrame_display_(frame, True)
            return
    raise ValueError("Window not found")