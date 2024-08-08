import os, time
import tkinter.filedialog as filedialog
import shutil
import sys
import importlib.util
import subprocess


def is_library_installed(library_name):
    A = importlib.util.find_spec(library_name)
    return A is not None


class ArgumentHandler:
    def __init__(C, arguments=None):
        B = arguments
        if B is None:
            B = sys.argv[1:]
        C.a = B

    def get_argument_by_flag(A, flag, delete=False, default=None):
        C = default
        if not flag in A.a:
            B = -1
        else:
            B = A.a.index(flag)
        if B < 0:
            return default
        if B + 1 == len(A.a):
            return default
        if delete:
            A.a.pop(B)
            D = A.a.pop(B)
        else:
            D = A.a.__getitem__(B + 1)
        return D

    def has_argument(self, argument, delete=False):
        return argument in self.a


argument_handler = ArgumentHandler()


def is_directory_empty(directory_path):
    return not os.listdir(directory_path)


sl = argument_handler.get_argument_by_flag(
    "-suppression_level", delete=True, default="0"
)
if sl.isdigit():
    give_feedback = int(sl)
else:
    give_feedback = 0

wait_for_reaction = not (
    argument_handler.has_argument("-hasty", delete=True) or give_feedback > 2
)


if is_library_installed("tge"):
    try:
        import tge
    except:
        pass
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


default_python_installation = f"{os.getenv('LOCALAPPDATA')}\Programs\Python"
while True:
    inp = argument_handler.get_argument_by_flag(
        "-install_option", delete=True, default=False
    )
    if not inp:
        inp = input(
            f"""Choose how to install TGE (Enter Number):
        1. Install TGE for all installed python installations in the default python installation ({default_python_installation})
                    
        2. Select a file (.exe) in the python folder you wanna install TGE in
        
        3. Select a folder to install TGE into
        
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
            path = filedialog.askopenfilename()
        path = os.path.dirname(path) + "/Lib/site-packages"
        if os.path.exists(path):
            dirs = [path + "/tge"]
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
            path = filedialog.askdirectory()
        if not os.path.exists(path):
            if give_feedback < 1:
                print("Path not found.")
            continue
        if is_directory_empty(path):
            dirs = [path]
            break
        dirs = [path + "/tge"]
        break

if give_feedback < 1:
    print()
base_github_url = "https://raw.githubusercontent.com/Miner3DGaming/TGE/main/"
while True:

    inp = argument_handler.get_argument_by_flag(
        "-install_minified", delete=True, default=None
    )
    if inp is None:
        min_space = "300kb"
        norm_space = "600kb"
        min_import_time = "0.05-0.01"
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
        github_url = f"{base_github_url}tge/"
        break

    elif inp in ["y", "1", "sure", ""]:
        github_url = f"{base_github_url}minified_tge/"
        break


import requests, json

response = requests.get(f"{base_github_url}directory.json")

response.raise_for_status()


def decompress_directory_list(
    compressed: dict,
) :
    # FIXME: THIS IS BROKEN FOR PATHS WHERE THERE IS ONLY ONE FILE AND I HAVE NO IDEA HOW TO FIX IT
    paths = []

    def dfs(node, current_path="") -> None:
        nonlocal paths

        if isinstance(node, list):
            paths.append(f"{current_path}/{node[0]}".strip("/"))
            return
        if isinstance(node, str):
            paths.append(node)
            return

        for key, value in node.items():
            if key == "files":
                for file_path in value:
                    paths.append(f"{current_path}/{file_path}".strip("/"))
            else:
                dfs(value, f"{current_path}/{key}".strip("/"))

    dfs(compressed)
    return paths


files = [
    (file + "py" if file.endswith(".") else file)
    for file in decompress_directory_list(json.loads(response.text))
]

urls = [github_url + file for file in files]

for dir in dirs:
    if os.path.exists(dir):
        shutil.rmtree(dir)

if give_feedback < 1:
    print("Directories tge will download into:")
    print(*dirs, sep="\n", end="\n\n")

requirements = []
start = time.time()
for file_id in range(len(urls)):
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
    for idx in range(len(dirs)):
        try:  # TODO: THIS IS BOUND TO GO WRONG CHANGE THIS TO BE BETTER
            installation_directory = dirs[idx - dir_offset]
        except ValueError:
            break

        if not os.path.exists(installation_directory):
            os.mkdir(installation_directory)

        path = os.path.join(installation_directory, file_name)
        parent_dir = os.path.dirname(path)
        if not os.path.exists(installation_directory):
            if give_feedback < 2:
                print(
                    "Directory '%s' cannot be found anymore, maybe it has been moved or deleted."
                    % installation_directory
                )
            dirs.pop(idx)
            dir_offset += 1
            continue
        os.makedirs(parent_dir, exist_ok=True)
        print(f"Writing to {path}")
        with open(path, "w", encoding="utf8") as f:
            f.write(file.text)
    if give_feedback < 1:
        print("Done writing!")


dont_download_dependencies = argument_handler.has_argument(
    "-skip_dependencies", delete=True
)
if not dont_download_dependencies:

    if give_feedback < 1:
        print("Checking and downloading dependencies")

    def download_library(library_name):
        D = False
        C = library_name
        B = True
        E = ["python", "-m", "pip", "install", C]
        try:
            F = subprocess.run(E, check=B, capture_output=B, text=B)
            return B, F.stdout
        except subprocess.CalledProcessError as A:
            G = f"Failed to install {C}. Return code: {A.returncode}. Output: {A.output}. Error: {A.stderr}."
            return D, G
        except Exception as A:
            return D, f"An unexpected error occurred: {str(A)}"

    if give_feedback < 1:
        print("Directories tge will download into:")
        print(*dirs, sep="\n", end="\n\n")

    def install_all_libraries(libs):
        A = []
        for B in libs:
            if is_library_installed(B):
                A.append((True, ""))
                continue
            A.append(download_library(B))
        return A

    import platform

    output = install_all_libraries(requirements)
    if give_feedback < 3:
        for id, value in enumerate(output):
            successful, error = value
            if not successful:
                library = requirements[id]
                if library == "pyobjc":
                    if platform.system() != "Darwin":
                        continue
                print(
                    "Error while downloading dependency (%s):" % requirements[id], error
                )
end = time.time()
if give_feedback < 1:
    print(
        "\nDownloading and installing tge %s took %s seconds"
        % (
            "and all it's dependencies" if not dont_download_dependencies else "",
            end - start,
        )
    )
if wait_for_reaction:
    input()
