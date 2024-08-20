from PIL import Image
import pyautogui
import screeninfo
import pygetwindow as gw

def screenshot_monitor(monitor_index:int=0)->Image.Image:
    monitors = screeninfo.get_monitors()

    if monitor_index >= len(monitors):
        raise ValueError("Monitor index out of range")

    monitor:screeninfo.Monitor = monitors[monitor_index]

    left = monitor.x
    top = monitor.y
    width = monitor.width
    height = monitor.height


    return pyautogui.screenshot(region=(left, top, width, height))


def screenshot_window(window_id: str) -> Image.Image:
    window_names = gw.getAllTitles()
    wanted_window = None
    for window_name in window_names:
        windows = gw.getWindowsWithTitle(window_name)
        for window in windows:
            if window._hWnd == window_id:
                wanted_window = window
                break
        else:
            continue
        break
        
    
    
    if wanted_window is None:
        raise ValueError("No window found with the specified id")
    
    

    left = wanted_window.left
    top = wanted_window.top
    width = wanted_window.width
    height = wanted_window.height
    
    return pyautogui.screenshot(region=(left, top, width, height))

def get_window_by_id(window_id:int):
    window_names = gw.getAllTitles()
    wanted_window = None
    for window_name in window_names:
        windows = gw.getWindowsWithTitle(window_name)
        for window in windows:
            if window._hWnd == window_id:
                wanted_window = window
                break
        else:
            continue
        break
    return wanted_window


