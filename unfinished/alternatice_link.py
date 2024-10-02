import os
import win32com.client
from typing import Any
import ctypes, sys



def create_shortcut(source_path: str, shortcut_path: str, shortcut_name: str) -> str:
    shell = win32com.client.Dispatch("WScript.Shell")

    shortcut = shell.CreateShortcut(os.path.join(shortcut_path, shortcut_name + ".lnk"))

    shortcut.TargetPath = source_path

    shortcut.save()


def create_symlink(source_path: str, link_path: str) -> str:
    "link_path is the symlink path, source_path is what your pointing to. Usually requires admin privileges"
    try:
        os.symlink(source_path, link_path)
        return ""
    except OSError as e:
        return f"Error: {e}"



def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_python_script_as_admin(script_path:str, *args:Any)->str:
    args_str = ' '.join([f'"{arg}"' for arg in args])
    command = f'{sys.executable} "{script_path}" {args_str}'

    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, command, None, 1)
        return ""
    except Exception as e:
        return f"Failed to request admin privileges: {e}"


