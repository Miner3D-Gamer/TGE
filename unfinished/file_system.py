import os
import time
from tge.tbe import ArgumentHandler
# import re


# import sys

# def restart_program():
#     python = sys.executable
#     os.execl(python, python, *sys.argv)


# string = re.compile("& *python.exe *.py")

current_working_directory = os.getcwd()

# print(current_working_directory)
home_directory = current_working_directory
default_offset_directory = ""
default_drive_letter = "C"


def lchop(string: str, substring: str) -> str:
    if string.startswith(substring):
        return string[len(substring) :]
    else:
        return string


def rchop(string: str, substring: str) -> str:
    if string.endswith(substring):

        return string[: -len(substring)]
    else:
        return string


class SimDirFilSystem:  # Simple Directory File System
    def __init__(
        self,
        home_directory: str,
        current_drive_letter: str | None = None,
        current_offset_directory: str = "",
    ):
        if current_drive_letter is None:
            current_drive_letter = default_drive_letter

        self.home_directory = home_directory
        self.current_offset_directory = current_offset_directory
        self.current_drive_letter = current_drive_letter

        self.current_command = ""
        self.quit_notations = ["quit", "leave", "exit", "bye", "q"]
        self.commands = {
            "change_directory": {
                "cmd": ["cd", "chdir", "change_directory"],
                "description": "Displays the name of or changes the current directory.",
                "help": "Displays the name of or changes the current directory.\n\nTo use this command you must specify one parameter as the path you to to append/change to.",
                "function": self.change_directory,
            },
            "get_directory_items": {
                "cmd": ["dir", "get_directory_items", "ls"],
                "description": "",
                "help": "",
                "function":self.get_directory_items
            },
            "make_directory": {
                "cmd": [
                    "make_directory",
                    "md",
                    "mkdir",
                    "create_directory",
                    "crdir",
                    "crd",
                ],
                "description": "Creates a directory.",
                "help": "Create a directory with a given parameter.\n\nYou cannot create multiple directories like this: \n\tmkdir \\a\\b\\c\\d\n\nRather, you would need to use: \n\tmkdir a\n\tchdir a\n\tmkdir b\n\tchdir b\n\tmk c\n\tchdir c \n\tmkdir d",
                "function":self.make_directory
            },
            "help": {
                "cmd": ["help"],
                "description": "Provides information for commands.",
                "help": "Provides information for commands.\n\nUse 'help [command]' to see more information about that command",
                "function":self.help
            },
            "remove_directory": {"cmd": ["rm", "rmdir"], "description": "", "help": "", "function":self.remove_directory},
            "rename_file": {
                "cmd": ["rename", "ren", "rename_file", "rn"],
                "description": "Renames a file.",
                "help": "",
                "function":self.rename_file
            },
            "create_file": {
                "cmd": ["crf", "create_file", "crfile", "mkf", "mkfile", "make_file"],
                "description": "",
                "help": "",
                "function":self.create_file
            },
            "remove_file": {
                "cmd": ["rmf", "rmfile", "remove_file"],
                "description": "",
                "help": "",
                "function":self.remove_file
            }
        }
        self.current_directory = home_directory
        self.last = {"type":"empty"}
        self.current_command_parameters_bool = None
        self.input = ""
        self.invalid_file_name_characters = ["/", "\\", ":", "*", "?", '"', "<", ">", "|"]
        # self.command_indexing_time = 0

    def ask_for_command(self):
        """
        Ask/Receive a command from the user.

        sets self.current_command to the first part of the input of the user if the command the user included a space inside the command
        if a space is found the command will automatically be split into the main command and parameters
        """
        self.input = input(
            f"{self.current_drive_letter}:{self.current_offset_directory}>"
        ).lstrip()
        if self.input.find(" ") != -1:
            self.input = self.input.split(" ", 1)
            self.current_command = self.input[0].strip().lower()

            if self.input.__len__() > 1:
                self.current_command_parameters = self.input[1].strip()
                self.current_command_parameters_bool = True
            else:
                self.current_command_parameters_bool = False
        else:
            self.current_command = self.input.strip().lower()
            self.current_command_parameters_bool = False

        # print(self.input)
        # for i in self.quit_notations:
        #     print(self.current_command, i, self.current_command == i)
        if (
            self.current_command in self.quit_notations
            or self.current_command.startswith("&")
        ):
            quit()

    def execute(self):
        start_search = time.time()
        for command in self.commands:
            if self.current_command in self.commands[command]["cmd"]:
                self.commands[command]["function"]()
                break

        # else:
        #     if self.input:
        #         self.last = self.input
        #     else:
        #         pass

    def change_directory(self):
        """
        Change or append the current directory
        """
        if not self.current_command_parameters_bool:
            print(
                f">> To use '{self.current_command}' you need to specify one parameter."
            )
            return
        self.current_command_parameters = self.current_command_parameters.replace(
            "/", "\\"
        )
        # print(f"{self.home_directory}/{lchop(self.current_command_parameters, '/')}")
        new_path = "\\" + lchop(self.current_command_parameters, "\\")
        # print(f"{self.home_directory}{self.current_offset_directory}{new_path}")

        first_dir = f"{self.home_directory}{new_path}"
        second_dir = f"{self.home_directory}{self.current_offset_directory}{new_path}"
        if os.path.isfile(first_dir) or os.path.isfile(second_dir):
            print(
                ">> File path invalid, full path required. I'll update to do this automatically later."
            )
            return

        if os.path.exists(
            f"{self.home_directory}{new_path}"
        ):  # Check if C:/{new_path} is what the user is trying to change to
            self.current_offset_directory = new_path
            self.current_directory = self.home_directory + new_path
        elif os.path.exists(
            f"{self.home_directory}{self.current_offset_directory}{new_path}"
        ):  # Check if user wants to append {new_path} to current directory
            self.current_offset_directory += new_path
            self.current_directory = (
                self.home_directory + self.current_offset_directory + new_path
            )
        else:
            print(
                f">> Directory invalid: {self.current_drive_letter}:{self.current_offset_directory}{new_path}"
            )

    def get_directory_items(self):
        """
        Save all folders and files in current directory to self.last
        """
        folders_in_this_dir = []
        files_in_this_dir = []
        for root, folders, files in os.walk(self.current_directory):
            if not root == self.current_directory:
                continue
            folders_in_this_dir = folders
            files_in_this_dir = files
            if folders:
                print("Folders:")
                for folder in folders:
                    print("\t%s"%folder)
            if files:
                print("Files:")
                for file in files:
                    print("\t%s"%file)
        
        self.last = {"type":"folders&files", "folders":folders_in_this_dir, "files":files_in_this_dir}

    def make_directory(self):
        if not self.current_command_parameters_bool:
            print(
                f">> To use '{self.current_command}' you need to specify one parameter."
            )
            return

        self.current_command_parameters = self.current_command_parameters.replace(
            "/", "\\"
        )

        new_path = "\\" + lchop(self.current_command_parameters, "\\")
        print(new_path)
        print(new_path[2:2])
        if new_path[2:2] == ":":
            print("ss")

        # first_dir = f"{self.home_directory}{new_path}"
        # second_dir = f"{self.home_directory}{self.current_offset_directory}{new_path}"

        print(
            f">> Creating directory {self.current_drive_letter}:{self.current_offset_directory}{new_path}"
        )

        try:
            os.mkdir(f"{self.home_directory}{self.current_offset_directory}{new_path}")
        except FileExistsError:
            print(
                f">> Directory '{self.current_drive_letter}:{self.current_offset_directory}{new_path}' already exists."
            )
        except FileNotFoundError:
            print(
                f">> Parent Directories for Child directories must be created manually. This may also occur if the directory character limit which is by default 256. Error on directory: '{self.current_drive_letter}:{self.current_offset_directory}{new_path}'. I will update this to create parent directories automatically later."
            )
        except NotADirectoryError or OSError:
            print(f">> Invalid Directory name: '{new_path}'")

    def help(self):
        if not self.current_command_parameters_bool:
            for i in self.commands:
                description = self.commands[i]["description"]
                if description == "":
                    description = "No description available."
                print(f"{i}: {description}")
                for j in self.commands[i]["cmd"]:
                    print(f"\t{j}")
            return

        # print(self.current_command_parameters)
        for i in self.commands:
            if self.current_command_parameters in self.commands[i]["cmd"]:
                current_command = i
                break
        else:
            print(f">> Unknown command '{self.current_command_parameters}'")
            return

        command_help = self.commands[i]["help"]
        if command_help == "":
            command_help = "No description available."
        command_help = ">> " + command_help.replace("\n", "\n>> ")
        print(f"{command_help}")
        print(f">>\n>> Command shortcuts:")
        for i in self.commands[current_command]["cmd"]:
            print(f">> \t{i}")

            # print("hi")

    def rename_file(self):
        if (
            not self.current_command_parameters_bool
        ):  # or self.current_command_parameters.find(" ") > -1
            print(
                f">> To use '{self.current_command}' you need to specify one parameter."
            )
            return

        try:
            path, name = self.current_command_parameters.split(">")
        except ValueError:
            print(f"Both a file path and new name must be specified and split by a '>'")
            return

        if os.path.isfile(
            f"{self.home_directory}{self.current_offset_directory}{path}"
        ):
            in_cd = True
        elif os.path.isfile(path):
            in_cd = False
        else:

            print(f"Invalid file path: {path}")
            return

        if not name:
            print(f"Name must be specified")
            return

        if self.invalid_file_name_characters in name:
            print(f"Invalid file name: {name}")
            return
        try:
            if in_cd:
                os.rename(
                    self.home_directory + self.current_offset_directory + path, name
                )
            else:
                os.rename(path, name)
        except NameError:
            print(f"What, how? How did a NameError occur??")
        except Exception as e:
            print(f"Error renaming file: {e}")

    def remove_file(self): ...

    def remove_directory(self): ...

    def create_file(self):
        if (
            not self.current_command_parameters_bool
        ):  # or self.current_command_parameters.find(" ") > -1
            print(
                f">> To use '{self.current_command}' you need to specify one parameter."
            )
            return

        # self.current_command_parameters = self.current_command_parameters.replace("/", "\\")

        # print(self.current_command_parameters)

        try:
            open(f"{self.current_directory}{self.current_command_parameters}", "w")
        except Exception as e:
            print(f"Error creating file:{e}")

        # with open("./directory", "w") as f:
        #     f.write("Roots:\n")
        #     for i in roots:
        #         f.write(f"\t{i}\n")
        #     f.write("\nFiles:\n")
        #     for i in files:
        #         f.write(f"\t{i}\n")
        #     f.write("\nFolders:\n")
        #     for i in folders:
        #         f.write(f"\t{i}\n")

        # print(all, "what")


# Slander


def StartSimDirFilSystemForUser():
    ComSimFileSys = SimDirFilSystem(os.path.dirname(__file__) + "/limited_dir")

    while True:
        ComSimFileSys.ask_for_command()
        ComSimFileSys.execute()
        # print(ComSimFileSys.current_directory)
        print("Latest:", ComSimFileSys.last)


StartSimDirFilSystemForUser()
