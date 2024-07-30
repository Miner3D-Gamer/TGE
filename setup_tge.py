import os, json

import tge

tge.console.clear()

print(tge.INIT_TIME)

total_functions = tge.tbe.count_functions_in_library("tge")
print("TGE has %s functions" % total_functions)
undocumented = tge.tbe.print_undocumented_functions_in_directory()
print(
    f"{total_functions-undocumented}/{total_functions} Functions are documented, that means {((total_functions-undocumented)/total_functions)*100}% of functions are documented and {undocumented} are still missing"
)
print()
tge.tbe.print_check_for_functions_in_module_with_missing_notations(
    tge.manipulation.list_utils
)
# print("lines:", tge.tbe.count_lines_in_directory("./tge"))
dir = f"{os.getcwd()}/tge/"

for i in range(2):
    generated_uuid = tge.tbe.generate_uuid_from_directory(dir, ["hashed"])

    with open("tge/update.hashed", "w") as f:
        f.write(tge.codec.base.encode_base64(str(generated_uuid.bytes)[2:-1]))


print()
directories = []


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
try:
    os.remove(output)
except PermissionError:
    print(
        "VS is still using the minified tge folder, delete it manually or just leave it"
    )
except FileNotFoundError:
    ...

with open(".gitignore", "w") as f:
    f.write(
        "\n".join(
            [
                file[2:].replace("\\", "/")
                for file in tge.tbe.find_files_with_extension(".", ".pyc")
            ]
        )
    )


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
                    (
                        tge.tbe.remove_unused_libraries(
                            "".join(
                                [
                                    tge.manipulation.string_utils.left_replace(
                                        line, "	", " "
                                    )
                                    for line in tge.tbe.minify(
                                        f.read(),
                                        rename_important_names=False,
                                        remove_docstrings=True,
                                    )
                                ]
                            )
                        )
                    )
                    if file.endswith(".py")
                    else f.read()
                )
                o.write(data)
tge_size = tge.conversion.binary.convert_byte_to_kilobyte(
    tge.file_operations.get_file_size_of_directory("./tge", [".pyc"])
)
minified_size = tge.conversion.binary.convert_byte_to_kilobyte(
    tge.file_operations.get_file_size_of_directory("./minified_tge", [".pyc"])
)

# with open("download_tge.py", "r") as f:
#     data = tge.tbe.minify(
#         f.read(),
#         rename_important_names=False,
#         remove_docstrings=True,
#     )
#     with open("minified_downloader.py", "w") as w:
#         w.write(data)


print("Size of TGE: %s kb" % tge_size)
print("Size of minified TGE: %s kb" % minified_size)
print(
    "The minified TGE is %sx smaller"
    % str(tge_size / (minified_size if minified_size != 0 else tge_size))
)

print("Is github version of tge up to date:", not tge.is_tge_outdated())
# the hash is smiling b'[\xa5d(\\!\xb7\xd0P&\xaf\xec(:>\xde'
