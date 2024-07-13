import os, json, python_minifier

# Nope, I've tried optimizing this crap for the last 4 hours. This version is good enough
# Welp, TODO: Instead of using an array, use a dictionary for a greater compression.


import tge

directories = []

dir = f"{os.getcwd()}/tge/"
for root, dirs, files in os.walk(dir, topdown=False):
    root = root[len(dir) :].lstrip("\\")
    for name in files:
        file = os.path.join(root, name).replace("\\", "/")
        if file.endswith(".py"):
            file = file[:-2]
        elif file.endswith(".pyc"):
            continue
        directories.append(file)



compressed = tge.tbe.compress_directory_list(directories)

with open("directory.json", "w") as f:  #
    compressed = json.dumps(compressed)
    for replacer, replacement in [('", "', '","'), ('": ', '":'), (', "', ',"')]:
        compressed  = compressed.replace(replacer, replacement)
    f.write(compressed)





cwd = os.getcwd().replace("\\", "/")
output = rf"{cwd}/minified_tge/"
for root, dirs, files in os.walk(dir, topdown=False):
    root = root.replace("\\", "/")
    for file in files:

        file = file.replace("\\", "/")
        file_path = os.path.join(root[len(dir) :].lstrip("/"), file)
        total_file_path = os.path.join(root, file)
        with open(total_file_path, "r", encoding="utf8") as f:
            if file.endswith(".pyc"):
                continue
            os.makedirs(os.path.dirname(output + file_path), exist_ok=True)
            with open(output + file_path, "w", encoding="utf8") as o:
                if file.endswith(".py"):
                    data = python_minifier.minify(
                        f.read(), rename_globals=False, remove_literal_statements=True
                    )
                else:
                    data = f.read()
                o.write(data)
