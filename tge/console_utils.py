import time
import os
from typing import List, Union, Tuple, Callable, Optional
from types import TracebackType
from random import random, choice
import sys
from collections.abc import Sequence
from typing import Union


from .tbe import determine_affirmative


if os.name == "nt":

    def clear() -> None:
        """
        Clears the terminal screen on Windows (NT-based systems).

        Uses the `cls` command to clear the screen.
        """
        os.system("cls")

else:

    def clear() -> None:
        """
        Clears the terminal screen on Unix-like systems (Linux, macOS, etc.).

        Uses the `clear` command to clear the screen.
        """
        os.system("clear")


def typing_print(text: str, delay: Union[int, float]) -> None:
    """
    Prints the given text with a typing effect.

    Args:
        text: The string to print.

    Returns:
        None
    """

    if not delay > 0:
        delay = 0.05
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)


def typingInput(text: str, delay: Union[int, float] = 0) -> str:
    """
    Displays the given text character by character with a delay of 0.05 seconds,
    then waits for the user to type a string and press Enter. Returns the entered string.

    Parameters:
    text (str): The text to be displayed before waiting for input.

    Returns:
    str: The string entered by the user.
    """
    if not delay > 0:
        delay = 0.05
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    value = input("")
    return value


def write_sentences_to_console(
    text: List[str], type_delay: Union[int, float], line_delay: Union[int, float] = 0.7
) -> None:
    """
    Writes a list of sentences

    Args:
    - punctuations: a list of valid sentence-ending punctuations
    - o_text: the input text to split into sentences and print

    """

    for line in text:
        typing_print(line, type_delay)
        time.sleep(line_delay)


def choose_from_text_menu(
    menu_list: "Sequence[str]", prompt: str = "", destroy: bool = False
) -> int:
    "..."
    #raise BaseException("This function needs a revamp :/")
    """
    Displays a text menu and prompts the user to choose an option.

    Args:
        text (list): Sequence of options to display in the menu.
        prompt (str): Prompt to display before the menu.
        ans_prompt (str): Prompt to display when asking for user input.

    Returns:
        int: The index of the chosen option in the 'text' list.

    Raises:
        None.

    """
    if not hasattr(menu_list, "__len__"):
        return -1
    print_string = ""
    prompt_lines = print_string.count("\n") + prompt.count("\n") + 2
    lines = prompt_lines+len(menu_list)
    for idx, item in enumerate(menu_list):
        print_string += f"{idx+1}: {item}\n"
    user_input =""
    while True:
        print(print_string)
        print(" "*(len(user_input)+len(prompt)))
        clear_lines(1)
        user_input = input(prompt)
        if user_input.isdigit():
            number_input = int(user_input)
            if number_input > 0 and number_input < (len(menu_list) + 1):
                if destroy:
                    clear_lines(lines)
                return number_input - 1
        else:
            for idx, item in enumerate(menu_list):
                if user_input == item:
                    if destroy:
                        clear_lines(lines)
                    return idx
        clear_lines(lines, False)


def skip_line() -> None:
    """Prints a newline character to skip to the next line."""
    print("\n")


def format_table(data: List[List[str]]) -> str:
    """
    Prints a table representation of the provided data.

    Args:
        data (list): A list of lists containing the data to be printed as a table.

    Returns:
        tuple: A tuple containing a boolean value and a string message.
            - The boolean value indicates the success or failure of the table printing.
            - The string message provides additional information in case of failure.

    Raises:
        None

    Example:
        data = [['Name', 'Age', 'Country'],
                ['John', 25, 'USA'],
                ['Emily', 32, 'Canada']]
        message = print_table(data)
    """
    stuff = ""
    column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]

    header = "+" + "+".join("-" * (width + 2) for width in column_widths) + "+"
    stuff += header + "\n"

    for row in data:
        formatted_row = (
            "| "
            + (
                " | ".join(
                    str(item).ljust(width) for item, width in zip(row, column_widths)
                )
            )
            + " |"
        )
        stuff += formatted_row + "\n"
    stuff += header
    return stuff


def progress_bar(
    progress_name: str,
    current: int,
    total: int,
    length: int,
    show_float: bool = True,
    empty_tile: str = "-",
    full_tile: str = "#",
) -> None:
    """
    Displays a progress bar indicating the completion of a task.

    Parameters:
    - progress_name (str): Name of the progress bar (optional).
    - current (int): Current progress value.
    - total (int): Total value representing the completion of the task.
    - length: Length of the progress bar (number of tiles).
    - show_float (bool): Determines whether to show the percentage as a float or an integer.
    - empty_tile (str): Symbol representing empty tiles in the progress bar (default: '-').
    - full_tile (str): Symbol representing filled tiles in the progress bar (default: '#').

    Returns:
    None

    Example:
    >>> progress_bar("Loading", 50, 100, 20, False,'-', '#')
    Loading: [##########----------] 50%
    """
    current += 1
    if show_float:
        percent = float(int(float(current / total * 100) * 10) / 10)

    else:
        percent = int(current / total * 100)
    filled_length = int(length * current // total)

    bar = f"{full_tile}" * filled_length + f"{empty_tile}" * (length - filled_length)
    if progress_name == "":
        sys.stdout.write(f"\r[{bar}] {percent}%")
        sys.stdout.flush()
    else:
        sys.stdout.write(f"\r{progress_name}: [{bar}] {percent}%")
        sys.stdout.flush()


def colorize_text(text: str, color: str) -> str:
    """
    Colorizes the input text using the specified color.

    Args:
        text (str): The text to be colorized.
        color (str): The color to be applied to the text. It should be one of the following options:
                    'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white',
                    'bright_black', 'bright_red', 'bright_green', 'bright_yellow', 'bright_blue',
                    'bright_magenta', 'bright_cyan', 'bright_white', 'bg_black', 'bg_red',
                    'bg_green', 'bg_yellow', 'bg_blue', 'bg_magenta', 'bg_cyan', 'bg_white',
                    'bg_bright_black', 'bg_bright_red', 'bg_bright_green', 'bg_bright_yellow',
                    'bg_bright_blue', 'bg_bright_magenta', 'bg_bright_cyan', 'bg_bright_white',
                    or 'reset'.

    Returns:
        str: The colorized text.

    Raises:
        ValueError: If an invalid color is specified.
    """
    colors = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "bright_black": "\033[90m",
        "bright_red": "\033[91m",
        "bright_green": "\033[92m",
        "bright_yellow": "\033[93m",
        "bright_blue": "\033[94m",
        "bright_magenta": "\033[95m",
        "bright_cyan": "\033[96m",
        "bright_white": "\033[97m",
        "bg_black": "\033[40m",
        "bg_red": "\033[41m",
        "bg_green": "\033[42m",
        "bg_yellow": "\033[43m",
        "bg_blue": "\033[44m",
        "bg_magenta": "\033[45m",
        "bg_cyan": "\033[46m",
        "bg_white": "\033[47m",
        "bg_bright_black": "\033[100m",
        "bg_bright_red": "\033[101m",
        "bg_bright_green": "\033[102m",
        "bg_bright_yellow": "\033[103m",
        "bg_bright_blue": "\033[104m",
        "bg_bright_magenta": "\033[105m",
        "bg_bright_cyan": "\033[106m",
        "bg_bright_white": "\033[107m",
        "reset": "\033[0m",
    }
    if color not in colors:
        raise ValueError("Invalid color specified.")
    return colors[color] + text + colors["reset"]


def visualize_directory(
    path: str, prefix: str = "", lines: Optional[List[str]] = None
) -> List[str]:
    """
    Recursively visualizes the directory structure of a given path.

    Args:
        path (str): The path of the directory to visualize.
        prefix (str, optional): The prefix for indentation in the visualization.
                                Defaults to an empty string.
        lines (list, optional): The list to store the visualization lines.
                                Defaults to an empty list.

    Returns:
        None

    Raises:
        None

    This function recursively traverses the directory structure starting from
    the given path and prints the directory structure using ASCII characters.
    Directories are represented in square brackets and files are indicated with
    a forward slash ("/"). If a directory or file cannot be accessed due to
    permission issues, "(Access Denied)" is displayed.

    Example:
        >>> visualize_directory('/path/to/directory')
        [directory]
        ├── [subdirectory1]
        │   ├── /file1.txt
        │   └── [subsubdirectory]
        └── [subdirectory2]
            ├── /file2.txt
            └── /file3.txt
    """
    if lines is None:
        lines = []

    if prefix == "":
        base_name = os.path.basename(path)
        lines.append(f"[{base_name}]")

    is_last = False
    last_marker = "└──"
    middle_marker = "├──"
    line_marker = "│   "
    empty_marker = "   "

    try:
        with os.scandir(path) as entries_r:
            entries = list(entries_r)
            for i, entry in enumerate(entries):
                is_last = i == len(entries) - 1
                marker = last_marker if is_last else middle_marker

                if entry.is_dir():
                    lines.append(f"{prefix}{marker}[{entry.name}]")
                    new_prefix = (
                        prefix + line_marker if not is_last else prefix + empty_marker
                    )
                    visualize_directory(entry.path, new_prefix, lines)
                else:
                    lines.append(f"{prefix}{marker}/{entry.name}")
    except PermissionError:
        marker = last_marker if is_last else middle_marker
        lines.append(f"{prefix}{marker}(Access Denied)")

    return lines


def clear_lines(num_lines: int, move_front: bool = False) -> None:
    """
    Clears a specified number of lines on the console screen.

    Args:
    num_lines (int): The number of lines to clear on the console screen.

    Returns:
    None: This function does not return anything.

    Raises:
    None

    Description:
    This function moves the cursor up num_lines lines on the console screen and clears the current line, effectively clearing a specified number of lines. It uses escape sequences to control the cursor and clear the line.

    Example:
    clear_lines(3)
    This will move the cursor up 3 lines and clear the current line, effectively clearing 3 lines on the console screen.
    """
    sys.stdout.write("\033[F\033[K" * num_lines)
    # "\033[K" # Clear the current line and move the cursor to the beginning
    # "\033[F" # Move cursor up
    # if move_front is true, the cursor should be moved by 1 character
    if move_front:
        sys.stdout.write("\033[F")


def prompt_bool(
    question: str,
    allow_undeterminable: bool = False,
    tries: int = 0,
    delete_lines: bool = True,
) -> Tuple[Optional[bool], str]:
    """
    Prompts the user with a yes/no question and returns their response.

    Args:
        question (str): The question to display to the user.
        allow_undeterminable (bool, optional): If True, returns None for invalid answers instead of retrying. Defaults to False.
        tries (int, optional): Union[int,float] of attempts allowed for a valid response. Defaults to 0 (no limit).
        delete_lines (bool, optional): If True, clears the input lines after each prompt. Defaults to True.
        return_value_when_tries_are_depleted (bool, optional): Value to return if the maximum number of tries is exceeded. Defaults to None.

    Returns:
        bool: The user's response, or the specified return_value_when_tries_are_depleted if the number of tries is exceeded.
        str: The raw user input.
    """
    tries_count = 0
    while True:
        tries_count += 1
        input_ans = str(input(question)).lower()
        ans = determine_affirmative(input_ans)
        if not ans is None:
            return ans, input_ans
        if allow_undeterminable:
            return ans, input_ans
        if tries > 0:
            if tries_count >= tries:
                return None, input_ans

        if delete_lines:
            clear_lines(1)


def prompt_number(
    question: str,
    min: Optional[int] = None,
    max: Optional[int] = None,
    delete_lines: bool = True,
    tries: int = 0,
) -> Optional[int]:
    """
    Asks the user a number question and validates the input.

    Args:
        question (str): The question to display to the user.
        min (int, optional): The minimum value allowed. Defaults to None.
        max (int, optional): The maximum value allowed. Defaults to None.
        delete_lines (bool, optional): If True, clears the input lines after each prompt. Defaults to True.
        tries (int, optional): Union[int,float] of attempts allowed for a valid response. Defaults to 0 (no limit).

    Returns:
        int: The validated input number or None if maximum tries reached.

    Raises:
        ValueError: If the input cannot be converted to an integer.

    """
    tries_count = 0
    while True:
        if tries > 0:
            if tries_count >= tries:
                return None
        tries_count += 1

        user_input: str = input(question)
        if delete_lines:
            clear_lines(1)
        if not user_input.isdigit():
            continue

        user_input_int: int = int(user_input)

        if not min is None:
            if user_input_int < min:
                continue
        if not max is None:
            if user_input_int > max:
                continue
        else:
            return user_input_int


def matrix_rain(
    rows: int,
    columns: int,
    speed: Union[int, float] = 0.1,
    density: Union[int, float] = 0.2,
    duration: Optional[Union[int, float]] = None,
    symbols: List[str] = ["0", "1"],
    callable_stop_if_return_true: Callable[..., bool] = lambda: False,
) -> None:
    """
    Displays a matrix rain animation on the console.

    Args:
        rows (int): The number of rows in the matrix.
        columns (int): The number of columns in the matrix.
        speed (float, optional): The speed at which the raindrops fall. Default is 0.1.
        density (float, optional): The density of raindrops in the matrix. Default is 0.2.
        duration (float, optional): The duration (in seconds) for which the matrix rain should be displayed. If not provided, it runs indefinitely.

    Returns:
        None

    Raises:
        None

    Note:
        - The raindrops are represented by '0' and '1' characters.
        - The console is cleared before each frame is printed.
    """
    mat_time = time.time()

    matrix = [[" " for _ in range(columns)] for _ in range(rows)]

    while True:
        for i in range(columns):
            if random() < density:
                matrix[0][i] = choice(symbols)
            else:
                matrix[0][i] = " "

        for i in range(rows - 1, 0, -1):
            for j in range(columns):
                matrix[i][j] = matrix[i - 1][j]

        matrix_str = ""
        idx = 0
        for row in matrix[1:]:
            matrix_str += "".join(row) + "\n"
            idx += 1

        clear_lines(rows + 1)
        print(matrix_str)

        if duration is not None:
            if time.time() - mat_time > duration:
                break
        if callable_stop_if_return_true():
            break

        time.sleep(speed)


class SuppressPrint:
    "To use:\nwith SuppressPrint():\n\tdo_something()"

    def __enter__(self):
        """To use:\nwith SuppressPrint():\n\tdo_something()"""
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")

    def __exit__(
        self,
        exc_type: Optional[Exception],
        exc_value: Optional[Exception],
        traceback: Optional[TracebackType],
    ) -> None:
        """To use:\nwith SuppressPrint():\n\tdo_something()"""
        sys.stdout.close()
        sys.stdout = self._original_stdout


__all__ = [
    "typing_print",
    "typingInput",
    "write_sentences_to_console",
    "choose_from_text_menu",
    "skip_line",
    "format_table",
    "progress_bar",
    "colorize_text",
    "visualize_directory",
    "clear_lines",
    "prompt_bool",
    "prompt_number",
    "matrix_rain",
    "SuppressPrint",
    "clear"
]
