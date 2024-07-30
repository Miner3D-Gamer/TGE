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
    return user32.MessageBoxW(None, message, title, style)

#print(show_message_box("text", "title", 6))


# Define necessary structures







