from PIL import Image
from typing import Any, Union, Tuple, List, Optional, Set
from ..math_functions.math_functions import clamp
import math
from .middle_man import *


def count_gif_frames(gif: Image.Image) -> int:
    """
    Count the number of frames in a GIF image.

    Args:
        gif (PIL.Image.Image): The GIF image to count frames for.

    Returns:
        int: The number of frames in the GIF.
    """
    frame_count = 0
    try:
        while True:
            gif.seek(frame_count)
            frame_count += 1
    except EOFError:
        pass
    return frame_count


def image_to_ascii(
    image_path: str = "",
    image: Optional[Image.Image] = None,
    width: Optional[int] = None,
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
    import numpy as np

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


def _load_image(
    image_path: str, alpha: bool = True
) -> Optional[Tuple[Image.Image, int, int]]:
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

    pixel_data: Any = image.load()
    if not isinstance(pixel_data, Image.Image):
        return None

    if not alpha:
        pixel_data = image.convert("RGB")

    width, height = image.size

    image.close()
    return pixel_data, width, height


def count_image_colors(
    image: Optional[Image.Image] = None, image_path: Optional[str] = None
) -> List[Tuple[int, int, int]]:
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
        if image_path is None:
            return []
        thing = _load_image(image_path)
        if thing is None:
            return []
        loaded_image, width, height = thing
    else:
        loaded_image, width, height = image, image.width, image.height

    unique_colors: Set[Union[Tuple[int, int, int], Any]] = set()

    for x in range(width):
        for y in range(height):
            pixel_value = loaded_image.getpixel((x, y))
            unique_colors.add(pixel_value)

    return list(unique_colors)


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
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
        self.color: List[int] = [
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

    def get(self) -> List[int]:
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
    a: Tuple[Union[int, float], Union[int, float], Union[int, float]],
    b: Tuple[Union[int, float], Union[int, float], Union[int, float]],
    similarity: Union[int, float],
) -> bool:
    """
    Determines if two RGB colors are similar within a given similarity threshold.

    Parameters:
    a (tuple[Union[int,float], Union[int,float], Union[int,float]]): The first RGB color, as a tuple of three numbers.
    b (tuple[Union[int,float], Union[int,float], Union[int,float]]): The second RGB color, as a tuple of three numbers.
    similarity (Union[int,float]): The similarity threshold from a number range of 0 to 442.

    Returns:
    bool: True if the colors are similar within the threshold, False otherwise.
    """
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(3))) <= similarity


__all__ = [
    "count_gif_frames",
    "image_to_ascii",
    "count_image_colors",
    "hex_to_rgb",
    "Color",
    "is_color_similar",
]
