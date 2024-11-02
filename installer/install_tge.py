# 1.0.0
try:
    import tkinter.filedialog as filedialog
except ImportError:
    TKINTER_available = False
else:
    TKINTER_available = True

from typing import Optional, Union, Any, Callable, List, Dict
from importlib.util import find_spec as importlib_find_spec
import requests, json, subprocess, sys, os, shutil, time
NestedList = List[Union[str, "NestedList"]]

def is_library_installed(library_name: str) -> bool:
    return importlib_find_spec(library_name) is not None


class ArgumentHandler:
    def __init__(self, arguments:Optional[List[str]]=None):
        B = arguments
        if B is None:
            self.a = sys.argv[1:]
        else:
            self.a = B

    def get_argument_by_flag(
        self, flag: str, delete: bool = False, default: Any=None
    ) -> Optional[Union[str, Any]]:
        
        if not flag in self.a:
            b = -1
        else:
            b = self.a.index(flag)
        
        if b < 0:
            return default
        if b + 1 == len(self.a):
            return default
        if delete:
            self.a.pop(b)
            d = self.a.pop(b)
        else:
            d = self.a.__getitem__(b + 1)
        return d

    def has_argument(self, argument: str, delete: bool=False):
        return argument in self.a


argument_handler = ArgumentHandler()


def is_directory_empty(directory_path: str) -> bool:
    return not os.listdir(directory_path)


sl = argument_handler.get_argument_by_flag(
    "-suppression_level", delete=True, default="0"
)
if not isinstance(sl, str):
    sl = "this will never happen yet my IDE plugin is too stupid know that and won't shut up"

if sl.isdigit():
    give_feedback = int(sl)
else:
    give_feedback = 0

wait_for_reaction = (
    argument_handler.has_argument("-clingy", delete=True) and give_feedback < 3
)


if is_library_installed("tge"):
    try:
        import tge
    except:
        pass
    else:
        if not hasattr(tge, "is_tge_outdated"):
            if give_feedback < 2:
                print("Installed TGE seems to be corrupted")
        else:
            if not tge.is_tge_outdated():
                while True:
                    if argument_handler.get_argument_by_flag(
                        "-install_option", delete=False, default=False
                    ):
                        break
                    inp = (
                        input(
                            "Your local TGE is already up to date, are you sure you wanna continue? (y/n): "
                        )
                        .lower()
                        .strip()
                    )
                    if inp == "n":

                        if wait_for_reaction:
                            input()
                        quit()
                    elif inp == "y":
                        break

unify: Callable[[str], str] = lambda x: x.replace("\\", "/")

default_python_installation = rf"{os.getenv('LOCALAPPDATA')}\Programs\Python"
while True:
    inp = argument_handler.get_argument_by_flag(
        "-install_option", delete=True, default=False
    )
    if not inp:
        inp = input(
            f"""Choose how to install TGE (Enter Number):
        1. Install TGE for all installed python installations in the default python installation ({default_python_installation})

        2. Select a file (.exe) in the python folder you wanna install TGE in (Visual Window)

        3. Select a folder to install TGE into (Visual Window)

        4. Input folder or file you want to install tge into (Console)
        
        5. Cancel Installation
        Your Input: """
        ).strip()
        if inp.startswith("&"):
            quit()

    if inp == "1":
        dirs = [
            f"{i.path}/Lib/site-packages/tge"
            for i in os.scandir(default_python_installation)
            if os.path.exists(f"{i.path}/Lib/site-packages")
        ]

        break
    elif inp == "2":
        path = argument_handler.get_argument_by_flag(
            "-path", delete=True, default=False
        )
        if not path:

            if TKINTER_available:
                path = filedialog.askopenfilename() # type: ignore
            else:
                path = input("(Tkinter not available) Directory: ")
        path = os.path.dirname(path) + "/Lib/site-packages"
        if os.path.exists(path):
            dirs = [
                path + "/tge" if not unify(path).endswith("/tge") else ""
            ]
            break
        else:
            if give_feedback < 1:
                print("'%s' could not be found\n" % path)
            continue
    elif inp == "3":
        path = argument_handler.get_argument_by_flag(
            "-path", delete=True, default=False
        )
        if not path:
            if TKINTER_available:
                path = filedialog.askdirectory() # type: ignore
            else:
                path = input("(Tkinter not available) Directory: ")
        if not os.path.exists(path):
            if give_feedback < 1:
                print("Path not found.")
            continue
        if is_directory_empty(path) or path.endswith("\\tge"):
            dirs = [path]
            break
        dirs = [path + "/tge"]
        break
    elif inp == "4":
        path = input("Directory: ")
        if not os.path.exists(path):
            if give_feedback < 1:
                print("Directory does not exist, canceling.")
            quit()
        if is_directory_empty(path) or path.endswith("\\tge"):
            dirs = [path]
            break
        dirs = [path + "/tge"]
        break
    elif inp == "5":
        quit()

if give_feedback < 1:
    print()
base_github_url = "https://raw.githubusercontent.com/Miner3D-Gamer/TGE/main"
while True:

    inp = argument_handler.get_argument_by_flag(
        "-install_minified", delete=True, default=None
    )
    if inp is None:
        min_space = "350kb"
        norm_space = "600kb"
        min_import_time = "0.01-0.3"
        norm_import_time = "0.4-0.6"
        inp = (
            input(
                "Do you want download the minified version of TGE? (Y/N)\nThe minified version will require less space (~%ss instead of ~%ss) and will be faster to import (%s instead of %s) but all docstring and annotations have been removed. Runtime differences are unknown (Default:N)\nYour Input: "
                % (min_space, norm_space, min_import_time, norm_import_time)
            )
            .strip()
            .lower()
        )
    if inp in ["n", "2", "nope"]:
        github_url = unify(os.path.join(base_github_url, "tge"))
        break

    elif inp in ["y", "1", "sure", ""]:
        github_url = unify(os.path.join(base_github_url, "minified_tge"))
        break


response = requests.get(unify(os.path.join(base_github_url, "directory.json")))

response.raise_for_status()


def decompress_file_path_dict(data: Dict[str, Any], current_path: str = "") -> List[str]:
    paths: List[str] = []
    dirs = "d"
    files = "f"

    if files in data:
        for file in data[files]:
            paths.append(current_path + file)

    if dirs in data:
        for dir_name, dir_content in data[dirs].items():
            paths.extend(decompress_file_path_dict(dir_content, current_path + dir_name + "/"))

    return paths

def decompress_file_path_list(data: NestedList, current: str="")-> List[str]:
    directories: List[str] = []

    def handle_folder_list(data: List[Union[str, List[Any]]]) -> List[str]:
        # List[str], str
        dir: List[str] = []
        for folder in data:
            if not isinstance(folder, list):
                raise ValueError("Expected lists but got %s" % type(folder))
            dir.extend(handle_folder(folder))
        return dir

    def handle_folder(data: List[Any]) -> List[str]:
        nonlocal current, add
        dir:List[str] = []
        if isinstance(data, str):
            raise ValueError("Expected list but got %s" % type(data[0]))
        dir.extend(decompress_file_path_list(data[1], add(data[0])))
        return dir
    
    add: Callable[[str], str] = lambda path: (current + "/" + path) if current else path
    #remove = lambda: "/".join(current.split("/")[:-1])

    size = len(data)
    if size == 2:
        if isinstance(data[0], list):
            if len(data[0]) == 2:
                if isinstance(data[0][0], list):
                    directories.extend(handle_folder_list(data[0]))
                else:
                    directories.extend(handle_folder(data[0]))
            else:
                directories.extend(handle_folder_list(data[0]))

        else:
            if isinstance(data[1], list):
                current = add(data[0])
                directories.extend(handle_folder(data[1]))
            else:
                for file in data:
                    if not isinstance(file, str):
                        raise ValueError("Expected strings but got %s" % type(file))
                    directories.append(add(file))
    else:
        for file in data:
            if not isinstance(file, str):
                raise ValueError("Expected strings but got %s" % type(file))
            directories.append(add(file))

    return directories


def decompress_file_paths(data: Union[NestedList, Dict[str, Any]])->Union[List[str],Dict[str,Any]]:
    if isinstance(data, list):
        return decompress_file_path_list(data)
    else:
        return decompress_file_path_dict(data)

files = [
    (file + "py" if file.endswith(".") else file)
    for file in decompress_file_path_list(json.loads(response.text))
]

urls = [unify(os.path.join(github_url, file)) for file in files if file.__contains__(".")]

for dir in dirs:
    if os.path.exists(dir):
        shutil.rmtree(dir)

if give_feedback < 1:
    print("Directories tge will download into:")
    print(*dirs, sep="\n", end="\n\n")

requirements = []
start = time.time()
total_urls = len(urls)
for file_id in range(total_urls):
    url = urls[file_id]
    file_name = files[file_id]
    if give_feedback < 1:
        print("Downloading %s" % url)

    file = requests.get(url)
    try:
        file.raise_for_status()
    except requests.HTTPError as e:
        if give_feedback < 3:
            print("Error while downloading %s : %s" % (file_name, e))
        continue

    if url.endswith("/requirements.txt"):
        requirements = file.text.split("\n")

    dir_offset = 0
    total_dirs = len(dirs)
    if total_dirs == 0:
        if give_feedback < 3:
            print("No download directory left, aborting download")
        if wait_for_reaction:
            input()
        break
    for idx in range(total_dirs):
        installation_directory = dirs[idx]

        if not os.path.exists(installation_directory):
            os.mkdir(installation_directory)

        path = unify(os.path.join(installation_directory, file_name))
        parent_dir = os.path.dirname(path)
        if not os.path.exists(installation_directory):
            if give_feedback < 2:
                print(
                    "Directory '%s' cannot be found anymore, maybe it has been moved or deleted."
                    % installation_directory
                )
            dirs.pop(idx)
            continue
        os.makedirs(parent_dir, exist_ok=True)
        if give_feedback < 1:
            print(f"Writing to {path} ({file_id+1}/{total_urls}) ({idx+1}/{total_dirs}) ({round((file_id+1)/total_urls*100,2)}%)")
        with open(path, "w", encoding="utf8") as f:
            f.write(file.text)
    if give_feedback < 1:
        print("Done writing!")


dont_download_dependencies = argument_handler.has_argument(
    "-skip_dependencies", delete=True
)
error = 0
if not dont_download_dependencies:
    if give_feedback < 1:
        print("Checking and downloading dependencies")

    def download_library(library_name: str):
        G = False
        E = "pip"
        D = True
        C = "install"
        A = library_name
        H = [
            ["python", "-m", E, C, A],
            ["python3", "-m", E, C, A],
            [E, C, A],
            ["pip3", C, A],
        ]
        j = None
        for F in H:
            try:
                I = subprocess.run(F, check=D, capture_output=D, text=D)
                return D, I.stdout
            except subprocess.CalledProcessError as b:
                j = f"Failed to install {A} using command: {' '.join(F)}. Return code: {b.returncode}. Output: {b.output}. Error: {b.stderr}."
            except FileNotFoundError:
                continue
            except Exception as b:
                return G, f"An unexpected error occurred: {str(b)}"
        return G, f"All installation attempts failed. Last error: {j}"

    def install_all_libraries(libs: List[str]):
        global error
        for B in libs:
            lib_renames = {"Pillow": "PIL"}
            if is_library_installed(lib_renames.get(B, B.replace("-", "_"))):
                continue
            if give_feedback < 2:
                print("Downloading %s" % B)
            successful, info = download_library(B)
            if successful:
                if give_feedback < 2:
                    print("Successfully installed %s" % B)
            else:
                if B == "pyobjc" and platform.system() != "Darwin":
                    continue
                if give_feedback < 3:
                    print("Error while installing %s: %s" % (B, info))
                error += 1

    import platform

    install_all_libraries(requirements)
    # install_rate = len(requirements)/error
# else:
#     install_rate = -1


end = time.time()
if give_feedback < 1:
    print(
        "\nDownloading and installing tge %stook %s seconds"
        % (
            (
                ""
                if dont_download_dependencies
                else (
                    "and all it's dependencies "
                    if error == 0
                    else " and %s out of %s dependencies "
                    % (len(requirements) - error, len(requirements))
                )
            ),
            end - start,
        )
    )
if wait_for_reaction:
    input()
