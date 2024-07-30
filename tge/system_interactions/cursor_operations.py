from .. import SYSTEM_NAME

from.shared import *

if SYSTEM_NAME == "windows":
    from .cursor.cursor_operations_ctypes import *

else:
    from .cursor.cursor_operations_pynput import *


def ClickMouseButton(button_number: int) -> None:
    "Click the mouse button specified by `button_number`."
    ClickMouseButtonList[button_number]()


def HoldMouseButton(button_number: int) -> None:
    "Hold down the mouse button specified by `button_number`."
    HoldMouseButtonList[button_number]()


def ReleaseMouseButton(button_number: int) -> None:
    "Release the mouse button specified by `button_number`."
    ReleaseMouseButtonList[button_number]()


def ClickMouseButtonAt(button_number: int, x: int, y: int) -> None:
    "Click the mouse button specified by `button_number` at the coordinates (x, y)."
    ClickMouseButtonAtList[button_number](x, y)


# if True: #// Variants of setting the mouse position
#     def set_mouse_pos(x: int,y: int) -> None:
#         mouseTo(x, y)

#     def moveTo(x: int, y: int) -> None:
#         mouseTo(x, y)

#     def set_mouse_location(x: int, y: int) -> None:
#         mouseTo(x, y)

#     def move_mouse(x: int, y: int) -> None:
#         mouseTo(x, y)

#     def set_mouse_position(x: int, y: int) -> None:
#         mouseTo(x, y)

#     def move_cursor(x: int, y: int) -> None:
#         mouseTo(x, y)

#     def set_pointer_position(x: int, y: int) -> None:
#         mouseTo(x, y)

#     def move_pointer(x: int, y: int) -> None:
#         mouseTo(x, y)





def LeftClickAt(x: int, y: int) -> None:
    "Move the mouse to the specified coordinates (x, y) and perform a left mouse button click."
    mouseTo(x, y)
    LeftClick()


def DoubleLeftClick() -> None:
    "Perform two consecutive left mouse button clicks at the current mouse position."
    LeftClick()
    LeftClick()


def DoubleLeftClickAt(x: int, y: int) -> None:
    "Move the mouse to the specified coordinates (x, y) and perform two consecutive left mouse button clicks."
    mouseTo(x, y)
    LeftClick()
    LeftClick()


def RightClickAt(x: int, y: int) -> None:
    "Move the mouse to the specified coordinates (x, y) and perform a right mouse button click."
    MouseTo(x, y)
    RightClick()


def DoubleRightClick() -> None:
    "Perform two consecutive right mouse button clicks at the current mouse position."
    RightClick()
    RightClick()


def MiddleClickAt(x: int, y: int) -> None:
    "Move the mouse to the specified coordinates (x, y) and perform a middle mouse button click."
    mouseTo(x, y)
    MiddleClick()



def drag_to(x, y):
    "Drag the mouse from its current position to the specified coordinates (x, y)"
    LeftMouseDown()
    mouseTo(x, y)
    LeftMouseUp()


def drag_obj_to(x, y, a, b):
    "Drag an object from the starting coordinates (x, y) to the destination coordinates (a, b)."
    mouseTo(x, y)
    drag_to(a, b)


# def is_valid_mouse_buttons(x):
#     return x in ["left", "right", "middle"]


ClickMouseButtonList = [LeftClick, MiddleClick, RightClick]
ClickMouseButtonAtList = [LeftClickAt, MiddleClickAt, RightClickAt]
HoldMouseButtonList = [LeftMouseDown, RightMouseDown, MiddleMouseDown]
ReleaseMouseButtonList = [LeftMouseUp, RightMouseUp, MiddleMouseUp]
