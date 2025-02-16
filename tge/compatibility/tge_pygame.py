import os

import pygame
from typing import NoReturn, Callable, Tuple,List


from ..tbe import pass_func

__all__ = ['update_screen', 'render_text', 'load_images_from_directory', 'handle_events', 'check_collision', 'check_collision_with_all', 'pygame_exit', 'background_color', 'draw_texture_at', 'exit']

def update_screen(clock: pygame.time.Clock, fps: int = 0) -> None:
    """
    Update the display and control the frame rate.

    Parameters:
        clock (pygame.time.Clock): The Pygame clock object to control the frame rate.
        fps (int): The desired frames per second for the display.

    Returns:
        None: This function does not return anything.
    """
    pygame.display.update()
    clock.tick(fps)


def render_text(
    screen: pygame.Surface,
    text: str,
    font_name: str,
    size: int,
    color: Tuple[int, int, int],
    position: Tuple[int, int],
) -> None:
    """
    Renders and displays the given text on the specified Pygame screen.

    Parameters:
    - screen (pygame.Surface): The Pygame surface on which to render the text.
    - text (str): The text to be rendered.
    - font_name (str): The name of the font to be used for rendering.
    - size (int): The font size for rendering the text.
    - color (tuple): The RGB tuple representing the color of the rendered text.
    - position (tuple): The (x, y) tuple specifying the position to display the rendered text on the screen.

    Returns:
    - None: This function does not return any value.
    """
    font = pygame.font.SysFont(font_name, size)
    rendered_text = font.render(text, True, color)
    screen.blit(rendered_text, position)


def load_images_from_directory(directory_path: str) -> int:
    """
    Loads all images in the specified directory to pygame.

    Args:
        directory_path (str): The path of the directory.
    """

    supported_extensions: List[str] = [
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".bmp",
        ".tga",
        ".lbm",
        ".pbm",
        ".ppm",
        ".svg",
        ".tiff",
        ".webp",
        ".xbm",
        ".xpm",
        ".tif",
    ]
    files = 0

    for root, _, file_names in os.walk(directory_path):
        for file_name in file_names:
            file_path = os.path.join(root, file_name)
            if os.path.splitext(file_path)[1] not in supported_extensions:
                continue
            globals()[file_name] = pygame.image.load(file_path)
            files += 1
    return files


def handle_events(
    quit_callback: Callable[..., NoReturn] = exit,
    key_callback: Callable[..., None] = pass_func,
    mouse_button_callback: Callable[..., None] = pass_func,
    misc_callback: Callable[..., None] = pass_func,
) -> None:
    """
    Handles various events in a Pygame application.

    Args:
        quit_callback (function, optional): A callback function to handle the quit event.
            Defaults to the exit function.
        key_callback (function, optional): A callback function to handle key press events.
            Defaults to the pass_func function.
        mouse_button_callback (function, optional): A callback function to handle mouse button press events.
            Defaults to the pass_func function.

    Returns:
        None

    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_callback()
        elif event.type == pygame.KEYDOWN:
            key_callback(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_button_callback(event.button)
        else:
            misc_callback(event)


def check_collision(*rects: pygame.Rect) -> bool:
    """
    Check for collision between multiple rectangles.

    Parameters:
    - rects: Variable number of pygame.Rect objects representing the rectangles

    Returns:
    - True if any of the rectangles collide, False otherwise
    """
    for i in range(len(rects)):
        for j in range(i + 1, len(rects)):
            if rects[i].colliderect(rects[j]):
                return True
    return False


def check_collision_with_all(*rects: pygame.Rect) -> bool:
    """
    Check for collision with all rectangles.

    Parameters:
    - rects: Variable number of pygame.

    Returns:
    - True if all of the rectangles collide, False otherwise
    """
    for i in range(len(rects)):
        for j in range(len(rects)):
            if not rects[i].colliderect(rects[j]):
                return False
    return True


def pygame_exit() -> None:
    """
    ㅤ
    >>> pygame.quit()
    """
    pygame.quit()


def background_color(window: pygame.Surface, color: Tuple[ int, int, int]) -> None:
    """
    Fill the given Pygame window surface with the specified color.

    Args:
        window (pygame.Surface): The Pygame window surface to be filled.
        color (tuple): A tuple representing the RGB values of the desired color.

    Returns:
        None
    """
    window.fill(color)


def draw_texture_at(
    surface: pygame.Surface, texture: pygame.Surface, position: Tuple[int, int]
) -> None:
    """
    Draws a texture onto a surface at a specified position.

    Args:
        surface (pygame.Surface): The surface onto which the texture will be drawn.
        texture (pygame.Surface): The texture image to be drawn onto the surface.
        position (tuple): The position (x, y) where the texture will be drawn on the surface.

    Returns:
        None
    """
    surface.blit(texture, position)


def exit() -> NoReturn:
    """
    Exit the program safely and without errors just with one line
    >>> pygame.quit()
    >>> quit()
    """
    pygame.quit()
    quit()
