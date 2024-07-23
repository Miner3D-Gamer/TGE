from ..cursor_operations import USER32, KERNEL32, ctypes, CF_UNICODETEXT, GHND

def get_clipboard(user32 = USER32, kernel32 = KERNEL32) -> str: # About 20% faster on Windows than with pyperclip
        """
        Retrieve the current content of the system clipboard.

        Returns:
            str: The text content currently stored in the clipboard.
        """
        user32.OpenClipboard(0)
        handle = user32.GetClipboardData(CF_UNICODETEXT)

        # Lock the memory to get a pointer to the data
        locked_mem = kernel32.GlobalLock(handle)
        data = ctypes.c_wchar_p(locked_mem).value

        # Unlock and close the clipboard
        kernel32.GlobalUnlock(handle)
        user32.CloseClipboard()

        return data
    
#set_clipboard_text
def copy_to_clipboard(text, user32 = USER32, kernel32 = KERNEL32): # Roughly 95% to 1515% faster on Windows than pyperclip
    """
    Copy text to the system clipboard.

    Args:
        text (str): The text to be copied to the clipboard.
    """
    user32.OpenClipboard(0)
    user32.EmptyClipboard()

    # Allocate memory for the text and copy it
    handle = kernel32.GlobalAlloc(GHND, (len(text) + 1) * ctypes.sizeof(ctypes.c_wchar))
    locked_mem = kernel32.GlobalLock(handle)
    ctypes.memmove(locked_mem, text.encode('utf-16le'), (len(text) + 1) * ctypes.sizeof(ctypes.c_wchar))

    # Unlock and set the clipboard data
    kernel32.GlobalUnlock(handle)
    user32.SetClipboardData(CF_UNICODETEXT, handle)
    user32.CloseClipboard()


def clear_clipboard(user32 = USER32) -> None: # Roughly 95% faster on Windows than pyperclip
    """
    Clear the contents of the clipboard.

    This function utilizes the 'pyperclip' library to copy an empty string to the clipboard,
    effectively clearing its contents.

    Returns:
        None: This function does not return any value.
    """
    user32.OpenClipboard(0)
    user32.EmptyClipboard()
    user32.CloseClipboard()