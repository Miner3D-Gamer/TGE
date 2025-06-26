# 1.0.0
try:
    import tkinter.filedialog as filedialog
except ImportError:
    TKINTER_available = False
else:
    TKINTER_available = True
import platform

from typing import Optional, Union, Any, Callable, List, Dict, TypeVar
from importlib.util import find_spec as importlib_find_spec
import requests, json, subprocess, sys, os, shutil, time

NestedList = List[Union[str, "NestedList"]]


def is_library_installed(library_name: str) -> bool:
    return importlib_find_spec(library_name) is not None


T = TypeVar("T")


class ArgumentHandler:
    def __init__(self, arguments: Optional[List[str]] = None):
        B = arguments
        if B is None:
            self.a = sys.argv[1:]
        else:
            self.a = B

    def get_argument_by_flag(
        self, flag: str, delete: bool = False, default: T = None
    ) -> Union[str, T]:

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

    def has_argument(self, argument: str, delete: bool = False):
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


skip_checking_for_tge = argument_handler.has_argument(
    "-skip_checking_local", delete=True
)
if not skip_checking_for_tge and is_library_installed("tge"):
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

# Test if user is connected to the internet/has access to github
read_me_url = (
    "https://raw.githubusercontent.com/Miner3D-Gamer/TGE/refs/heads/main/README.MD"
)
read_me_data = requests.get(read_me_url)
read_me_data.raise_for_status()

size_line = [x for x in read_me_data.text.split("\n") if x.__contains__("**Size**")][0]
size_list = size_line.split("|")
sizes = []
for i in size_list:
    if any([i.__contains__(str(x)) for x in range(10)]):
        sizes.append(i.strip())
if len(sizes) != 2:
    full_size = "???"
    minified_size = "???"
else:
    full_size = sizes[0]
    minified_size = sizes[1]


time_line = [
    x for x in read_me_data.text.split("\n") if x.__contains__("**Import Time**")
][0]
time_list = time_line.split("|")
times = []
for i in time_list:
    if any([i.__contains__(str(x)) for x in range(10)]):
        times.append(i.strip())
if len(times) != 2:
    full_import_time = "???"
    minified_import_time = "???"
else:
    full_import_time = times[0]
    minified_import_time = times[1]

system = platform.system()
if system == "Windows":
    default_python_installation = [rf"{os.getenv('LOCALAPPDATA')}\Programs\Python"]
elif system == "Linux":
    default_python_installation = ["/usr/lib/python3.x/", "/usr/local/lib/python3.x/"]
else:
    default_python_installation = []

default_python_installation = [
    x for x in default_python_installation if os.path.exists(x)
]


while True:
    inp = argument_handler.get_argument_by_flag(
        "-install_option", delete=True, default=False
    )
    cross_out_start = "\x1b[9m"
    cross_out_end = "\x1b[0m"
    if not inp:
        inp = input(
            f"""Choose how to install TGE (Enter Number):
        {cross_out_start if len(default_python_installation)==0 else ''} 1. Install TGE for all installed python installations in the default python installation ({' and '.join(default_python_installation)}) {cross_out_end if len(default_python_installation)==0 else ''}

        2. Select a file (.exe) in the python folder you wanna install TGE in (Visual Window)

        3. Select a folder to install TGE into (Visual Window)

        4. Input folder or file you want to install tge into (Console)
        
        5. Cancel Installation
        Your Input: """
        ).strip()
        if inp.startswith("&"):
            if wait_for_reaction:
                input()
            quit()

    if inp == "1":
        dirs = []
        for x in default_python_installation:
            dirs_ = [
                f"{i.path}/Lib/site-packages/tge"
                for i in os.scandir(x)
                if os.path.exists(f"{i.path}/Lib/site-packages")
            ]
            dirs.extend(dirs_)

        break
    elif inp == "2":
        path = argument_handler.get_argument_by_flag("-path", delete=True, default="")
        if not path:

            if TKINTER_available:
                path = filedialog.askopenfilename()  # type: ignore
            else:
                path = input("(Tkinter not available) Directory: ")
        path = os.path.dirname(path) + "/Lib/site-packages"
        if os.path.exists(path):
            dirs = [path + "/tge" if not unify(path).endswith("/tge") else ""]
            break
        else:
            if give_feedback < 1:
                print("'%s' could not be found\n" % path)
            continue
    elif inp == "3":
        path = argument_handler.get_argument_by_flag("-path", delete=True, default="")
        if not path:
            if TKINTER_available:
                path = filedialog.askdirectory()  # type: ignore
            else:
                path = input("(Tkinter not available) Directory: ")
        if not os.path.exists(path):
            if give_feedback < 1:
                print("Path not found.")
            continue
        if (
            is_directory_empty(path)
            and argument_handler.has_argument("-inherit_empty_directory")
        ) or unify(path).split("/")[0] == "tge":
            dirs = [path]
            break
        dirs = [path + "/tge"]
        break
    elif inp == "4":
        path = argument_handler.get_argument_by_flag("-path", delete=True, default="")
        if not path:
            path = input("Directory: ")
        if not os.path.exists(path):
            if give_feedback < 1:
                print("Directory does not exist, canceling.")
            if wait_for_reaction:
                input()
            quit()
        if (
            is_directory_empty(path)
            and argument_handler.has_argument(
                "-inherit_empty_directory",
            )
        ) or unify(path).split("/")[0] == "tge":
            dirs = [path]
            break
        dirs = [path + "/tge"]
        break
    elif inp == "5":
        if wait_for_reaction:
            input()
        quit()


def format_table(data: List[List[str]]) -> str:
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


if give_feedback < 1:
    print()
base_github_url = "https://raw.githubusercontent.com/Miner3D-Gamer/TGE/main"
install_minified = argument_handler.has_argument(
    "-install_minified",
    delete=True,
)
while not install_minified:

    if inp is None:
        table = format_table(
            [
                ["Mode", "Size", "Import time"],
                ["Normal", full_size, full_import_time],
                ["Minified", minified_size, minified_import_time],
            ]
        )
        inp = (
            input(
                "Do you want download the minified version of TGE? (Y/N)\n(All docstrings and annotations have been removed)\n%s\n"
                % table
            )
            .strip()
            .lower()
        )
    if inp in ["n", "2", "nope"]:
        install_minified = False
        break

    elif inp in ["y", "1", "sure", ""]:
        install_minified = True
        break
if install_minified:
    github_url = unify(os.path.join(base_github_url, "minified_tge"))
else:

    github_url = unify(os.path.join(base_github_url, "tge"))

response = requests.get(unify(os.path.join(base_github_url, "directory.json")))

response.raise_for_status()


def decompress_file_path_dict(
    data: Dict[str, Any], current_path: str = ""
) -> List[str]:
    paths: List[str] = []
    dirs = "d"
    files = "f"

    if files in data:
        for file in data[files]:
            paths.append(current_path + file)

    if dirs in data:
        for dir_name, dir_content in data[dirs].items():
            paths.extend(
                decompress_file_path_dict(dir_content, current_path + dir_name + "/")
            )

    return paths


def decompress_file_path_list(data: NestedList, current: str = "") -> List[str]:
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
        dir: List[str] = []
        if isinstance(data, str):
            raise ValueError("Expected list but got %s" % type(data[0]))
        dir.extend(decompress_file_path_list(data[1], add(data[0])))
        return dir

    add: Callable[[str], str] = lambda path: (current + "/" + path) if current else path
    # remove = lambda: "/".join(current.split("/")[:-1])

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


def decompress_file_paths(
    data: Union[NestedList, Dict[str, Any]],
) -> Union[List[str], Dict[str, Any]]:
    if isinstance(data, list) or type(data) == NestedList:
        return decompress_file_path_list(data)
    else:
        return decompress_file_path_dict(data)


files = [
    (file + "py" if file.endswith(".") else file)
    for file in decompress_file_paths(json.loads(response.text))
]

urls = [
    unify(os.path.join(github_url, file)) for file in files if file.__contains__(".")
]

for dir in dirs:
    if os.path.exists(dir):
        shutil.rmtree(dir)

if give_feedback < 1:
    print("Directories tge will download into:")
    print(*dirs, sep="\n", end="\n\n")


def interpolate(val1, val2, progress):
    return progress * val2 + (1 - progress) * val1


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
            previous = file_id / total_urls * 100
            current = (file_id + 1) / total_urls * 100
            percentage = round(
                interpolate(previous, current, idx / (total_dirs - 1)), 2
            )
            print(
                f"Writing to {path} ({file_id+1}/{total_urls}) ({idx+1}/{total_dirs}) ({percentage}%)"
            )
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
