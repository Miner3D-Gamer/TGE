from ..shared import  ctypes

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

# // Clipboard
CF_TEXT = 1
OPEN_EXISTING = 3
GMEM_ZEROINIT = 0x0040

def getScreenDimensions() -> "tuple[int, int]":
    "Retrieve the dimensions of the screen as a tuple (width, height)."
    return ctypes.windll.user32.GetSystemMetrics(
        0
    ), ctypes.windll.user32.GetSystemMetrics(1)


SCREEN_WIDTH, SCREEN_HEIGHT = getScreenDimensions()


def set_mouse_to(
    x: int, y: int, screen_width: int = SCREEN_WIDTH, screen_height: int = SCREEN_HEIGHT
) -> None:
    "Move the mouse cursor to the specified coordinates (x, y)."

    # Calculate absolute position
    abs_x = int(65535 * (x / screen_width))
    abs_y = int(65535 * (y / screen_height))

    # Move the mouse cursor to the target position
    ctypes.windll.user32.mouse_event(
        MOUSE_EVENTF_MOVE | MOUSE_EVENTF_ABSOLUTE, abs_x, abs_y, 0, 0
    )


def get_mouse_position() -> "tuple[int, int]":
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
