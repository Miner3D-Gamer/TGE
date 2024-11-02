#type: ignore
import os,subprocess
def create_virtual_drive(drive_letter,folder_path,size_mb=None):A=f"subst {drive_letter}: {folder_path}";subprocess.run(A,shell=True)
def remove_virtual_drive(drive_letter):A=f"subst {drive_letter}: /d";subprocess.run(A,shell=True)
def add_to_path_to_system_path_variables(path):A=os.getenv('PATH');B=f"{A};{path}";os.system(f'setx PATH "{B}"')