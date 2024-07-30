
WHEEL_DELTA = 120
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
    "Move the mouse cursor to the specified coordinates (x, y)."
    MOUSE.position = x, y


def mouseGet() -> "tuple[int, int]":
    "Retrieve the current mouse cursor position as a tuple (x, y)."
    return MOUSE.position


def LeftClick() -> None:
    "Perform a left mouse button click at the current mouse position."
    MOUSE.click(1)


def RightClick() -> None:
    "Perform a left mouse button click at the current mouse position."
    MOUSE.click(3)


def MiddleClick() -> None:
    "Perform a middle mouse button click at the current mouse position."
    MOUSE.click(2)


def ScrollV(clicks: int, wheel_delta: int = WHEEL_DELTA) -> None:
    "Scroll the mouse wheel vertically by the specified number of `clicks`."
    MOUSE.scroll(dy=clicks)


def ScrollH(clicks: int, wheel_delta: int = WHEEL_DELTA) -> None:
    "Scroll the mouse wheel horizontally by the specified number of `clicks`."
    MOUSE.scroll(dx=clicks)


def Scroll(
    dx: int = None,
    dy: int = None,
    wheel_delta_x: int = WHEEL_DELTA,
    wheel_delta_y: int = WHEEL_DELTA,
) -> None:
    "Scroll the mouse wheel both horizontally and vertically by the specified amounts (`dx` and `dy`)."
    MOUSE.scroll(dy=dy, dx=dx)


def LeftMouseDown() -> None:
    "Press and hold the left mouse button."
    MOUSE.press(1)


def RightMouseDown() -> None:
    "Press and hold the right mouse button."
    MOUSE.press(3)


def MiddleMouseDown() -> None:
    "Press and hold the middle mouse button."
    MOUSE.press(2)


def LeftMouseUp() -> None:
    "Release the left mouse button."
    MOUSE.release(1)


def RightMouseUp() -> None:
    "Release the right mouse button."
    MOUSE.release(3)


def MiddleMouseUp() -> None:
    "Release the middle mouse button."
    MOUSE.release(2)
