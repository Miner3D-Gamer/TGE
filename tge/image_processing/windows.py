from typing import Tuple
import ctypes
from ctypes import wintypes
from PIL import Image


SRCCOPY = 0x00CC0020
DIB_RGB_COLORS = 0


class BITMAPINFOHEADER(ctypes.Structure):
    _fields_ = [
        ("biSize", wintypes.DWORD),
        ("biWidth", wintypes.LONG),
        ("biHeight", wintypes.LONG),
        ("biPlanes", wintypes.WORD),
        ("biBitCount", wintypes.WORD),
        ("biCompression", wintypes.DWORD),
        ("biSizeImage", wintypes.DWORD),
        ("biXPelsPerMeter", wintypes.LONG),
        ("biYPelsPerMeter", wintypes.LONG),
        ("biClrUsed", wintypes.DWORD),
        ("biClrImportant", wintypes.DWORD),
    ]


class BITMAPINFO(ctypes.Structure):
    _fields_ = [("bmiHeader", BITMAPINFOHEADER)]


user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32
hdc_screen = user32.GetDC(None)
hdc_mem = gdi32.CreateCompatibleDC(hdc_screen)
hbm = gdi32.CreateCompatibleBitmap(hdc_screen, 1, 1)
hbm_old = gdi32.SelectObject(hdc_mem, hbm)


def screenshot(position: Tuple[int, int], size: Tuple[int, int]) -> Image.Image:
    """
    Captures a screenshot of a specific screen area.

    Parameters:
    position (Tuple[int, int]): The (x, y) coordinates of the top-left corner of the screen area to capture.
    size (Tuple[int, int]): The (width, height) of the screen area to capture.

    Returns:
    Image.Image: An RGBA image of the captured screen area.

    The function uses Win32 APIs to capture the screen. It converts the captured 
    bitmap from BGRA to RGBA format before returning the image.
    """
    hdc_screen = user32.GetDC(None)
    hdc_mem = gdi32.CreateCompatibleDC(hdc_screen)
    hbm = gdi32.CreateCompatibleBitmap(hdc_screen, size[0], size[1])
    hbm_old = gdi32.SelectObject(hdc_mem, hbm)

    gdi32.BitBlt(
        hdc_mem, 0, 0, size[0], size[1], hdc_screen, position[0], position[1], SRCCOPY
    )

    bmi = BITMAPINFO()
    bmi.bmiHeader.biSize = ctypes.sizeof(BITMAPINFOHEADER)
    bmi.bmiHeader.biWidth = size[0]
    bmi.bmiHeader.biHeight = -size[1]  # Negative for top-down bitmap
    bmi.bmiHeader.biPlanes = 1
    bmi.bmiHeader.biBitCount = 32
    bmi.bmiHeader.biCompression = 0
    bmi.bmiHeader.biSizeImage = size[0] * size[1] * 4
    bmi.bmiHeader.biXPelsPerMeter = 0
    bmi.bmiHeader.biYPelsPerMeter = 0
    bmi.bmiHeader.biClrUsed = 0
    bmi.bmiHeader.biClrImportant = 0

    # Create a buffer to receive the image data
    buffer = ctypes.create_string_buffer(bmi.bmiHeader.biSizeImage)

    # Get the bitmap bits
    gdi32.GetDIBits(hdc_mem, hbm, 0, size[1], buffer, ctypes.byref(bmi), 0)

    # Clean up
    gdi32.SelectObject(hdc_mem, hbm_old)
    gdi32.DeleteObject(hbm)
    gdi32.DeleteDC(hdc_mem)
    user32.ReleaseDC(None, hdc_screen)

    # Convert buffer.raw from BGRA to RGBA
    raw_data = buffer.raw
    rgba_data = bytearray(b for b in raw_data)

    for i in range(0, len(rgba_data), 4):
        rgba_data[i], rgba_data[i + 2] = rgba_data[i + 2], rgba_data[i]

    return Image.frombytes("RGBA", size, bytes(rgba_data))


def get_pixel_color(pos: Tuple[int, int]) -> Tuple[int, int, int]:
    """
    Retrieves the RGB color of a specific pixel on the screen.

    Parameters:
    pos (Tuple[int, int]): The (x, y) coordinates of the pixel on the screen.

    Returns:
    Tuple[int, int, int]: The (R, G, B) color values of the pixel at the specified position.

    The function captures a 1x1 pixel area from the screen using Win32 APIs, extracts 
    the color data, and returns it as an RGB tuple.
    """
    gdi32.BitBlt(hdc_mem, 0, 0, 1, 1, hdc_screen, pos[0], pos[1], SRCCOPY)

    bmi = BITMAPINFO()
    bmi.bmiHeader.biSize = ctypes.sizeof(BITMAPINFOHEADER)
    bmi.bmiHeader.biWidth = 1
    bmi.bmiHeader.biHeight = -1  # Negative for top-down bitmap
    bmi.bmiHeader.biPlanes = 1
    bmi.bmiHeader.biBitCount = 32
    bmi.bmiHeader.biCompression = 0
    bmi.bmiHeader.biSizeImage = 0
    bmi.bmiHeader.biXPelsPerMeter = 0
    bmi.bmiHeader.biYPelsPerMeter = 0
    bmi.bmiHeader.biClrUsed = 0
    bmi.bmiHeader.biClrImportant = 0

    buffer = ctypes.create_string_buffer(4)

    gdi32.GetDIBits(hdc_mem, hbm, 0, 1, buffer, ctypes.byref(bmi), DIB_RGB_COLORS)

    # Cleanup
    gdi32.SelectObject(hdc_mem, hbm_old)
    gdi32.DeleteObject(hbm)
    gdi32.DeleteDC(hdc_mem)
    user32.ReleaseDC(None, hdc_screen)

    pixel = buffer.raw

    return pixel[2], pixel[1], pixel[0]
