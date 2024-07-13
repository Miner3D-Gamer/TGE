import os, tkinter, time
import tkinter.filedialog


def is_directory_empty(directory_path):
    return not os.listdir(directory_path)


default_python_installation = f"{os.getenv('LOCALAPPDATA')}\Programs\Python"
while True:
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
        path = tkinter.filedialog.askopenfilename()
        path = os.path.dirname(path) + "/Lib/site-packages"
        if os.path.exists(path):
            dirs = [path + "/tge"]
            break
        else:
            print("'%s' could not be found" % path)
            quit()
    elif inp == "3":
        path = tkinter.filedialog.askdirectory()
        if not os.path.exists(path):
            print("Path not found.")
            continue
        if is_directory_empty(path):
            dirs = [path]
            break
        dirs = [path + "/tge"]
        break


print()
base_github_url = "https://raw.githubusercontent.com/Miner3DGaming/TGE/main/"
while True:
    inp = (
        input(
            f"Do you wanna download the minified version of TGE? (Y/N)\nThe minified version will be faster to download and require less space (~300kb instead of ~1mb) but manually editing it for whatever reason will be annoying\nYour Input: "
        )
        .strip()
        .lower()
    )
    if inp == "n" or inp == "2":
        github_url = f"{base_github_url}tge/"
        break

    elif inp == "y" or inp == "1":
        github_url = f"{base_github_url}minified_tge/"
        break


import requests, json

response = requests.get(f"{base_github_url}directory.json")

response.raise_for_status()


files = [
    (file + "py" if file.endswith(".") else file) for file in json.loads(response.text)
]

urls = [github_url + file for file in files]

requirements = []
start = time.time()
for file_id in range(len(urls)):
    url = urls[file_id]
    file_name = files[file_id]
    print("Downloading %s" % url)

    file = requests.get(url)
    try:
        file.raise_for_status()
    except requests.HTTPError:
        print("Error while downloading %s" % file_name)
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

import sys

for dir in dirs:
    sys.path.append(dir)

try:
    import tge.library as library

    print("Done downloading TGE in %s seconds!" % (end - start))
except:
    print("Well, this didn't quit work out. Wasted about %s seconds" % (end - start))
    quit()





output = library.install_all_libraries(requirements)

for successful, error in output:
    if not successful:
        print("Error while downloading dependency:", error)
