import pyperclip


def copy_to_clipboard(text: str, user32: None = None, kernel32: None = None) -> None:
    """
    Copy text to the system clipboard.

    Args:
        text (str): The text to be copied to the clipboard.
    """
    pyperclip.copy(text)


def get_clipboard(user32: None = None, kernel32: None = None) -> str:
    """
    Retrieve the current content of the system clipboard.

    Returns:
        str: The text content currently stored in the clipboard.
    """
    return pyperclip.paste()


def clear_clipboard(user32: None = None) -> None:
    """
    Clear the contents of the clipboard.

    This function utilizes the 'pyperclip' library to copy an empty string to the clipboard,
    effectively clearing its contents.

    Returns:
        None: This function does not return any value.
    """
    pyperclip.copy("")
