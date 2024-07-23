from .. import SYSTEM_NAME


if SYSTEM_NAME == "windows":
    import ctypes

    class POINT(ctypes.Structure):
        _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

    USER32 = ctypes.windll.user32
    KERNEL32 = ctypes.windll.kernel32

    # // Mouse
    CURSOR_POINT = POINT()

    WHEEL_DELTA = 120  # The number of wheel clicks per notch
    MOUSE_EVENTF_MOVE = 0x0001  # Move Mouse Event
    MOUSEEVENTF_LEFTDOWN = 0x0002  # MOUSEEVENTF_LEFTDOWN
    MOUSEEVENTF_LEFTUP = 0x0004  # MOUSEEVENTF_LEFTUP
    MOUSEEVENTF_RIGHTDOWN = 0x0008  # MOUSEEVENTF_RIGHTDOWN
    MOUSEEVENTF_RIGHTUP = 0x0010  # MOUSEEVENTF_RIGHTUP
    MOUSEEVENTF_MIDDLEDOWN = 0x0020  # MOUSEEVENTF_MIDDLEDOWN
    MOUSEEVENTF_MIDDLEUP = 0x0040  # MOUSEEVENTF_MIDDLEUP
    MOUSEEVENTF_WHEEL = 0x0800  # Mouse wheel event
    MOUSEEVENTF_HWHEEL = 0x01000  # Horizontal wheel movement
    MOUSE_EVENTF_ABSOLUTE = 0x8000  # Move absolute event

    # // Clipboard
    CF_TEXT = 1
    CF_UNICODETEXT = 13
    GMEM_DDESHARE = 0x2000
    OPEN_EXISTING = 3
    GMEM_MOVEABLE = 0x0002
    GMEM_ZEROINIT = 0x0040
    GHND = GMEM_DDESHARE | GMEM_MOVEABLE

    from .cursor.cursor_operations_ctypes import *

else:
    from .cursor.cursor_operations_pynput import *


def ClickMouseButton(button_number: int) -> None:
    ClickMouseButtonList[button_number]()


def HoldMouseButton(button_number: int) -> None:
    HoldMouseButtonList[button_number]()


def ReleaseMouseButton(button_number: int) -> None:
    ReleaseMouseButtonList[button_number]()


def ClickMouseButtonAt(button_number: int, x: int, y: int) -> None:
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


def LeftClick() -> None:
    Click()


def ClickAt(x: int, y: int) -> None:
    mouseTo(x, y)
    Click()


def DoubleClick() -> None:
    Click()
    Click()


def DoubleClickAt(x: int, y: int) -> None:
    mouseTo(x, y)
    Click()
    Click()


def TripleClick() -> None:
    Click()
    Click()
    Click()


def TripleClickAt(x: int, y: int) -> None:
    mouseTo(x, y)
    Click()
    Click()
    Click()


def RightClickAt(x: int, y: int) -> None:
    MouseTo(x, y)
    RightClick()


def DoubleRightClick() -> None:
    RightClick()
    RightClick()


def DoubleRightClickAt(x: int, y: int) -> None:
    mouseTo(x, y)
    RightClick()
    RightClick()


def TripleRightClickAt(x: int, y: int) -> None:
    mouseTo(x, y)
    RightClick()
    RightClick()
    RightClick()


def TripleRightClick() -> None:
    RightClick()
    RightClick()
    RightClick()


def MiddleClickAt(x: int, y: int) -> None:
    mouseTo(x, y)
    MiddleClick()


def DoubleMiddleClickAt(x: int, y: int) -> None:
    mouseTo(x, y)
    MiddleClick()
    MiddleClick()


def DoubleMiddleClick() -> None:
    MiddleClick()
    MiddleClick()


def TripleMiddleClick() -> None:
    MiddleClick()
    MiddleClick()
    MiddleClick()


def TripleMiddleClickAt(x: int, y: int) -> None:
    mouseTo(x, y)
    MiddleClick()
    MiddleClick()
    MiddleClick()


def drag_to(x, y):
    LeftMouseDown()
    mouseTo(x, y)
    LeftMouseUp()


def drag_obj_to(x, y, a, b):
    mouseTo(x, y)
    drag_to(a, b)


# def is_valid_mouse_buttons(x):
#     return x in ["left", "right", "middle"]


ClickMouseButtonList = [Click, MiddleClick, RightClick]
ClickMouseButtonAtList = [ClickAt, MiddleClickAt, RightClickAt]
HoldMouseButtonList = [LeftMouseDown, RightMouseDown, MiddleMouseDown]
ReleaseMouseButtonList = [LeftMouseUp, RightMouseUp, MiddleMouseUp]
