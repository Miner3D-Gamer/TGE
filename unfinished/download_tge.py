import os, tkinter, time
import tkinter.filedialog


default_python_installation = f"{os.getenv('LOCALAPPDATA')}\Programs\Python"
while True:
    inp = input(
        f"""Choose how to install TGE (Enter Number):
    1. Install TGE for all installed python installations in the default python installation ({default_python_installation})
                
    2. Select a file (.exe) in the python folder you wanna install TGE in
    
    Your Input: """
    ).strip()
    if not inp in ["1", "2"]:
        if inp.startswith("&"):
            quit()
        continue
    if inp == "1":
        dirs = {
            f"{i.path}/Lib/site-packages/tge"
            for i in os.scandir(default_python_installation)
            if os.path.exists(f"{i.path}/Lib/site-packages")
        }

        break
    else:
        path = tkinter.filedialog.askopenfilename()
        path = os.path.dirname(path) + "/Lib/site-packages"
        if os.path.exists(path):
            dirs = [path + "/tge"]
            break
        else:
            print("'%s' could not be found" % path)
            quit()


while True:
    inp = (
        input(
            f"Do you wanna download the minified version of TGE? (Y/N)\nThe minified version will be faster to download but manually editing it for whatever reason will be annoying\nYour Input: "
        )
        .strip()
        .lower()
    )
    if inp == "n" or inp == "1":
        github_url = "https://raw.githubusercontent.com/Miner3DGaming/TGE/main/tge/"
        break

    elif inp == "y":
        github_url = (
            "https://raw.githubusercontent.com/Miner3DGaming/TGE/main/minified_tge/"
        )
        break


import requests, json

response = requests.get(
    "https://raw.githubusercontent.com/Miner3DGaming/TGE/main/directory.json"
)

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
        print("Error while downloading %s"% file_name)
        continue

    if url.endswith("/requirements.txt"):
        requirements = file.text.split("\n")

    for installation_directory in dirs:
        path = os.path.join(installation_directory, file_name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf8") as f:
            f.write(file.text)
end = time.time()


try:
    import tge.library as library
    print("Done downloading TGE in %s seconds!" % (end - start))
except:
    print("Well, this didn't quit work out. Wasted about %s seconds" % (end-start))
    quit()


import sys

for dir in dirs:
    sys.path.append(dir)




output = library.install_all_libraries(requirements)

for successful, error in output:
    if not successful:
        print("Error while downloading dependency:", error)
