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


def set_mouse_to(coords: "tuple[int, int]") -> None:
    "Move the mouse cursor to the specified coordinates (x, y)."
    MOUSE.position = coords


def get_mouse_position() -> "tuple[int, int]":
    "Retrieve the current mouse cursor position as a tuple (x, y)."
    return MOUSE.position


def left_click() -> None:
    "Perform a left mouse button click at the current mouse position."
    MOUSE.click(1)


def right_click() -> None:
    "Perform a left mouse button click at the current mouse position."
    MOUSE.click(3)


def middle_click() -> None:
    "Perform a middle mouse button click at the current mouse position."
    MOUSE.click(2)


def scroll_vertical(clicks: int, wheel_delta: int = WHEEL_DELTA) -> None:
    "Scroll the mouse wheel vertically by the specified number of `clicks`."
    MOUSE.scroll(dy=clicks)


def scroll_horizontal(clicks: int, wheel_delta: int = WHEEL_DELTA) -> None:
    "Scroll the mouse wheel horizontally by the specified number of `clicks`."
    MOUSE.scroll(dx=clicks)


def scroll(
    dx: int = None,
    dy: int = None,
    wheel_delta_x: int = WHEEL_DELTA,
    wheel_delta_y: int = WHEEL_DELTA,
) -> None:
    "Scroll the mouse wheel both horizontally and vertically by the specified amounts (`dx` and `dy`)."
    MOUSE.scroll(dy=dy, dx=dx)


def left_mouse_down() -> None:
    "Press and hold the left mouse button."
    MOUSE.press(1)


def right_mouse_down() -> None:
    "Press and hold the right mouse button."
    MOUSE.press(3)


def middle_mouse_down() -> None:
    "Press and hold the middle mouse button."
    MOUSE.press(2)


def left_mouse_up() -> None:
    "Release the left mouse button."
    MOUSE.release(1)


def right_mouse_up() -> None:
    "Release the right mouse button."
    MOUSE.release(3)


def middle_mouse_up() -> None:
    "Release the middle mouse button."
    MOUSE.release(2)


def is_left_pressed():
    return _is_button_pressed(1)


def is_right_pressed():
    return _is_button_pressed(3)


def is_middle_pressed():
    return _is_button_pressed(2)


MOUSE


def _is_button_pressed(button):
    with pynput.mouse.Events() as events:
        for event in events:
            if isinstance(event, pynput.mouse.Events.Click) and event.button == button:
                return event.pressed
        return False

