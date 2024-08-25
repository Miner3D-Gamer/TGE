import os
import shutil
from ast import parse as ast_parse, walk as ast_walk, FunctionDef as ast_FunctionDef
import zipfile
import math
import hashlib
import uuid
from typing import Union, Tuple, Iterable, List
from collections import defaultdict
import tkinter as tk
import re

from .codec.codec import decode, base_x_decode_to_binary, base_x_encode_binary
from . import SYSTEM_NAME

def make_legal_filename(filename: str) -> str:
    illegal_chars = r'[\\/*?"<>|:]'
    
    legal_filename = re.sub(illegal_chars, '_', filename)
    
    legal_filename = legal_filename.strip()
    
    return legal_filename

def create_missing_directory(directory: str) -> bool:
    """
    Creates a directory at the given path if it does not already exist.

    Args:
        directory (str): The path of the directory to create.

    Returns:
        Boolean: True if the directory was created, False if it already existed.

    If the directory already exists, this function does not modify it and does not raise any exceptions.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        return True
    else:
        return False


def delete_directory(directory: str) -> Tuple[bool, str]:
    """
    Deletes a directory and its contents.

    Args:
        directory (str): The name of the directory to delete.

    Returns:
        Tuple[bool, str]: A tuple with two items: a boolean indicating whether
        the directory was successfully deleted, and a string with a message
        indicating the result of the operation.
    """
    try:
        parent_dir = os.path.dirname(__file__)
        full_path = os.path.join(parent_dir, directory)

        if os.path.exists(full_path):
            shutil.rmtree(full_path)
            return True, "Directory deleted"
        else:
            return False, "Directory not found"
    except:
        return False, "Error deleting directory"


def write_save_data(name: str, dir: str, data) -> Tuple[bool, str]:
    """
    Saves data to a file with the given name in the specified directory.

    :param name: The name of the file to be saved, without the ".save" extension.
    :param dir: The directory where the file should be saved.
    :param data: The data to be written to the file.
    :return: A tuple (success, message) where success is True if the file was saved
             successfully and False otherwise, and message is a string with a status
             message or an error message if an exception occurred.
    """
    try:
        name = name.replace(".save", "")
        file_path = os.path.join(dir, f"{name}.save")
        with open(file_path, "w") as f:
            f.write(data)
            return True, "File saved"
    except Exception as e:
        return False, f"Error saving file: {str(e)}"


def load_save_data(name: str, dir: str) -> Tuple[bool, str]:
    """
    Loads a file and returns the data.

    Args:
        name (str): The name of the .save file to load.
        dir (str): The directory containing the file to load.

    Returns:
        tuple: A tuple containing a boolean indicating success and the decoded data.
            The boolean is True if the file was loaded and decoded successfully, and False
            otherwise. The decoded data is returned as bytes if decoding was successful,
            or a string containing an error message if decoding was not successful.
    """
    try:
        name = name.rstrip(".save", "")
        file_path = os.path.join(dir, f"{name}.save")
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                data = f.read()
                success, decoded_data = decode(data)
                if success:
                    return True, decoded_data
                else:
                    return False, decoded_data
        else:
            return False, "File not found"
    except Exception as e:
        return False, f"Error loading file: {str(e)}"


def move_file(source_path: str, destination_path: str) -> None:
    """
    Move a file from the source path to the destination path.

    This function checks if the file exists at the given source path and verifies its presence.
    If the file exists, it creates any missing directories in the destination path and then
    performs the file move using the `shutil.move` function. Returns True if the move is successful,
    and False if the source file does not exist.

    Args:
        source_path (str): The path to the source file.
        destination_path (str): The desired path for the moved file.

    Returns:
        bool: True if the file is successfully moved, False if the source file doesn't exist.

    """
    shutil.move(source_path, destination_path)


def copy_file(source_path: str, destination_path: str) -> bool:
    """
    Copies a file from the source path to the destination path.

    Args:
        source_path (str): The path to the source file.
        destination_path (str): The path where the file will be copied.

    Returns:
        bool: True if the file was successfully copied, False otherwise.
    """
    shutil.copy(source_path, destination_path)


def rename_file(source_path: str, name: str) -> bool:
    """
    Renames a file located at the given source path with the specified name.

    Args:
        source_path (str): The current path of the file to be renamed.
        name (str): The new name to be assigned to the file.

    Returns:
        bool: True if the file is successfully renamed, False otherwise.
    """
    file_path = os.path.dirname(source_path)
    new_path = os.path.join(file_path, name)
    os.rename(source_path, new_path)


def copy_directory(source_path: str, destination_path: str) -> bool:
    """
    Copy the contents of a source directory to a destination directory.

    This function attempts to copy all files and subdirectories from the source directory
    to the destination directory. If the source directory exists and the copy operation is successful,
    the function returns True. If the source directory doesn't exist or an error occurs during the copy,
    the function returns False.

    Args:
        source_path (str): The path to the source directory to be copied.
        destination_path (str): The path to the destination directory where contents will be copied.

    Returns:
        bool: True if the copy operation is successful, False otherwise.
    """

    create_missing_directory(destination_path)
    shutil.copytree(source_path, destination_path)


def move_directory(source_path: str, destination_path: str) -> bool:
    """
    Move a directory or file from the source path to the destination path.

    This function attempts to move the directory or file located at the source path
    to the specified destination path. If the source path points to an existing
    directory or file, the function creates any missing directories in the destination
    path and performs the move operation.

    Args:
        source_path (str): The path to the source directory or file.
        destination_path (str): The desired path for the moved directory or file.

    Returns:
        bool: True if the move operation is successful, False otherwise.
    """

    create_missing_directory(destination_path)
    shutil.move(source_path, destination_path)


def rename_directory(source_path: str, name: str) -> bool:
    """
    Renames a directory at the given source path with the new provided name.

    This function attempts to rename the specified directory by changing its name
    to the provided new name while maintaining its location. The function first
    checks if the directory exists using the 'doesDirectoryFileExist' function.
    If the directory exists, it is renamed by updating its path accordingly.

    Args:
        source_path (str): The current path of the directory to be renamed.
        name (str): The new name to be assigned to the directory.

    Returns:
        bool: True if the directory was successfully renamed, False otherwise.
    """
    file_path = os.path.dirname(source_path)
    new_path = os.path.join(file_path, name)
    os.rename(source_path, new_path)


def get_folder_name(path: str) -> str:
    """
    Get the parent folder name from the given path.

    This function takes a path as input and returns the name of the parent folder.

    Args:
        path (str): A string representing the path to a file or directory.

    Returns:
        str: The name of the parent folder extracted from the path.

    Note:
        - The path can use either forward slashes ('/') or backslashes ('\\') as separators.
        - If the given path points to a directory, the name of the last folder in the path is returned.
        - If the given path points to a file, the name of the second-to-last folder in the path is returned.
          (This is assuming the file is located inside a folder within the path.)

    Examples:
        >>> get_parent_folder("C:\\Users\\Username\\Documents\\file.txt")
        'Documents'
        >>> get_parent_folder("/home/user/pictures")
        'pictures'
    """
    file_path = path.replace("\\", "/")
    if os.path.isdir(path):
        return file_path.split("/")[-1]
    else:
        final_file_path = file_path.split("/")[-2]
        return final_file_path


def combine_files(directory: str, output_directory: str, name: str) -> bool:
    """
    Combines multiple files from a directory into a single encrypted file.

    Args:
        directory (str): The directory path containing the files to be combined.
        output_directory (str): The directory path where the combined file will be saved.
        name (str): The name of the combined file (without extension).

    Returns:
        bool: True if the files are successfully combined and saved as an encrypted file,
              False if an error occurs during the process.

    Raises:
        Any exceptions raised during the execution will be caught and cause the function to return False.
    """
    try:
        file_data = []
        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)

            if os.path.isfile(file_path):
                with open(file_path, "rb") as file:
                    file_bytes = file.read()
                    file_data.append((file_name, file_bytes))

        combined_data = b""
        for file_name, file_bytes in file_data:
            combined_data += file_name.encode() + b":" + file_bytes + b"|"

        encoded_data = base_x_encode_binary(combined_data)

        output_file = os.path.join(output_directory, name + ".encrypted")
        with open(output_file, "wb") as file:
            file.write(encoded_data)

        return True
    except:
        return False


def split_file(directory: str, output_directory: str) -> bool:
    """
    Splits a combined encrypted file into individual files and saves them to the output directory.

    Args:
        directory (str): The path of the combined encrypted file.
        output_directory (str): The directory path where the individual files will be saved.

    Returns:
        bool: True if the combined file is successfully split into individual files and saved,
              False if an error occurs during the process.

    Raises:
        Any exceptions raised during the execution will be caught and cause the function to return False.
    """
    try:
        with open(directory, "rb") as file:
            encoded_data = file.read()

        combined_data = base_x_decode_to_binary(encoded_data).decode("utf-8")

        file_data = combined_data.split(b"|")[:-1] 

        for data in file_data:
            file_name, file_bytes = data.split(b":", 1)
            output_file_path = os.path.join(output_directory, file_name.decode())
            with open(output_file_path, "wb") as file:
                file.write(file_bytes)
        return True
    except:
        return False




def does_file_exist(directory: str) -> bool:
    """
    Check if a file exists at the specified directory.

    Parameters:
    directory (str): The path to the directory or file to check.

    Returns:
    bool: True if the file exists and is a regular file, False otherwise.
    """
    return os.path.exists(directory) and os.path.isfile(directory)


def does_directory_exist(directory: str) -> bool:
    """
    Check if the specified directory exists and is a valid directory.

    Parameters:
    directory (str): The path to the directory to be checked.

    Returns:
    bool: True if the directory exists and is a valid directory, False otherwise.
    """
    return os.path.exists(directory) and os.path.isdir(directory)


def delete_file(directory: str) -> bool:
    """
    Deletes a file from a directory.

    Args:
        name (str): The name of the file to delete.
        dir (str): The name of the directory where the file is located.

    """
    os.remove(directory)


def compare_file(directory1: str, directory2: str) -> bool:
    """
    Compares the contents of two files and returns True if they are identical, False otherwise.

    Args:
        directory1 (str): The path to the first file.
        directory2 (str): The path to the second file.

    Returns:
        bool: True if the contents of the files are identical, False otherwise.


    """
    with open(directory1, "rb") as f1, open(directory2, "rb") as f2:
        return f1.read() == f2.read()


def are_directories_the_same(
    directory1: str,
    directory2: str,
    dir1_blacklist: list = [],
    dir2_blacklist: list = [],
) -> bool:
    """

    Args:
        directory1 (str): The path to the first directory.
        directory2 (str): The path to the second directory.

    Returns:
        Union[bool, str]:
        - If the directories are the same, returns True
        - If the directories are different, returns False
    """

    return generate_uuid_from_directory(
        directory1, dir1_blacklist
    ) == generate_uuid_from_directory(directory2, dir2_blacklist)


def count_items_in_directory(directory_path) -> int:
    """
    Counts the number of items (files and directories) in the specified directory.

    Args:
        directory_path (str): The path of the directory.

    Returns:
        int: The total count of items in the directory.
    """
    return len(os.listdir(directory_path))


def get_current_working_directory() -> str:
    """
    Retrieve the current working directory path.

    Attempts to fetch the absolute path of the current working directory using the `os.getcwd()` function.

    Returns:
        str: The absolute path of the current working directory.
             Returns an empty string if an exception occurs during the retrieval process.
    """
    try:
        return os.getcwd()
    except:
        return ""


def get_file_extension(file_path: str) -> str:
    """
    Return the file extension from a given file path.

    :param file_path: A string representing the file path.
    :type file_path: str
    :return: A string representing the file extension.
    :rtype: str
    """
    return os.path.splitext(file_path)[1][1:]


def find_files_by_extension(directory_path: str, extension: str) -> list:
    """
    Retrieve a list of file names within the given directory that match the specified extension.

    Args:
        directory_path (str): The path to the directory where files will be searched.
        extension (str): The target file extension to filter files by.

    Returns:
        list: A list of file names that have the specified extension within the directory.
    """
    result = []
    for file in os.listdir(directory_path):
        _, file_extension = os.path.splitext(file)
        if file_extension == extension:
            result.append(file)
    return result


def get_file_size(file_path: str) -> int:
    """
    Get the size of a file located at the specified 'file_path'.

    This function checks if the provided path points to a valid file on the system.
    If the file exists, its size in bytes is returned; otherwise, 0 is returned.

    Args:
        file_path (str): The path to the file for which the size is to be determined.

    Returns:
        int: The size of the file in bytes if it exists, or 0 if the file doesn't exist.
    """
    if os.path.isfile(file_path):
        return os.path.getsize(file_path)
    else:
        return 0


def get_file_creation_time(file_path: str) -> str:
    """
    Retrieve the creation time of a file.

    This function takes a file path as input and returns the creation time
    of the file as a formatted string. If the provided path does not point
    to a valid file, an empty string is returned.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: A formatted string representing the creation time of the file,
        or an empty string if the file does not exist.
    """
    if os.path.isfile(file_path):
        return os.path.getctime(file_path)
    else:
        return ""


def count_functions_in_file(file_path: str) -> Tuple[int, list]:
    """
    Count and retrieve the names of top-level functions defined in the specified Python file.

    This function reads the content of the given Python file, parses its abstract syntax tree (AST),
    and identifies all top-level functions. It then returns the count of functions and a list of their names.

    Args:
        file_path (str): The path to the Python file to be analyzed.

    Returns:
        Tuple[int, list]: A tuple containing two elements:
            - The total number of top-level functions found in the file.
            - A list containing the names of the identified functions.

        If an error occurs during file reading or parsing, the function returns (0, []).
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            tree = ast_parse(file.read())
            functions = [
                node.name
                for node in ast_walk(tree)
                if isinstance(node, ast_FunctionDef)
            ]
            return len(functions), functions
    except:
        return 0, []


def count_functions_in_directory(directory_path: str) -> Tuple[int, dict, list]:
    """
    Counts the number of functions in all Python files within a directory and its subdirectories.
    Returns a dictionary where the keys are the file paths and the values are tuples with the count and names of functions.
    Also returns the total count of functions across all files.

    Args:
        directory_path (str): The path to the directory.

    Returns:
        tuple: A tuple containing the dictionary with file paths and function details, and the total count of functions.

    Raises:
        NotADirectoryError: If the specified directory path does not exist or is not a directory.
        IOError: If there was an error while reading any of the files.

    Example:
        >>> count_functions_in_directory('my_directory')
        (
            4,
            {
                'my_directory/file1.py': (3, ['function1', 'function2', 'function3']),
                'my_directory/subdirectory/file2.py': (1, ['function4'])
            },
        )
    """
    function_counts = {}
    total_function_count = 0
    error_files = []

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        tree = ast_parse(file.read())
                        functions = [
                            node.name
                            for node in ast_walk(tree)
                            if isinstance(node, ast_FunctionDef)
                        ]
                        function_counts[file_path] = (len(functions), functions)
                        total_function_count += len(functions)
                except IOError:
                    error_files.append(file_path)

    return total_function_count, function_counts, error_files


def count_function_names_in_directory(directory_path: str) -> Tuple[int, list]:
    """
    Count the total number of function names in Python files within the specified directory.

    This function recursively searches through all the Python files in the given directory
    and its subdirectories, tallying the total number of function names encountered. It returns
    a tuple containing the total count of function names and a list of unique function names.

    Args:
        directory_path (str): The path to the directory to be searched for Python files.

    Returns:
        Tuple[int, list]: A tuple containing the total count of function names and a list of
        unique function names extracted from the Python files.

    Note:
        This function depends on the 'count_functions_in_directory' utility function to perform
        the actual counting of function occurrences in the directory's Python files.
    """
    total_function_count, function_counts, error_files = count_functions_in_directory(
        directory_path
    )
    function_names = []

    for file_path, (count, names) in function_counts.items():
        for name in names:
            function_names.append(name)

    return len(function_names), function_names


def save_counted_function_names_from_directory(
    directory_path: str,
    file_name: str,
    output_path: str,
    create_missing_directory_bool: bool,
) -> bool:
    """
    Count the occurrences of function names in the Python files within the specified directory and save them to a file.

    Args:
        directory_path (str): The path to the directory containing Python files for function name counting.
        file_name (str): The name of the output file where the counted function names will be saved.
        output_path (str): The directory path where the output file will be saved.
        create_missing_directory_bool (bool): A flag indicating whether to create the output directory if it's missing.

    Returns:
        bool: True if the function names were successfully counted and saved, False otherwise.
    """
    functions = count_function_names_in_directory(directory_path)[1]
    if directory_path == "":
        directory_path = get_current_working_directory()

    if output_path == "":
        output_path = directory_path

    if file_name == "":
        file_name = "functions.txt"

    if create_missing_directory_bool:
        create_missing_directory(output_path)
    try:
        with open(output_path + file_name, "w", encoding="utf-8") as f:
            for name in functions:
                f.write(name + "\n")
        return True
    except:
        return False


def input_file_path(extension: str = None) -> str:
    """
    Prompts the user to select a file path for saving a file.

    This function opens a file dialog that allows the user to specify a file path
    for saving a file. The 'extension' parameter can be used to suggest a default
    file extension for the saved file.

    Parameters:
        extension (str, optional): A suggested file extension for the saved file.
            If provided, the file dialog will include this extension in the suggested
            file name and in the file type dropdown filter. Defaults to None.

    Returns:
        str: The selected file path for saving the file, including the chosen file name
        and extension.

    Note:
        This function requires the 'tkinter.filedialog' module to be imported in
        order to work properly.

    Example:
        >>> input_file_path(extension=".txt")
        '/path/to/save/file.txt'
    """
    return tk.filedialog.asksaveasfilename(defaultextension=extension)


def input_directory_path() -> str:
    """
    Prompt user to select a directory using a file dialog.

    This function opens a file dialog window that allows the user to choose a directory.
    The selected directory's path is returned as a string.

    Returns:
        str: The path of the selected directory.
    """
    save_path = tk.filedialog.askdirectory()
    return save_path


def unzip_file(
    zip_path: str, extract_dir: str, create_missing_directory_bool: bool = False
) -> Tuple[bool, bool]:
    """
    Unzips a zip file to the specified extract directory.

    Args:
        zip_path (str): path to the zip file.
        extract_dir (str): Directory to extract the contents of the zip file to.
    """
    if zip_path == "":
        return False, False
    if extract_dir == "":
        return False, False
    try:
        if create_missing_directory_bool:
            existed = create_missing_directory(extract_dir)
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_dir)
        return True, True
    except:
        if create_missing_directory_bool:
            if existed:
                delete_directory(extract_dir)
        return False, True


def zip_directory(
    directory_path: str, output_path: str, create_missing_directory_bool: bool = False
) -> Tuple[bool, bool]:
    """
    Zip a given directory and save the resulting zip file to the output path.

    Args:
        directory_path (str): path to the directory to be zipped.
        output_path (str): path to save the resulting zip file.

    Returns:
        None
    """
    if directory_path == "":
        return False, False
    if output_path == "":
        return False, False
    if not output_path.endswith(".zip"):
        output_path += ".zip"
    try:
        if create_missing_directory_bool:
            create_missing_directory(output_path)

        with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipfile:
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipfile.write(file_path, os.path.relpath(file_path, directory_path))
        return True, True
    except:
        return False, True


def get_appdata_path() -> str:
    """
    Retrieve the path to the 'AppData' directory of the current user.

    Returns:
        str: The expanded and absolute path to the 'AppData' directory.
    """
    return os.path.expanduser("~\AppData")


# def create_shortcut(
#     name: str, target_path: str, shortcut_path: str, description: str = ""
# ) -> None:
#     """
#     Creates a shortcut to a target file or script.

#     This function generates a shortcut (or symbolic link) to a specified target file or script
#     at the specified shortcut path location. Additional properties like the working directory,
#     description, and execution settings can be customized for the shortcut.

#     Args:
#         name (str): The name of the shortcut (without the file extension).
#         target_path (str): The path to the target file or script that the shortcut points to.
#         shortcut_path (str): The path where the shortcut should be created.
#         description (str, optional): An optional description for the shortcut (default is "").

#     Returns:
#         None

#     Note:
#         - The 'pyshortcuts' library is used to create the shortcut. Make sure it is installed.
#         - The 'executable' parameter is set to 'target_path', indicating the executable to run
#         when the shortcut is activated.

#     """
#     target_parent_folder = os.path.dirname(target_path)
#     pyshortcuts.make_shortcut(
#         name=name,
#         script=target_path,
#         working_dir=target_parent_folder,
#         folder=shortcut_path,
#         description=description,
#         executable=target_path,
#     )


def get_latest_file_in_directory_from_all_filenames_that_are_real_numbers(
    path: str,
) -> Union[str, None]:
    """
    Finds the latest file in a directory where the filename is a real number.

    The function assumes filenames that are valid integers represent file versions or sequence numbers.

    Args:
        path (str): The path to the directory.

    Returns:
        Union[str, None]: The name of the latest file (with the highest integer value in its name)
                          or None if no such file is found.
    """
    files = os.listdir(path)
    max_num = -1
    latest_file = None

    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            filename, file_extension = os.path.splitext(file)
            try:
                file_number = int(filename)
                if file_number > max_num:
                    max_num = file_number
                    latest_file = file
            except ValueError:
                continue

    return latest_file


def is_directory_empty(directory_path: str) -> bool:
    """
    Checks if a directory is empty.

    Args:
        directory_path (str): The path to the directory.

    Returns:
        bool: True if the directory is empty, False otherwise.
    """
    return not os.listdir(directory_path)


def get_filesize(file_path: str) -> int:
    """
    Gets the size of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        int: The size of the file in bytes.
    """
    return os.path.getsize(file_path)


def get_file_size_of_directory(
    directory: str, blacklisted_file_extensions: list = [], chunk_size: int = 4096
) -> int:
    """
    Calculates the total size of files in a directory, excluding those with blacklisted extensions.

    Args:
        directory (str): The path to the directory.
        blacklisted_file_extensions (list, optional): A list of file extensions to exclude from size calculation.
        chunk_size (int, optional): The chunk size to round file sizes to.

    Returns:
        int: The total size of the files in the directory, rounded to the nearest chunk size.
    """
    total_size = 0

    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            if any(f.endswith(ext) for ext in blacklisted_file_extensions):
                continue

            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                file_size = os.path.getsize(fp)
                rounded_size = math.ceil(file_size / chunk_size) * chunk_size
                total_size += rounded_size

    return total_size


def generate_uuid_from_directory(directory, blacklisted_extensions: list = []):
    """Generate a UUID based on the content of all files in a directory, excluding files with specified extensions.

    Args:
        directory (str): Path to the directory to scan.
        blacklisted_extensions (list, optional): List of file extensions to exclude from hashing. Defaults to an empty list.

    Returns:
        UUID: A UUID generated from the MD5 hash of the file contents."""
    hash_md5 = hashlib.md5()

    for root, _, files in os.walk(directory):
        for file in sorted(files):  
            blacklisted = True
            for ext in blacklisted_extensions:
                if file.endswith(ext):
                    break
            else:
                blacklisted = False
            if blacklisted:
                continue
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path): 
                with open(file_path, "rb") as f:
                    for chunk in iter(lambda: f.read(4096), b""):
                        hash_md5.update(chunk)

    unique_hash = hash_md5.hexdigest()
    unique_uuid = uuid.UUID(unique_hash[:32])

    return unique_uuid


if SYSTEM_NAME == "windows":

    def add_to_path_to_system_path_variables(path):
        """
        Adds a new path to the system PATH environment variable on Windows.

        Args:
            path (str): The path to add to the system PATH.

        Note:
            Uses the `setx` command to update the PATH environment variable permanently.
        """
        current_path = os.getenv("PATH")
        new_path = f"{current_path};{path}"
        os.system(f'setx PATH "{new_path}"')

elif SYSTEM_NAME == "darwin":
    import subprocess

    def add_to_path_to_system_path_variables(path):
        """
        Adds a new path to the system PATH environment variable on macOS (Darwin).

        Args:
            path (str): The path to add to the system PATH.

        Notes:
            Appends the path to the `~/.bash_profile` file and reloads it using the `source` command.
        """
        with open(os.path.expanduser("~/.bash_profile"), "a") as file:
            file.write(f'\nexport PATH="{path}:$PATH"\n')
        subprocess.run(["source", "~/.bash_profile"], shell=True, check=True)

elif SYSTEM_NAME == "linux":
    import subprocess

    def add_to_path_to_system_path_variables(path):
        """
        Adds a new path to the system PATH environment variable on Linux.

        Args:
            path (str): The path to add to the system PATH.

        Notes:
            Appends the path to the `~/.bashrc` file and reloads it using the `source` command.
        """
        with open(os.path.expanduser("~/.bashrc"), "a") as file:
            file.write(f'\nexport PATH="{path}:$PATH"\n')
        subprocess.run(["source", "~/.bashrc"], shell=True, check=True)

else:

    def add_to_path_to_system_path_variables(path):
        """
        Raises an exception for unknown system types.

        Args:
            path (str): The path to add to the system PATH (not used).

        Raises:
            BaseException: If the system type is unknown.
        """
        raise BaseException("Unknown System")


class _compress_directory_list_trie_node:
    def __init__(self):
        "Node in a Trie data structure with a dictionary of child nodes and a boolean flag to mark the end of a path."
        self.children = defaultdict(_compress_directory_list_trie_node)
        self.is_end_of_path = False


def _compress_directory_list_insert_path(
    root: _compress_directory_list_trie_node, path: Iterable
) -> None:
    "Insert a path into a Trie data structure."
    node = root
    for part in path:
        node = node.children[part]
    node.is_end_of_path = True


def _compress_directory_list_build_trie(
    paths: Iterable,
) -> _compress_directory_list_trie_node:
    "Build a Trie from a list of file paths."
    root = _compress_directory_list_trie_node()
    for path in paths:
        _compress_directory_list_insert_path(root, path.split("/"))
    return root


def _compress_directory_list_serialize_trie(
    node: _compress_directory_list_trie_node,
) -> dict:
    "Serialize a Trie into a compressed dictionary format representing a directory structure."
    if not node.children:
        return []

    if len(node.children) == 1 and node.is_end_of_path == False:
        key, child = next(iter(node.children.items()))
        serialized_child = _compress_directory_list_serialize_trie(child)
        if isinstance(serialized_child, list) and not serialized_child:
            return key
        if isinstance(serialized_child, str):
            return f"{key}/{serialized_child}"
        return {key: serialized_child}

    result = {}
    for key, child in node.children.items():
        serialized_child = _compress_directory_list_serialize_trie(child)
        if isinstance(serialized_child, list) and not serialized_child:
            result.setdefault("files", []).append(key)
        else:
            result[key] = serialized_child

    return result


def compress_directory_list(paths: Iterable) -> "dict[Union[list,str]]":
    "Compress a list of file paths into a dictionary format representing the directory structure."
    trie = _compress_directory_list_build_trie(paths)
    compressed = _compress_directory_list_serialize_trie(trie)
    return compressed


def find_files_with_extension(root_dir: str, file_extension: str) -> List[str]:
    """
    Returns a list of all file directories with the specified extension.

    :param root_dir: The root directory to start searching from.
    :param file_extension: The file extension to search for (e.g., '.txt').
    :return: A list of file paths with the specified extension.
    """
    file_paths = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(file_extension):
                file_paths.append(os.path.join(root, file))
    return file_paths


def find_files_with_extensions(root_dir: str, file_extensions: List[str]) -> List[str]:
    """
    Returns a list of all file directories with the specified extensions.

    :param root_dir: The root directory to start searching from.
    :param file_extensions: The file extensions to search.
    :return: A list of file paths with the specified extension.
    """
    files = []
    for file_extension in file_extensions:
        files.extend(find_files_with_extension(root_dir, file_extension))
    return files
