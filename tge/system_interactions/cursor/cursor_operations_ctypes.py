from ..shared import ctypes
from typing import Tuple

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]


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

VK_XBUTTON1 = 0x05 # 4th mouse button
VK_XBUTTON2 = 0x06 # 5th mouse button

MK_LBUTTON = 0x0001  # Left button
MK_MBUTTON = 0x0010  # Middle button
MK_RBUTTON = 0x0002  # Right button

# // Clipboard
CF_TEXT = 1
OPEN_EXISTING = 3
GMEM_ZEROINIT = 0x0040


def getScreenDimensions() -> Tuple[int, int]:
    "Retrieve the dimensions of the screen as a tuple (width, height)."
    return ctypes.windll.user32.GetSystemMetrics(
        0
    ), ctypes.windll.user32.GetSystemMetrics(1)


SCREEN_WIDTH, SCREEN_HEIGHT = getScreenDimensions()


def set_mouse_to(
    coords: Tuple[int, int],
    screen_width: int = SCREEN_WIDTH,
    screen_height: int = SCREEN_HEIGHT,
) -> None:
    "Move the mouse cursor to the specified coordinates (x, y)."

    # Calculate absolute position
    abs_x = int(65535 * (coords[0] / screen_width))
    abs_y = int(65535 * (coords[1] / screen_height))

    # Move the mouse cursor to the target position
    ctypes.windll.user32.mouse_event(
        MOUSE_EVENTF_MOVE | MOUSE_EVENTF_ABSOLUTE, abs_x, abs_y, 0, 0
    )


def get_mouse_position() -> Tuple[int, int]:
    "Retrieve the current mouse cursor position as a tuple (x, y)."
    ctypes.windll.user32.GetCursorPos(ctypes.byref(CURSOR_POINT))
    return CURSOR_POINT.x, CURSOR_POINT.y


def left_click() -> None:
    "Perform a left mouse button click at the current mouse position."
    # Perform a left mouse button click
    ctypes.windll.user32.mouse_event(
        MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0
    )  # MOUSEEVENTF_LEFTDOWN
    ctypes.windll.user32.mouse_event(
        MOUSEEVENTF_LEFTUP, 0, 0, 0, 0
    )  # MOUSEEVENTF_LEFTUP


def right_click() -> None:
    "Perform a left mouse button click at the current mouse position."
    # Perform a right mouse button click
    ctypes.windll.user32.mouse_event(
        MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0
    )  # MOUSEEVENTF_RIGHTDOWN
    ctypes.windll.user32.mouse_event(
        MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0
    )  # MOUSEEVENTF_RIGHTUP


def middle_click() -> None:
    "Perform a middle mouse button click at the current mouse position."
    ctypes.windll.user32.mouse_event(
        MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0
    )  # MOUSEEVENTF_MIDDLEDOWN
    ctypes.windll.user32.mouse_event(
        MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0
    )  # MOUSEEVENTF_MIDDLEUP

MOUSEEVENTF_XDOWN = 0x0080
MOUSEEVENTF_XUP = 0x0100


def click_mouse_button_4():
    """
    Simulates a click of the XButton1 mouse button (usually button 4).
    """
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_XDOWN, 0, 0, VK_XBUTTON1, 0)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_XUP, 0, 0, VK_XBUTTON1, 0)

def click_mouse_button_5():
    """
    Simulates a click of the XButton2 mouse button (usually button 5).
    """
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_XDOWN, 0, 0, VK_XBUTTON2, 0)
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_XUP, 0, 0, VK_XBUTTON2, 0)

def hold_mouse_button_4():
    """
    Simulates holding down the XButton1 mouse button (usually button 4).
    """
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_XDOWN, 0, 0, VK_XBUTTON1, 0)

def release_mouse_button_4():
    """
    Simulates releasing the XButton1 mouse button (usually button 4).
    """
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_XUP, 0, 0, VK_XBUTTON1, 0)

def hold_mouse_button_5():
    """
    Simulates holding down the XButton2 mouse button (usually button 5).
    """
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_XDOWN, 0, 0, VK_XBUTTON2, 0)

def release_mouse_button_5():
    """
    Simulates releasing the XButton2 mouse button (usually button 5).
    """
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_XUP, 0, 0, VK_XBUTTON2, 0)

def is_mouse_button_4_pressed():
    """
    Checks if the XButton1 mouse button (usually button 4) is currently pressed.
    Returns:
        bool: True if button 4 is pressed, False otherwise.
    """
    return (ctypes.windll.user32.GetAsyncKeyState(VK_XBUTTON1) & 0x8000) != 0

def is_mouse_button_5_pressed():
    """
    Checks if the XButton2 mouse button (usually button 5) is currently pressed.

    Returns:
        bool: True if button 5 is pressed, False otherwise.
    """
    return (ctypes.windll.user32.GetAsyncKeyState(VK_XBUTTON2) & 0x8000) != 0









def scroll_vertical(clicks: int, wheel_delta: int = WHEEL_DELTA) -> None:
    "Scroll the mouse wheel vertically by the specified number of `clicks`."
    # Simulate scrolling the mouse wheel up by sending wheel events
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_WHEEL, 0, 0, wheel_delta * clicks, 0)


def scroll_horizontal(clicks: int, wheel_delta: int = WHEEL_DELTA) -> None:
    "Scroll the mouse wheel horizontally by the specified number of `clicks`."
    ctypes.windll.user32.mouse_event(MOUSEEVENTF_HWHEEL, 0, 0, wheel_delta * clicks, 0)


def scroll(
    dx: int = None,
    dy: int = None,
    wheel_delta_x: int = WHEEL_DELTA,
    wheel_delta_y: int = WHEEL_DELTA,
) -> None:
    "Scroll the mouse wheel both horizontally and vertically by the specified amounts (`dx` and `dy`)."
    if dx:
        scroll_horizontal(dx, wheel_delta=wheel_delta_x)
    if dy:
        scroll_vertical(dy, wheel_delta=wheel_delta_y)


def left_mouse_down() -> None:
    "Press and hold the left mouse button."
    ctypes.windll.user32.mouse_event(
        MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0
    )  # MOUSEEVENTF_LEFTDOWN


def right_mouse_down() -> None:
    "Press and hold the right mouse button."
    ctypes.windll.user32.mouse_event(
        MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0
    )  # MOUSEEVENTF_RIGHTDOWN


def middle_mouse_down() -> None:
    "Press and hold the middle mouse button."
    ctypes.windll.user32.mouse_event(
        MOUSEEVENTF_MIDDLEDOWN, 0, 0, 0, 0
    )  # MOUSEEVENTF_MIDDLEDOWN


def left_mouse_up() -> None:
    "Release the left mouse button."
    ctypes.windll.user32.mouse_event(
        MOUSEEVENTF_LEFTUP, 0, 0, 0, 0
    )  # MOUSEEVENTF_LEFTUP


def right_mouse_up() -> None:
    "Release the right mouse button."
    ctypes.windll.user32.mouse_event(
        MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0
    )  # MOUSEEVENTF_RIGHTUP


def middle_mouse_up() -> None:
    "Release the middle mouse button."
    ctypes.windll.user32.mouse_event(
        MOUSEEVENTF_MIDDLEUP, 0, 0, 0, 0
    )  # MOUSEEVENTF_MIDDLEUP


def is_left_button_pressed():
    """Check if the left mouse button is pressed."""
    return (ctypes.windll.user32.GetAsyncKeyState(MK_LBUTTON) & 0x8000) != 0


def is_middle_button_pressed():
    """Check if the middle mouse button is pressed."""
    return (ctypes.windll.user32.GetAsyncKeyState(MK_MBUTTON) & 0x8000) != 0


def is_right_button_pressed():
    """Check if the right mouse button is pressed."""
    return (ctypes.windll.user32.GetAsyncKeyState(MK_RBUTTON) & 0x8000) != 0
