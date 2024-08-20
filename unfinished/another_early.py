import ctypes
from ctypes import wintypes

user32 = ctypes.windll.user32


def show_message_box(message, title, style):
    """
    Display a message box.

    Parameters:
    message (str): The message to display.
    title (str): The title of the message box.
    style (int): The style of the message box.

    Returns:
    int: The result of the message box.
    """
    selected = user32.MessageBoxW(None, message, title, style)
    return ["invalid style", "ok", "cancel", "abort", "retry", "ignore", "yes", "no", "unused (8)", "unused (9)", "try again", "continue"][selected]


print(show_message_box("hi", "title", 6))
