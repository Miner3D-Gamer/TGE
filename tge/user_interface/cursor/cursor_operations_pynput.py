from ..cursor_operations import WHEEL_DELTA

import pynput

MOUSE = pynput.mouse.Controller()

from pyautogui import size as getScreenDimensions



# from screeninfo import get_monitors

# def getScreenDimensions() -> tuple[int, int]:
#     monitors = get_monitors()

#     monitor_width = 0
#     monitor_height = 0

#     for monitor in monitors:
#         monitor_width += monitor.width
#         monitor_height += monitor.height
#     return monitor_width, monitor_height

        


SCREEN_WIDTH, SCREEN_HEIGHT = getScreenDimensions()






def MouseTo(x: int, y: int) -> None:
    MOUSE.position = x, y

def mouseGet() -> tuple[int, int]:
    return MOUSE.position

def Click() -> None:
    MOUSE.click(1)

def RightClick() -> None:
    MOUSE.click(3)

def MiddleClick() -> None:
    MOUSE.click(2)

def ScrollV(clicks: int, wheel_delta: int = WHEEL_DELTA) -> None:
    MOUSE.scroll(dy=clicks)

def ScrollH(clicks: int, wheel_delta: int = WHEEL_DELTA) -> None:
    MOUSE.scroll(dx=clicks)

def Scroll(dx: int = None, dy: int = None, wheel_delta_x: int = WHEEL_DELTA, wheel_delta_y: int = WHEEL_DELTA) -> None:
    MOUSE.scroll(dy=dy, dx=dx)

def LeftMouseDown() -> None:
    MOUSE.press(1)

def RightMouseDown() -> None:
    MOUSE.press(3)

def MiddleMouseDown() -> None:
    MOUSE.press(2)

def LeftMouseUp() -> None:
    MOUSE.release(1)

def RightMouseUp() -> None:
    MOUSE.release(3)

def MiddleMouseUp() -> None:
    MOUSE.release(2)