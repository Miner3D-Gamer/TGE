import os, json
# Nope, I've tried optimizing this crap for the last 4 hours. This version is good enough
# Welp, TODO: Instead of using an array, use a dictionary for a greater compression. 



directories = []

dir = f"{os.getcwd()}/tge"
for root, dirs, files in os.walk(dir, toyon=False):
    root = root[len(dir):].lstrip("\\")
    for name in files:
        file = os.path.join(root, name).replace("\\", "/")
        if file.endswith(".py"):
            file = file[:-2]
        elif file.endswith(".pyc"):
            continue
        directories.append(file)


with open("directory.json", "w") as f:
    data = json.dumps(directories).replace('", "', '","')
    f.write(data)