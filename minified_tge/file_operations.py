_C='utf-8'
_B=True
_A=False
import os,shutil
from filecmp import dircmp as file_dircmp,cmp as file_cmp
from ast import parse as ast_parse,walk as ast_walk,FunctionDef as ast_FunctionDef
import zipfile
from pathlib import Path as pathlib_path
from typing import List,Union,Tuple,Any
import tkinter as tk,pyshortcuts
from.codec import decode,b64decode,b64encode
def create_missing_directory(directory):
	'\n    Creates a directory at the given path if it does not already exist.\n\n    Args:\n        directory (str): The path of the directory to create.\n\n    Returns:\n        Boolean: True if the directory was created, False if it already existed.\n\n    If the directory already exists, this function does not modify it and does not raise any exceptions.\n    ';A=directory
	if not os.path.exists(A):os.makedirs(A);return _B
	else:return _A
def delete_directory(directory):
	'\n    Deletes a directory and its contents.\n\n    Args:\n        directory (str): The name of the directory to delete.\n\n    Returns:\n        Tuple[bool, str]: A tuple with two items: a boolean indicating whether\n        the directory was successfully deleted, and a string with a message\n        indicating the result of the operation.\n    '
	try:
		B=pathlib_path(__file__).resolve().parent;A=os.path.join(B,directory)
		if os.path.exists(A):shutil.rmtree(A);return _B,'Directory deleted'
		else:return _A,'Directory not found'
	except:return _A,'Error deleting directory'
def write_save_data(name,dir,data):
	'\n    Saves data to a file with the given name in the specified directory.\n\n    :param name: The name of the file to be saved, without the ".save" extension.\n    :param dir: The directory where the file should be saved.\n    :param data: The data to be written to the file.\n    :return: A tuple (success, message) where success is True if the file was saved\n             successfully and False otherwise, and message is a string with a status\n             message or an error message if an exception occurred.\n    ';A=name
	try:
		A=A.replace('.save','');B=os.path.join(dir,f"{A}.save")
		with open(B,'w')as C:C.write(data);return _B,'File saved'
	except Exception as D:return _A,f"Error saving file: {str(D)}"
def load_save_data(name,dir):
	'\n    Loads a file and returns the data.\n\n    Args:\n        name (str): The name of the .save file to load.\n        dir (str): The directory containing the file to load.\n\n    Returns:\n        tuple: A tuple containing a boolean indicating success and the decoded data.\n            The boolean is True if the file was loaded and decoded successfully, and False\n            otherwise. The decoded data is returned as bytes if decoding was successful,\n            or a string containing an error message if decoding was not successful.\n    ';A=name
	try:
		A=A.rstrip('.save','');B=os.path.join(dir,f"{A}.save")
		if os.path.exists(B):
			with open(B,'rb')as D:
				E=D.read();F,C=decode(E)
				if F:return _B,C
				else:return _A,C
		else:return _A,'File not found'
	except Exception as G:return _A,f"Error loading file: {str(G)}"
def move_file(source_path,destination_path):
	"\n    Move a file from the source path to the destination path.\n\n    This function checks if the file exists at the given source path and verifies its presence.\n    If the file exists, it creates any missing directories in the destination path and then\n    performs the file move using the `shutil.move` function. Returns True if the move is successful,\n    and False if the source file does not exist.\n\n    Args:\n        source_path (str): The path to the source file.\n        destination_path (str): The desired path for the moved file.\n\n    Returns:\n        bool: True if the file is successfully moved, False if the source file doesn't exist.\n\n    Example:\n        >>> move_file('source_folder/file.txt', 'destination_folder/file.txt')\n        True\n    ";B=destination_path;A=source_path
	if doesDirectoryFileExist(A):create_missing_directory(B);shutil.move(A,B);return _B
	else:return _A
def copy_file(source_path,destination_path):
	'\n    Copies a file from the source path to the destination path.\n\n    Args:\n        source_path (str): The path to the source file.\n        destination_path (str): The path where the file will be copied.\n\n    Returns:\n        bool: True if the file was successfully copied, False otherwise.\n    ';B=destination_path;A=source_path
	try:
		if doesDirectoryFileExist(A):create_missing_directory(B);shutil.copy(A,B);return _B
		else:return _A
	except:return _A
def rename_file(source_path,name):
	'\n    Renames a file located at the given source path with the specified name.\n\n    Args:\n        source_path (str): The current path of the file to be renamed.\n        name (str): The new name to be assigned to the file.\n\n    Returns:\n        bool: True if the file is successfully renamed, False otherwise.\n    ';A=source_path
	try:
		if doesDirectoryFileExist(A):B=os.path.dirname(A);C=os.path.join(B,name);os.rename(A,C);return _B
		else:return _A
	except:return _A
def copy_directory(source_path,destination_path):
	"\n    Copy the contents of a source directory to a destination directory.\n\n    This function attempts to copy all files and subdirectories from the source directory\n    to the destination directory. If the source directory exists and the copy operation is successful,\n    the function returns True. If the source directory doesn't exist or an error occurs during the copy,\n    the function returns False.\n\n    Args:\n        source_path (str): The path to the source directory to be copied.\n        destination_path (str): The path to the destination directory where contents will be copied.\n\n    Returns:\n        bool: True if the copy operation is successful, False otherwise.\n    ";B=destination_path;A=source_path
	try:
		if doesDirectoryFileExist(A):create_missing_directory(B);shutil.copytree(A,B);return _B
		else:return _A
	except:return _A
def move_directory(source_path,destination_path):
	'\n    Move a directory or file from the source path to the destination path.\n\n    This function attempts to move the directory or file located at the source path\n    to the specified destination path. If the source path points to an existing\n    directory or file, the function creates any missing directories in the destination\n    path and performs the move operation.\n\n    Args:\n        source_path (str): The path to the source directory or file.\n        destination_path (str): The desired path for the moved directory or file.\n\n    Returns:\n        bool: True if the move operation is successful, False otherwise.\n\n    Example:\n        source_path = \'/path/to/source_directory\'\n        destination_path = \'/path/to/destination_directory\'\n        if move_directory(source_path, destination_path):\n            print("Move successful!")\n        else:\n            print("Move failed or encountered an error.")\n    ';B=destination_path;A=source_path
	try:
		if doesDirectoryFileExist(A):create_missing_directory(B);shutil.move(A,B);return _B
		else:return _A
	except:return _A
def rename_directory(source_path,name):
	"\n    Renames a directory at the given source path with the new provided name.\n\n    This function attempts to rename the specified directory by changing its name\n    to the provided new name while maintaining its location. The function first\n    checks if the directory exists using the 'doesDirectoryFileExist' function.\n    If the directory exists, it is renamed by updating its path accordingly.\n    \n    Args:\n        source_path (str): The current path of the directory to be renamed.\n        name (str): The new name to be assigned to the directory.\n\n    Returns:\n        bool: True if the directory was successfully renamed, False otherwise.\n    ";A=source_path
	try:
		if doesDirectoryFileExist(A):B=os.path.dirname(A);C=os.path.join(B,name);os.rename(A,C);return _B
		else:return _A
	except:return _A
def get_parent_path(path):'\n    Returns the parent directory of a given path.\n    param path: A string representing a path.\n    type path: str\n    return: A string representing the parent directory of the given path.\n    rtype: str\n    ';return os.path.dirname(path)
def get_parent_folder(path):
	'\n    Get the parent folder name from the given path.\n\n    This function takes a path as input and returns the name of the parent folder.\n    \n    Args:\n        path (str): A string representing the path to a file or directory.\n\n    Returns:\n        str: The name of the parent folder extracted from the path.\n\n    Note:\n        - The path can use either forward slashes (\'/\') or backslashes (\'\\\') as separators.\n        - If the given path points to a directory, the name of the last folder in the path is returned.\n        - If the given path points to a file, the name of the second-to-last folder in the path is returned.\n          (This is assuming the file is located inside a folder within the path.)\n\n    Examples:\n        >>> get_parent_folder("C:\\Users\\Username\\Documents\\file.txt")\n        \'Documents\'\n        >>> get_parent_folder("/home/user/pictures/image.jpg")\n        \'user\'\n    ';A='/';B=path.replace('\\',A)
	if os.path.isdir(path):return B.split(A)[-1]
	else:C=B.split(A)[-2];return C
def combine_files(directory,output_directory,name):
	'\n    Combines multiple files from a directory into a single encrypted file.\n\n    Args:\n        directory (str): The directory path containing the files to be combined.\n        output_directory (str): The directory path where the combined file will be saved.\n        name (str): The name of the combined file (without extension).\n\n    Returns:\n        bool: True if the files are successfully combined and saved as an encrypted file,\n              False if an error occurs during the process.\n\n    Raises:\n        Any exceptions raised during the execution will be caught and cause the function to return False.\n    ';D=directory
	try:
		E=[]
		for A in os.listdir(D):
			F=os.path.join(D,A)
			if os.path.isfile(F):
				with open(F,'rb')as B:C=B.read();E.append((A,C))
		G=b''
		for(A,C)in E:G+=A.encode()+b':'+C+b'|'
		H=b64encode(G);I=os.path.join(output_directory,name+'.encrypted')
		with open(I,'wb')as B:B.write(H)
		return _B
	except:return _A
def split_file(directory,output_directory):
	'\n    Splits a combined encrypted file into individual files and saves them to the output directory.\n\n    Args:\n        directory (str): The path of the combined encrypted file.\n        output_directory (str): The directory path where the individual files will be saved.\n\n    Returns:\n        bool: True if the combined file is successfully split into individual files and saved,\n              False if an error occurs during the process.\n\n    Raises:\n        Any exceptions raised during the execution will be caught and cause the function to return False.\n    '
	try:
		with open(directory,'rb')as A:B=A.read()
		C=b64decode(B);D=C.split(b'|')[:-1]
		for E in D:
			F,G=E.split(b':',1);H=os.path.join(output_directory,F.decode())
			with open(H,'wb')as A:A.write(G)
		return _B
	except:return _A
def doesDirectoryFileExist(is_file,directory):
	'\n    Check if a file or directory exists in the given path.\n\n    Args:\n        is_file (bool): True if checking for a file, False if checking for a directory.\n        directory (str): The path to the file or directory.\n\n    Returns:\n        bool: True if the file or directory exists, False otherwise.\n    ';A=directory
	if is_file:
		if os.path.isfile(f"{pathlib_path(__file__).resolve().parent}/{A}")or os.path.isfile(A):return _B
		else:return _A
	elif os.path.exists(f"{pathlib_path(__file__).resolve().parent}/{A}")or os.path.exists(A):return _B
	else:return _A
def doesFileExist(directory):'\n    Check if a file exists at the specified directory.\n\n    Parameters:\n    directory (str): The path to the directory or file to check.\n\n    Returns:\n    bool: True if the file exists and is a regular file, False otherwise.\n    ';A=directory;return os.path.exists(A)and os.path.isfile(A)
def doesDirectoryExist(directory):'\n    Check if the specified directory exists and is a valid directory.\n\n    Parameters:\n    directory (str): The path to the directory to be checked.\n\n    Returns:\n    bool: True if the directory exists and is a valid directory, False otherwise.\n    ';A=directory;return os.path.exists(A)and os.path.isdir(A)
def delete_file(name,dir):
	'\n    Deletes a file from a directory.\n\n    Args:\n        name (str): The name of the file to delete.\n        dir (str): The name of the directory where the file is located.\n\n    Returns:\n        bool: True if the file was deleted, False otherwise.\n    '
	if os.path.isfile(f"{pathlib_path(__file__).resolve().parent}/{dir}/{name}"):os.system(f"rm {f'{pathlib_path(__file__).resolve().parent}/{dir}/{name}'}");return _B
	else:return _A
def compare_file(directory1,directory2):
	'\n    Compares the contents of two files and returns True if they are identical, False otherwise.\n\n    Args:\n        directory1 (str): The path to the first file.\n        directory2 (str): The path to the second file.\n\n    Returns:\n        bool: True if the contents of the files are identical, False otherwise.\n\n    Raises:\n        Any exception raised while opening or reading the files will be caught and the function will return False.\n\n    '
	try:
		with open(directory1,'r')as A,open(directory2,'r')as B:return A.read()==B.read(),_B
	except:return _A,_A
def compare_directory(directory1,directory2):
	'\n    Recursively compares the files in two directories and their subdirectories.\n\n    Args:\n        directory1 (str): The path to the first directory.\n        directory2 (str): The path to the second directory.\n\n    Returns:\n        Union[bool, str]: \n        - If the directories are the same, returns True and a success message.\n        - If the directories are different, returns False and an error message.\n    ';B=directory2;A=directory1
	try:
		C=file_dircmp(A,B)
		for D in C.common_files:
			F=os.path.join(A,D);G=os.path.join(B,D)
			if not file_cmp(F,G):return _A
		for E in C.subdirs.values():
			if not compare_directory(os.path.join(A,E.left),os.path.join(B,E.right)):return _A
		return _B,'Files are compared successfully'
	except OSError as H:return _A,'Error: '+str(H)
def count_items_in_directory(directory_path):'\n    Counts the number of items (files and directories) in the specified directory.\n\n    Args:\n        directory_path (str): The path of the directory.\n\n    Returns:\n        int: The total count of items in the directory.\n    ';return len(os.listdir(directory_path))
def get_current_working_directory():
	'\n    Retrieve the current working directory path.\n\n    Attempts to fetch the absolute path of the current working directory using the `os.getcwd()` function.\n    \n    Returns:\n        str: The absolute path of the current working directory.\n             Returns an empty string if an exception occurs during the retrieval process.\n    '
	try:return os.getcwd()
	except:return''
def get_file_extension(file_path):'\n    Return the file extension from a given file path.\n\n    :param file_path: A string representing the file path.\n    :type file_path: str\n    :return: A string representing the file extension.\n    :rtype: str\n    ';return os.path.splitext(file_path)[1][1:]
def find_files_by_extension(directory_path,extension):
	'\n    Retrieve a list of file names within the given directory that match the specified extension.\n\n    Args:\n        directory_path (str): The path to the directory where files will be searched.\n        extension (str): The target file extension to filter files by.\n\n    Returns:\n        list: A list of file names that have the specified extension within the directory.\n    ';A=[]
	for B in os.listdir(directory_path):
		D,C=os.path.splitext(B)
		if C==extension:A.append(B)
	return A
def get_file_size(file_path):
	"\n    Get the size of a file located at the specified 'file_path'.\n\n    This function checks if the provided path points to a valid file on the system.\n    If the file exists, its size in bytes is returned; otherwise, 0 is returned.\n\n    Args:\n        file_path (str): The path to the file for which the size is to be determined.\n\n    Returns:\n        int: The size of the file in bytes if it exists, or 0 if the file doesn't exist.\n    ";A=file_path
	if os.path.isfile(A):return os.path.getsize(A)
	else:return 0
def get_file_creation_time(file_path):
	'\n    Retrieve the creation time of a file.\n\n    This function takes a file path as input and returns the creation time\n    of the file as a formatted string. If the provided path does not point\n    to a valid file, an empty string is returned.\n\n    Args:\n        file_path (str): The path to the file.\n\n    Returns:\n        str: A formatted string representing the creation time of the file,\n        or an empty string if the file does not exist.\n    ';A=file_path
	if os.path.isfile(A):return os.path.getctime(A)
	else:return''
def count_functions_in_file(file_path):
	'\n    Count and retrieve the names of top-level functions defined in the specified Python file.\n\n    This function reads the content of the given Python file, parses its abstract syntax tree (AST),\n    and identifies all top-level functions. It then returns the count of functions and a list of their names.\n\n    Args:\n        file_path (str): The path to the Python file to be analyzed.\n\n    Returns:\n        Tuple[int, list]: A tuple containing two elements:\n            - The total number of top-level functions found in the file.\n            - A list containing the names of the identified functions.\n\n        If an error occurs during file reading or parsing, the function returns (0, []).\n    '
	try:
		with open(file_path,'r',encoding=_C)as B:C=ast_parse(B.read());A=[A.name for A in ast_walk(C)if isinstance(A,ast_FunctionDef)];return len(A),A
	except:return 0,[]
def count_functions_in_directory(directory_path):
	"\n    Counts the number of functions in all Python files within a directory and its subdirectories.\n    Returns a dictionary where the keys are the file paths and the values are tuples with the count and names of functions.\n    Also returns the total count of functions across all files.\n\n    Args:\n        directory_path (str): The path to the directory.\n\n    Returns:\n        tuple: A tuple containing the dictionary with file paths and function details, and the total count of functions.\n\n    Raises:\n        NotADirectoryError: If the specified directory path does not exist or is not a directory.\n        IOError: If there was an error while reading any of the files.\n\n    Example:\n        >>> count_functions_in_directory('my_directory')\n        (\n            4,\n            {\n                'my_directory/file1.py': (3, ['function1', 'function2', 'function3']),\n                'my_directory/subdirectory/file2.py': (1, ['function4'])\n            },\n        )\n    ";D={};E=0;F=[]
	for(G,J,H)in os.walk(directory_path):
		for A in H:
			if A.endswith('.py'):
				B=os.path.join(G,A)
				try:
					with open(B,'r',encoding=_C)as A:I=ast_parse(A.read());C=[A.name for A in ast_walk(I)if isinstance(A,ast_FunctionDef)];D[B]=len(C),C;E+=len(C)
				except IOError:F.append(B)
	return E,D,F
def count_function_names_in_directory(directory_path):
	"\n    Count the total number of function names in Python files within the specified directory.\n\n    This function recursively searches through all the Python files in the given directory\n    and its subdirectories, tallying the total number of function names encountered. It returns\n    a tuple containing the total count of function names and a list of unique function names.\n\n    Args:\n        directory_path (str): The path to the directory to be searched for Python files.\n\n    Returns:\n        Tuple[int, list]: A tuple containing the total count of function names and a list of\n        unique function names extracted from the Python files.\n\n    Note:\n        This function depends on the 'count_functions_in_directory' utility function to perform\n        the actual counting of function occurrences in the directory's Python files.\n    ";E,B,F=count_functions_in_directory(directory_path);A=[]
	for(G,(H,C))in B.items():
		for D in C:A.append(D)
	return len(A),A
def save_counted_function_names_from_directory(directory_path,file_name,output_path,create_missing_directory_bool):
	"\n    Count the occurrences of function names in the Python files within the specified directory and save them to a file.\n\n    Args:\n        directory_path (str): The path to the directory containing Python files for function name counting.\n        file_name (str): The name of the output file where the counted function names will be saved.\n        output_path (str): The directory path where the output file will be saved.\n        create_missing_directory_bool (bool): A flag indicating whether to create the output directory if it's missing.\n\n    Returns:\n        bool: True if the function names were successfully counted and saved, False otherwise.\n    ";C=file_name;B=output_path;A=directory_path;D=count_function_names_in_directory(A)[1]
	if A=='':A=get_current_working_directory()
	if B=='':B=A
	if C=='':C='functions.txt'
	if create_missing_directory_bool:create_missing_directory(B)
	try:
		with open(B+C,'w',encoding=_C)as E:
			for F in D:E.write(F+'\n')
		return _B
	except:return _A
def input_file_path(extension=None):'\n    Prompts the user to select a file path for saving a file.\n\n    This function opens a file dialog that allows the user to specify a file path\n    for saving a file. The \'extension\' parameter can be used to suggest a default\n    file extension for the saved file.\n\n    Parameters:\n        extension (str, optional): A suggested file extension for the saved file.\n            If provided, the file dialog will include this extension in the suggested\n            file name and in the file type dropdown filter. Defaults to None.\n\n    Returns:\n        str: The selected file path for saving the file, including the chosen file name\n        and extension.\n\n    Note:\n        This function requires the \'tkinter.filedialog\' module to be imported in\n        order to work properly.\n\n    Example:\n        >>> input_file_path(extension=".txt")\n        \'/path/to/save/file.txt\'\n    ';return tk.filedialog.asksaveasfilename(defaultextension=extension)
def input_directory_path():"\n    Prompt user to select a directory using a file dialog.\n\n    This function opens a file dialog window that allows the user to choose a directory.\n    The selected directory's path is returned as a string.\n\n    Returns:\n        str: The path of the selected directory.\n    ";A=tk.filedialog.askdirectory();return A
def unzip_file(zip_path,extract_dir,create_missing_directory_bool=_A):
	'\n    Unzips a zip file to the specified extract directory.\n    \n    Args:\n        zip_path (str): pathlib_path to the zip file.\n        extract_dir (str): Directory to extract the contents of the zip file to.\n    ';C=create_missing_directory_bool;B=zip_path;A=extract_dir
	if B=='':return _A,_A
	if A=='':return _A,_A
	try:
		if C:D=create_missing_directory(A)
		with zipfile.ZipFile(B,'r')as E:E.extractall(A)
		return _B,_B
	except:
		if C:
			if D:delete_directory(A)
		return _A,_B
def zip_directory(directory_path,output_path,create_missing_directory_bool=_A):
	'\n    Zip a given directory and save the resulting zip file to the output path.\n\n    Args:\n        directory_path (str): pathlib_path to the directory to be zipped.\n        output_path (str): pathlib_path to save the resulting zip file.\n\n    Returns:\n        None\n    ';E='.zip';B=directory_path;A=output_path
	if B=='':return _A,_A
	if A=='':return _A,_A
	if not A.endswith(E):A+=E
	try:
		if create_missing_directory_bool:create_missing_directory(A)
		with C.ZipFile(A,'w',C.ZIP_DEFLATED)as C:
			for(F,I,G)in os.walk(B):
				for H in G:D=os.path.join(F,H);C.write(D,os.path.relpath(D,B))
		return _B,_B
	except:return _A,_B
def get_appdata_path():"\n    Retrieve the path to the 'AppData' directory of the current user.\n\n    Returns:\n        str: The expanded and absolute path to the 'AppData' directory.\n    ";return os.path.expanduser('~\\AppData')
def create_shortcut(name,target_path,shortcut_path,description=''):'\n    Creates a shortcut to a target file or script.\n\n    This function generates a shortcut (or symbolic link) to a specified target file or script\n    at the specified shortcut path location. Additional properties like the working directory,\n    description, and execution settings can be customized for the shortcut.\n\n    Args:\n        name (str): The name of the shortcut (without the file extension).\n        target_path (str): The path to the target file or script that the shortcut points to.\n        shortcut_path (str): The path where the shortcut should be created.\n        description (str, optional): An optional description for the shortcut (default is "").\n\n    Returns:\n        None\n\n    Note:\n        - The \'pyshortcuts\' library is used to create the shortcut. Make sure it is installed.\n        - The \'executable\' parameter is set to \'target_path\', indicating the executable to run\n        when the shortcut is activated.\n\n    Example:\n        create_shortcut("MyScriptShortcut", "/path/to/myscript.py", "/desktop/shortcuts/",\n                        "Shortcut to run my custom script.")\n    ';A=target_path;B=os.path.dirname(A);pyshortcuts.make_shortcut(name=name,script=A,working_dir=B,folder=shortcut_path,description=description,executable=A)
def get_latest_file_in_directory_from_all_filenames_that_are_real_numbers(path):
	E=os.listdir(path);C=-1;A=None
	for B in E:
		if os.path.isfile(os.path.join(path,B)):
			F,G=os.path.splitext(B)
			try:
				D=int(F)
				if D>C:C=D;A=B
			except ValueError:continue
	if A is not None:return A
	else:return