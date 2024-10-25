from .. import SYSTEM_NAME

from.shared import *

if SYSTEM_NAME == "windows":
    from .cursor.cursor_operations_ctypes import * # type: ignore

else:
    from .cursor.cursor_operations_pynput import * # type: ignore


def click_mouse_button(button_number: int) -> None:
    "Click the mouse button specified by `button_number`."
    ClickMouseButtonList[button_number]()


def hold_mouse_button(button_number: int) -> None:
    "Hold down the mouse button specified by `button_number`."
    HoldMouseButtonList[button_number]()


def release_mouse_button(button_number: int) -> None:
    "Release the mouse button specified by `button_number`."
    ReleaseMouseButtonList[button_number]()


def click_mouse_button_at(button_number: int, x: int, y: int) -> None:
    "Click the mouse button specified by `button_number` at the coordinates (x, y)."
    ClickMouseButton_atList[button_number](x, y)







def left_click_at(x: int, y: int) -> None:
    "Move the mouse to the specified coordinates (x, y) and perform a left mouse button click."
    set_mouse_to((x, y))
    left_click()


def double_left_click() -> None:
    "Perform two consecutive left mouse button clicks at the current mouse position."
    left_click()
    left_click()


def double_left_click_at(x: int, y: int) -> None:
    "Move the mouse to the specified coordinates (x, y) and perform two consecutive left mouse button clicks."
    set_mouse_to((x, y))
    left_click()
    left_click()


def right_click_at(x: int, y: int) -> None:
    "Move the mouse to the specified coordinates (x, y) and perform a right mouse button click."
    set_mouse_to((x, y))
    right_click()


def double_right_click() -> None:
    "Perform two consecutive right mouse button clicks at the current mouse position."
    right_click()
    right_click()


def MiddleClick_at(x: int, y: int) -> None:
    "Move the mouse to the specified coordinates (x, y) and perform a middle mouse button click."
    set_mouse_to((x, y))
    middle_click()



def drag_to(x, y):
    "Drag the mouse from its current position to the specified coordinates (x, y)"
    left_mouse_down()
    set_mouse_to((x, y))
    left_mouse_up()


def drag_obj_to(x, y, a, b):
    "Drag an object from the starting coordinates (x, y) to the destination coordinates (a, b)."
    set_mouse_to((x, y))
    drag_to(a, b)




ClickMouseButtonList = [left_click, middle_click, right_click]
ClickMouseButton_atList = [left_click_at, MiddleClick_at, right_click_at]
HoldMouseButtonList = [left_mouse_down, middle_mouse_down, right_mouse_down]
ReleaseMouseButtonList = [left_mouse_up, right_mouse_up, middle_mouse_up]
