from PIL import Image
from typing import Union, Tuple, Any
from numbers import Number
import numpy as np
from ..math_functions.math_functions import clamp
import math
from .middle_man import *


def rotate_image_file(image_path: str, angle: int) -> bool:
    """
    Rotate an image by the specified angle and save the rotated image back to the original path.

    Args:
        image_path (str): The file path to the image.
        angle (int): The angle in degrees by which to rotate the image clockwise.

    Returns:
        bool: True if the image rotation and saving were successful, False otherwise.

    Raises:
        This function does not raise any explicit exceptions. Any exceptions encountered during
        image processing or saving will cause the function to return False.

    Example:
        if rotate_image("image.jpg", 90):
            print("Image rotated successfully")
        else:
            print("Image rotation failed")
    """

    image = Image.open(image_path)
    rotated_image = image.rotate(angle)
    rotated_image.save(image_path)


def flip_image_file_vertically(image_path: str) -> bool:
    """
    Flips an image vertically and saves the result to the same file path.

    Args:
        image_path (str): The file path to the image.

    Returns:
        bool: True if the image was successfully flipped and saved, False otherwise.

    Notes:
        - This function uses the Pillow (PIL) library to open, flip, and save the image.
        - The original image is backed up before any modification attempt.
        - If an exception occurs during the flipping process, the function attempts to restore
          the original image from the backup and returns False.
    """

    image = Image.open(image_path)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    image.save(image_path)


def flip_image_file_horizontally(image_path: str) -> bool:
    """
    Flips an image horizontally and saves the result back to the original file path.

    Args:
        image_path (str): The path to the image file to be flipped.

    Returns:
        bool: True if the image was successfully flipped and saved, False otherwise.
    """

    image = Image.open(image_path)
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    image.save(image_path)
    return True


def add_anti_aliasing_to_image_file(image_path: str) -> bool:
    """
    Applies anti-aliasing to an image using a two-step resizing process.

    This function takes an image file path as input, opens the image, and applies
    anti-aliasing through a two-step process. The image is initially resized to
    double its dimensions and then back to its original dimensions, which helps
    in reducing aliasing artifacts. If the process is successful, the modified
    image is saved to the same path, and the function returns True. If any errors
    occur during the process, the function restores the original image and returns False.

    Args:
        image_path (str): The file path of the image to which anti-aliasing will be applied.

    Returns:
        bool: True if anti-aliasing is successfully applied and saved, False otherwise.
    """

    image = Image.open(image_path)
    image = image.resize((image.width * 2, image.height * 2))
    image.save(image_path)
    image = Image.open(image_path)
    image = image.resize((image.width // 2, image.height // 2))
    image.save(image_path)


def count_gif_frames(file_path) -> int:
    """
    Counts the number of frames in a GIF file.

    Args:
        file_path (str): The path to the GIF file.

    Returns:

    """

    with Image.open(file_path) as im:
        if hasattr(im, "is_animated") and im.is_animated:
            frame_count = 0
            while True:
                try:
                    im.seek(frame_count)
                    frame_count += 1
                except EOFError:
                    break
            return frame_count
        else:
            return -1




def image_to_ascii(
    image_path: str = "",
    image=None,
    width: int = None,
    unicode: bool = False,
    ascii_chars: str = "",
) -> str:
    """
    Convert an image into ASCII art.

    Parameters:
        image_path (str, optional): Path to the image file.
        image (PIL.Image.Image, optional): PIL image object.
        width (int, optional): Desired width of the ASCII art. If not specified, the width of the original image is used.
        unicode (bool, optional): Use Unicode characters for the ASCII art. If False, regular ASCII characters are used.
        ascii_chars (str, optional): Custom set of characters to be used for the ASCII art. If not specified, default characters are used based on the `unicode` flag.

    Returns:
        str: ASCII art representation of the image.

    Notes:
        - Provide either `image_path` or `image` parameter to specify the image source.
        - If `width` is not provided, the original image width is used.
        - The `unicode` flag determines whether to use Unicode or regular ASCII characters.
        - If `ascii_chars` is empty, a default set of characters is used based on the `unicode` flag.
        - Brighter pixels in the image correspond to darker characters in the ASCII art.
    """
    Image.MAX_IMAGE_PIXELS = None
    if image_path:
        if not image:
            image = Image.open(image_path)
    elif not image:
        return ""

    aspect_ratio = image.height / image.width
    if width is None:
        width = image.width
    height = int(width * aspect_ratio)
    image = image.resize((width, height)).convert("L")
    image_array = np.array(image)

    if ascii_chars == "":
        if unicode:
            ascii_chars = "█▮■▩▦▣▤@#$+=□:▫-. "
        else:
            ascii_chars = "@%#$*+=-:. "

    pixel_intensity = 255 - image_array
    ascii_chars_indices = (pixel_intensity / 255 * (len(ascii_chars) - 1)).astype(int)
    ascii_art_array = np.array(list(ascii_chars))[ascii_chars_indices]
    ascii_art = "\n".join("".join(row) for row in ascii_art_array)

    return ascii_art


def _load_image(image_path, alpha=True):
    """
    Loads an image and returns pixel data along with its dimensions.

    Args:
        image_path (str): The path to the image file.
        alpha (bool, optional): If True, retains the alpha channel (RGBA mode). If False, converts to RGB mode. Defaults to True.

    Returns:
        tuple: A tuple containing:
            - pixel_data (PixelAccess): Access object for image pixels.
            - width (int): Width of the image.
            - height (int): Height of the image.
    """

    image = Image.open(image_path)

    pixel_data = image.load()

    if not alpha:
        image = image.convert("RGB")

    width, height = image.size

    image.close()
    return pixel_data, width, height


def count_image_colors(image=None, image_path=None):
    """
    Counts unique colors in an image.

    Args:
        image (tuple, optional): A tuple containing the image data, width, and height. If not provided, `image_path` must be specified.
        image_path (str, optional): Path to the image file. Used if `image` is not provided.

    Returns:
        list: A list of unique colors in the image. Each color is represented as a tuple of RGB values.

    Notes:
        The image data should be in a format where `loaded_image[x, y]` returns an RGB tuple.
    """
    if image is None and image_path is None:
        return []

    if image is None:
        loaded_image, width, height = _load_image(image_path)
    else:
        if isinstance(image, tuple) and len(image) == 3:
            loaded_image, width, height = image
        else:
            return []

    unique_colors = set()

    for x in range(width):
        for y in range(height):
            pixel_value = loaded_image[x, y]
            unique_colors.add(pixel_value)

    return list(unique_colors)


def hex_to_rgb(hex_color):
    """
    Converts a hexadecimal color string to an RGB tuple.

    Args:
        hex_color (str): A color string in hexadecimal format (e.g., "#RRGGBB").

    Returns:
        Tuple[int, int, int]: A tuple containing the RGB components of the color.
    """
    hex_color = hex_color.lstrip("#")

    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)

    return (red, green, blue)


def hex_list_to_rgb_list(hex_list):
    """
    Converts a list of hexadecimal color strings to a list of RGB tuples.

    Args:
        hex_list (list): A list of color strings in hexadecimal format.

    Returns:
        list: A list of tuples, each containing the RGB components of a color.
    """
    rgb_list = []
    for i in hex_list:
        rgb_list.append(hex_to_rgb(i))

    return rgb_list


class Color:
    """
    A class representing an RGB color.

    Attributes:
        color (list): A list containing the RGB values of the color, each clamped between 0 and 255.
    """

    def __init__(self, color: Tuple[int, int, int]) -> None:
        """
        Initializes a Color instance with RGB values.

        Args:
            color (Tuple[int, int, int]): A tuple containing the RGB values of the color.
        """
        self.color = [
            clamp(0, 255, color[0]),
            clamp(0, 255, color[1]),
            clamp(0, 255, color[2]),
        ]

    def __repr__(self) -> str:
        """
        Returns a string representation of the Color instance.

        Returns:
            str: A string in the format "r{R} b{B} g{G}", where R, B, and G are the red, blue, and green components respectively.
        """
        return "r%s b%s g%s" % (self.color[0], self.color[1], self.color[2])

    def __iter__(self):
        """
        Returns an iterator over the RGB color components.

        Returns:
            iterator: An iterator for the RGB color values.
        """
        return iter(self.color)

    def get(self) -> Tuple[int, int, int]:
        """
        Returns the RGB color components as a list.

        Returns:
            list[int, int, int]: A list containing the red, green, and blue values.
        """
        return self.color

    def __call__(self):
        """
        Calls the instance to return the RGB color components.

        Returns:
            Tuple[int, int, int]: A tuple containing the red, green, and blue values.
        """
        return self.get()


def is_color_similar(
    a: Tuple[Number, Number, Number],
    b: Tuple[Number, Number, Number],
    similarity: Number,
) -> bool:
    """
    Determines if two RGB colors are similar within a given similarity threshold.

    Parameters:
    a (tuple[Number, Number, Number]): The first RGB color, as a tuple of three numbers.
    b (tuple[Number, Number, Number]): The second RGB color, as a tuple of three numbers.
    similarity (Number): The similarity threshold from a number range of 0 to 442.

    Returns:
    bool: True if the colors are similar within the threshold, False otherwise.
    """
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(3))) <= similarity
