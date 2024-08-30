import os
from importlib import import_module as importlib_import_module
import pygame
from types import FunctionType
from typing import NoReturn

from ..random_generators import generate_random_string

from ..tbe import pass_func

from ..image_processing.image_operations import count_gif_frames


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
    color: tuple,
    position: tuple,
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


def load_images_from_directory(directory_path: str) -> None:
    """
    Loads all images in the specified directory to pygame.

    Args:
        directory_path (str): The path of the directory.
    """

    supported_extensions = [
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
    skipped = []
    files = {}

    for file in os.listdir(directory_path):
        file_name, file_extension = os.path.splitext(file)
        if file_extension in supported_extensions:
            try:
                if file_extension == ".gif":
                    if count_gif_frames(directory_path + "/" + file)[1] == 1:
                        pass
                    else:
                        skipped.append(file)
                        continue
                files[file_name] = file
            except:
                skipped.append(file)
                continue
    if len(files) == 0:
        return False
    successful_files = 0
    temp_file_name = generate_random_string(20)
    with open(f"{temp_file_name}.py", "w") as f:
        f.write("from pygame import image\n")
        f.write("def pygame_load_images_from_directory_temp_file():\n")
        f.write("\tsuccessful_files = 0\n")
        for file in files:
            f.write(f"\tglobal {file}\n")
            f.write(f"\t{file} = image.load('{directory_path}/{files[file]}')\n")
            f.write("\tsuccessful_files += 1\n")
        f.write("\treturn successful_files")
    try:
        generated_module = importlib_import_module(temp_file_name)
        successful_files = (
            generated_module.pygame_load_images_from_directory_temp_file()
        )
    except:
        return skipped, successful_files, False
    os.remove(f"{temp_file_name}.py")

    if len(skipped) == 0:
        return skipped, successful_files, True
    else:
        return skipped, successful_files, False


def handle_events(
    quit_callback: FunctionType = exit,
    key_callback: FunctionType = pass_func,
    mouse_button_callback: FunctionType = pass_func,
    misc_callback: FunctionType = pass_func,
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


def background_color(window: pygame.Surface, color: tuple) -> None:
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
    surface: pygame.Surface, texture: pygame.Surface, position: tuple
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



