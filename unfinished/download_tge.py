import os,tkinter
import tkinter.filedialog


default_python_installation = f"{os.getenv('LOCALAPPDATA')}\Programs\Python"
while True:
    inp = input(f"""Choose how to install TGE (Enter Number):
    1. Install TGE for all installed python installations in the default python installation ({default_python_installation})
                
    2. Select a file (.exe) in the python folder you wanna install TGE in
    
    Your Input: """).strip()
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
            dirs = [path+ "/tge"]
            break
        else:
            print("'%s' could not be found" % path)
            quit()
        
    
    



import requests, json

response = requests.get(
    "https://raw.githubusercontent.com/Miner3DGaming/TGE/main/directory.json"
)

response.raise_for_status()


files = [
    (file + "py" if file.endswith(".") else file) for file in json.loads(response.text)
]

urls = [
    "https://raw.githubusercontent.com/Miner3DGaming/TGE/main/tge/" + file
    for file in files
]

for file_id in range(len(urls)):
    url = urls[file_id]
    file_name = files[file_id]
    print("Downloading %s" % url)

    file = requests.get(url)
    try:
        file.raise_for_status()
    except requests.HTTPError:
        print("Error while downloading %s", file_name)
    
    for installation_directory in dirs:
        path = os.path.join(installation_directory, file_name)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf8")as f:
            f.write(file.text)

print("Done downloading TGE!")




import sys

for dir in dirs:
    sys.path.append(dir)

import tge.library as library

library.install_all_libraries()

