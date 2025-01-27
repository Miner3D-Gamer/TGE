import os, json
from typing import List
import tge
import base64

# stubgen --recursive -p tge -o stubs
# Add NestedList to file_operations.py

tge.console.clear()

IGNORE = True

total_functions = tge.function_utils.count_functions_in_library("tge")
print("TGE has %s functions" % total_functions)
total_files = tge.file_operations.count_files_in_directory(
    "./tge",
    extension_backlist=[
        ".pyc",
        ".txt",
        ".hashed",
    ],
)
print("TGE has %s files" % total_files)


undocumented = tge.tbe.print_undocumented_functions_in_directory()
print(
    f"{total_functions-undocumented}/{total_functions} Functions are documented, that means {((total_functions-undocumented)/total_functions)*100}% of functions are documented and {undocumented} are still missing"
)
print()
# tge.function_utils.print_check_for_functions_in_module_with_missing_notations(tge)
# print("lines:", tge.tbe.count_lines_in_directory("./tge"))
dir = f"{os.getcwd()}/tge/"

for i in range(2):

    with open("tge/update.hashed", "w") as normal_file:
        normal_file.write(
            base64.b64encode(
                (
                    tge.file_operations.generate_uuid_from_directory(
                        dir, ["hashed", "pyc"]
                    ).bytes
                )
            ).decode()
        )


print()
directories: List[str] = []


for root, dirs, files in os.walk(dir, topdown=False):
    root = root[len(dir) :].lstrip("\\")
    for name in files:
        file = os.path.join(root, name).replace("\\", "/")
        if file.endswith(".py"):
            file = file[:-2]
        elif file.endswith(".pyc"):
            continue
        directories.append(file)


compressed = tge.file_operations._compress_path_list_to_dict(directories) #type: ignore

with open("directory.json", "w") as normal_file:  #
    compressed = json.dumps(compressed)
    for replacer, replacement in [('", "', '","'), ('": ', '":'), (', "', ',"')]:
        compressed = compressed.replace(replacer, replacement)
    normal_file.write(compressed)


cwd = os.getcwd()
output = rf"{cwd}/minified_tge"
try:
    os.remove(output)
except PermissionError:
    print(
        "Something is still using the minified tge folder, delete it manually or just leave it"
    )
except FileNotFoundError:
    ...


if tge.tbe.determine_affirmative(input("Minify?: ")):
    os.system("python generate_stubs.py -o stubs tge")
    for root, dirs, files in os.walk(dir, topdown=False):
        root = root
        for file in files:
            file_path = os.path.join(root[len(dir) :].lstrip("\\"), file)
            input_file_path = os.path.join(root, file)
            output_file_path = os.path.join(output, file_path)
            if file.endswith(".pyc"):
                continue
            if file.endswith(".hash"):
                with open(input_file_path, "rb") as normal_file:
                    with open(output_file_path, "wb") as minified_file:
                        data = normal_file.read()

                        minified_file.write(data)
                continue
            with open(input_file_path, "r+", encoding="utf8") as normal_file:

                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

                with open(output_file_path, "w", encoding="utf8") as minified_file:
                    data = (
                        tge.tbe.compress_imports_in_code(
                            tge.tbe.remove_unused_libraries(
                                "".join(
                                    [
                                        tge.string_utils.left_replace(line, "	", " ")
                                        for line in tge.tbe.minify(
                                            normal_file.read(),
                                            rename_globals=False,
                                            rename_locals=True,
                                            remove_docstrings=True,
                                        ).splitlines(keepends=True)
                                    ]
                                )
                            ).splitlines()
                        )
                        if input_file_path.endswith(".py")
                        else normal_file.read().splitlines()
                    )
                    if file.endswith(".py"):
                        if IGNORE:
                            data = ["#type: ignore"] + data
                        
                    minified_file.write("\n".join(data))
                


tge_size = tge.conversion.binary.convert_byte_to_kilobyte(
    tge.file_operations.get_file_size_of_directory("./tge", [".pyc"])
)
minified_size = tge.conversion.binary.convert_byte_to_kilobyte(
    tge.file_operations.get_file_size_of_directory("./minified_tge", [".pyc"])
)

if tge.library_utils.is_library_installed("minified_tge"):
    import minified_tge  # type: ignore
else:

    class minified_tge:
        INIT_TIME = 0


with open(".gitignore", "w") as normal_file:
    normal_file.write(
        "\n".join(
            [
                file[2:].replace("\\", "/")
                for file in tge.file_operations.find_files_with_extension(".", ".pyc")
            ]
        )
    )

print()
print("Import time of TGE:", tge.INIT_TIME)
print("Size of TGE: %s kb" % tge_size)
print("Import time of minified TGE:", minified_tge.INIT_TIME)
print("Size of minified TGE: %s kb" % minified_size)
print(
    "The minified TGE is %sx smaller"
    % str(tge_size / (minified_size if minified_size != 0 else tge_size))
)
print()

print("Is github version of tge up to date:", not tge.is_tge_outdated())
# the hash is smiling b'[\xa5d(\\!\xb7\xd0P&\xaf\xec(:>\xde'
