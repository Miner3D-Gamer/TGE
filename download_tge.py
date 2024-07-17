import os, tkinter, time
import tkinter.filedialog as filedialog
import shutil
import sys


class ArgumentHandler:
    def __init__(C, arguments=None):
        B = arguments
        if B is None:
            B = sys.argv[1:]
        C.a = B

    def get_argument_by_flag(A, flag, delete=False, default=None):
        C = default
        if not flag in A.a:
            B =  -1
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
argument_handler = ArgumentHandler()

def is_directory_empty(directory_path):
    return not os.listdir(directory_path)

sl = argument_handler.get_argument_by_flag("-suppression_level",delete=True, default="0")
if sl.isdigit():
    give_feedback  =  int(sl)
else:
    give_feedback  =  0

default_python_installation = f"{os.getenv('LOCALAPPDATA')}\Programs\Python"
while True:
    inp = argument_handler.get_argument_by_flag("-install_option",delete=True, default=False)
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
        dirs = {
            f"{i.path}/Lib/site-packages/tge"
            for i in os.scandir(default_python_installation)
            if os.path.exists(f"{i.path}/Lib/site-packages")
        }

        break
    elif inp == "2":
        path =  argument_handler.get_argument_by_flag("-path",delete=True, default=False)
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
        path =  argument_handler.get_argument_by_flag("-path",delete=True, default=False)
        if not path:
            path = filedialog.askdirectory()
        if not os.path.exists(path):
            if give_feedback <1:
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
    
    inp = argument_handler.get_argument_by_flag("-install_minified",delete=True, default=None)
    if inp is None:
        inp = (
            input(
                f"Do you wanna download the minified version of TGE? (Y/N)\nThe minified version will require less space (~200kb instead of ~800kb) but all docstring and annotations have been removed\nYour Input: "
            )
            .strip()
            .lower()
        )
    if inp in ["n", "2", "nope"]:
        github_url = f"{base_github_url}tge/"
        break

    elif inp in ["y", "1", "sure"]:
        github_url = f"{base_github_url}minified_tge/"
        break


import requests, json

response = requests.get(f"{base_github_url}directory.json")

response.raise_for_status()

def decompress_directory_list(compressed): # FIXME: THIS IS BROKEN FOR PATHS WHERE THERE IS ONLY ONE FILE AND I HAVE NO IDEA HOW TO FIX IT
    paths = []

    def dfs(node, current_path=""):
        if isinstance(node, list):
            paths.append(f"{current_path}/{node[0]}".strip('/'))
            return
        if isinstance(node, str):
            paths.append(node)
            return

        for key, value in node.items():
            if key == 'files':
                for file_path in value:
                    paths.append(f"{current_path}/{file_path}".strip('/'))
            else:
                dfs(value, f"{current_path}/{key}".strip('/'))

    dfs(compressed)
    return paths


files = [
    (file + "py" if file.endswith(".") else file) for file in decompress_directory_list(json.loads(response.text))
]

urls:list[str] = [github_url + file for file in files]

for dir in dirs:
    if os.path.exists(dir):
        shutil.rmtree(dir)




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

    for idx in range(len(dirs)):
        try:
            installation_directory = dirs[idx]
        except:
            break
        
        path = os.path.join(installation_directory, file_name)
        parent_dir = os.path.dirname(path)
        if not os.path.exists(parent_dir):
            if give_feedback < 2:
                print(
                    "Directory '%s' cannot be found anymore, maybe it has been moved or deleted."
                    % parent_dir
                )
            dirs.pop(idx)
            continue
        os.makedirs(parent_dir, exist_ok=True)
        with open(path, "w", encoding="utf8") as f:
            f.write(file.text)
end = time.time()


for dir in dirs:
    sys.path.append(dir)

try:
    import tge.library as library
    if give_feedback < 1:
        print("Done downloading TGE in %s seconds!" % (end - start))
except:
    if give_feedback < 2:
        print("Well, this didn't quit work out. Wasted about %s seconds" % (end - start))
    quit()


output = library.install_all_libraries(requirements)

for successful, error in output:
    if not successful:
        if give_feedback < 3:
            print("Error while downloading dependency:", error)
