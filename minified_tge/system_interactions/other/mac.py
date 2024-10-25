_A='hdiutil'
import subprocess,os
def create_virtual_drive(drive_letter,folder_path,size_mb=100):A=drive_letter;subprocess.run([_A,'create','-size',f"{size_mb}m",'-fs','HFS+','-volname','VirtualDrive',A]);subprocess.run([_A,'attach',A,'-mountpoint',folder_path])
def remove_virtual_drive(folder_path):subprocess.run([_A,'detach',folder_path])
def add_to_path_to_system_path_variables(path):
 A='~/.bash_profile'
 with open(os.path.expanduser(A),'a')as B:B.write(f'\nexport PATH="{path}:$PATH"\n')
 subprocess.run(['source',A],shell=True,check=True)