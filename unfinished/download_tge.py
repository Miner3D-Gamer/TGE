import os, tempfile




python_installation = f"{os.getenv('LOCALAPPDATA')}\Programs\Python"
print(python_installation)

dirs = {
    f"{i.path}/Lib/site-packages/tge"
    for i in os.scandir(python_installation)
    if os.path.exists(f"{i.path}/Lib/site-packages")
}

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
            
            