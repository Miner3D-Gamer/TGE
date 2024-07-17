import os, json

# Nope, I've tried optimizing this crap for the last 4 hours. This version is good enough
# Welp, TODO: Instead of using an array, use a dictionary for a greater compression.


import tge
print(tge.manipulation.string_utils.check_anagram("Hell oWl!dor", "Hello World!"))
print("TGE has %s functions"%tge.tbe.count_functions_in_library("tge"))
tge.tbe.print_undocumented_functions_in_directory()
print()
tge.tbe.print_check_for_functions_in_module_with_missing_notations(tge)


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
        compressed = compressed.replace(replacer, replacement)
    f.write(compressed)


cwd = os.getcwd()
output = rf"{cwd}/minified_tge/"
for root, dirs, files in os.walk(dir, topdown=False):
    root = root
    for file in files:
        file_path = os.path.join(root[len(dir) :].lstrip("\\"), file)
        total_file_path = os.path.join(root, file)
        if file.endswith(".pyc"):
                continue
        if file.endswith(".hash"):
            with open(total_file_path, "rb") as f:
                with open(output + file_path, "wb") as o:
                    data = f.read()
                    
                    o.write(data)
            continue
        with open(total_file_path, "r", encoding="utf8") as f:
            
            os.makedirs(os.path.dirname(output + file_path), exist_ok=True)
            
            with open(output + file_path, "w", encoding="utf8") as o:
                data = (
                    tge.tbe.minify(
                        f.read(), rename_important_names=False, remove_docstrings=True
                    )
                    if file.endswith(".py")
                    else f.read()
                )
                o.write(data)

import hashlib, uuid

generated_uuid = tge.tbe.generate_uuid_from_directory(dir)
with open("update.hashed", "w") as f:
    f.write(str(generated_uuid.bytes))


print(tge.is_tge_outdated())
# the hash is smiling b'[\xa5d(\\!\xb7\xd0P&\xaf\xec(:>\xde'