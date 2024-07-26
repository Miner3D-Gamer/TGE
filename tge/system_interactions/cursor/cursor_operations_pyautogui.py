from ..cursor_operations import WHEEL_DELTA
import pyautogui as pygui


def getScreenDimensions() -> tuple[int, int]:
    "Retrieve the dimensions of the screen as a tuple (width, height)."
    return pygui.size()


SCREEN_WIDTH, SCREEN_HEIGHT = getScreenDimensions()


def mouseTo(x: int, y: int) -> None:
    "Move the mouse cursor to the specified coordinates (x, y)."
    pygui.moveTo(x, y)


def mouseGet() -> tuple[int, int]:
    "Retrieve the current mouse cursor position as a tuple (x, y)."
    return pygui.position()


def LeftClick() -> None:
    "Perform a left mouse button click at the current mouse position."
    pygui.click(_pause=False)


def RightClick() -> None:
    "Perform a left mouse button click at the current mouse position."
    pygui.rightClick(_pause=False)


def MiddleClick() -> None:
    "Perform a middle mouse button click at the current mouse position."
    pygui.middleClick(_pause=False)


def ScrollV(clicks: int, wheel_delta: int = WHEEL_DELTA) -> None:
    "Uhh-"
    pass  # ???


def ScrollH(clicks: int, wheel_delta: int = WHEEL_DELTA) -> None:
    "Uhh-"
    pass  # ???


def Scroll(
    dx: int = None,
    dy: int = None,
    wheel_delta_x: int = WHEEL_DELTA,
    wheel_delta_y: int = WHEEL_DELTA,
):
    "Uhh-"
    pass  # pygui.scroll(dy, _pause=False)


def LeftMouseDown() -> None:
    "Press and hold the left mouse button."
    pygui.keyDown("left", _pause=False)


def RightMouseDown() -> None:
    "Press and hold the right mouse button."
    pygui.keyDown("right", _pause=False)


def MiddleMouseDown() -> None:
    "Press and hold the middle mouse button."
    pygui.keyDown("middle", _pause=False)


def LeftMouseUp() -> None:
    "Release the left mouse button."
    pygui.keyUp("left", _pause=False)


def RightMouseUp() -> None:
    "Release the right mouse button."
    pygui.keyUp("right", _pause=False)


def MiddleMouseUp() -> None:
    "Release the middle mouse button."
    pygui.keyUp("middle", _pause=False)
