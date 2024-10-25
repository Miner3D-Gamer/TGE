from .. import SYSTEM_NAME


if SYSTEM_NAME == "windows":
    from .clipboard.clipboard_windows import get_clipboard, copy_to_clipboard, clear_clipboard  # type: ignore
    from .keyboard.windows import press_key, key_to_virtual_key
else:
    from .clipboard.clipboard_pyperclip import get_clipboard, copy_to_clipboard, clear_clipboard  # type: ignore
    from .keyboard.linux import press_key, key_to_virtual_key


def save_clipboard_to_file(file_path: str) -> bool:
    """
    Saves the current contents of the clipboard to a specified file.

    This function attempts to open the specified file in write mode and writes the content
    currently stored in the clipboard to it. It uses the 'utf-8' encoding for writing the file.

    Args:
        file_path (str): The path to the file where the clipboard content will be saved.

    Returns:
        bool: Returns True if the clipboard content was successfully saved to the file,
            otherwise returns False if an error occurs during the process.
    """
    clip = get_clipboard()
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(clip if clip else "")
        return True
    except:
        return False


def load_clipboard_from_file(file_path: str) -> bool:
    """
    Loads text content from a file and copies it to the clipboard.

    This function reads the content of a file located at the given 'file_path',
    assuming it is encoded in UTF-8. The file's text content is then copied to
    the clipboard using the 'copy_to_clipboard' function. If the operation is
    successful, the function returns True. If any errors occur during file
    reading or clipboard copying, it returns False.

    Args:
        file_path (str): The path to the file from which content will be read.

    Returns:
        bool: True if the text was successfully copied to the clipboard, False otherwise.
    """
    try:
        file = open(file_path, "r", encoding="utf-8")
        text = file.read()
        file.close()
        copy_to_clipboard(text)
        return True
    except:
        return False


def append_to_clipboard(text: str) -> None:
    """
    Appends the given text to the current content in the clipboard.

    Parameters:
    text (str): The text to be appended to the clipboard.

    Returns:
    None
        This function does not return any value.

    """
    clip = get_clipboard()
    clip += text
    copy_to_clipboard(clip)


def prepend_to_clipboard(text: str) -> None:
    """
    Prepends the provided text to the current clipboard content.

    This function takes a string 'text' and retrieves the current content
    of the clipboard using the 'get_clipboard()' function. It then prepends
    the provided 'text' to the clipboard content and updates the clipboard
    with the modified content using the 'copy_to_clipboard()' function.

    Parameters:
    text (str): The text to be prepended to the clipboard content.

    Returns:
    None: This function does not return any value, it directly modifies
        the clipboard content.
    """
    clip = get_clipboard()
    clip = text + clip
    copy_to_clipboard(clip)


def get_clipboard_size() -> int:
    """
    Get the size of the content currently stored in the clipboard.

    Returns:
        int: The size of the clipboard content in terms of the number of characters.
    """
    return len(get_clipboard())


def get_clipboard_file_extension() -> str:
    """
    Retrieves the file extension of the content currently stored in the clipboard.

    This function extracts the file extension from the content present in the clipboard.
    It first obtains the clipboard content using the 'get_clipboard()' function and then
    extracts the file extension using the 'get_file_extension()' utility function.

    Returns:
    str: The file extension of the content in the clipboard, or an empty string if no
        valid file extension is found.
    """
    return get_clipboard().split(".")[-1]


def write_out_clipboard():
    """
    Simulates typing out the contents of the clipboard.

    Retrieves the text from the clipboard and simulates key presses for each character, including newlines.
    """
    clipboard = get_clipboard()
    for line in clipboard.splitlines(True):
        for character in line:
            k = key_to_virtual_key(character)
            if k:
                press_key(k)
