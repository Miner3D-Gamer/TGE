# tge - Text Game Engine


Originally made for displaying and creating console-based games but has evolved into a general-purpose library.

This library provides a wide range of functions and utilities for text-based game development, console operations,
data manipulation, conversions, math calculations, user interfaces, file operations, and more.

With a collection of over 800 functions, tge tries to simplify the development process and offers capabilities for
building text-based games, console applications, file manipulation, and various quality of life functions. (yay)

## How to install:
  1. Download the .py or .exe from the releases

  2. Execute the downloaded file


## If you use the .py you can use additional inputs to predefine options:
  If something is inputted what isn't suspected, the default is used


### -suppression_level (Default:0):
  0: Logs all messages

  1: Only log warnings and errors

  2: Only log errors

  3: No completely quiet


### -install_option (Default:Asks user)
  1: Install TGE for all installed python installations in the default python installation ({default_python_installation})             
  2: Select a file (.exe) in the python folder you wanna install TGE in (Or use what is inside -path)
  3: Select a folder to install TGE into (Or use what is inside -path)


### -path (No Default)
  The directory to a file or folder depending on if the -install_option is set to 1 or 2


### -install_minified (Default:Asks user)
  Anything from this list: ["y", "1", "sure"]: Installs the minified version of TGE. The minified version is ~200kb instead of ~1.1mb (All notations and docstrings have been removed)
  Anything from this list: ["n", "2", "nope"]: Will install the normal version of TGE
