import os, tempfile

temp_dir = tempfile.mktemp(prefix="tmp/tge")


python_installation = f"{os.getenv('LOCALAPPDATA')}\Programs\Python"
print(python_installation)

dirs = {f"{i.path}\Lib\site-packages" for i in os.scandir(python_installation) if os.path.exists(f"{i.path}\Lib\site-packages")}





