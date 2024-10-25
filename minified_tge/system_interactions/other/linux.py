import subprocess,os
def create_virtual_disk(drive_letter,folder_path,size_mb=100):B=folder_path;A=drive_letter;subprocess.run(['dd','if=/dev/zero',f"of={A}",'bs=1M',f"count={size_mb}"]);subprocess.run(['mkfs.ext4',A]);subprocess.run(['mkdir','-p',B]);subprocess.run(['sudo','mount','-o','loop',A,B])
def remove_virtual_disk(folder_path):subprocess.run(['sudo','umount',folder_path])
def add_to_path_to_system_path_variables(path):
 A='~/.bashrc'
 with open(os.path.expanduser(A),'a')as B:B.write(f'\nexport PATH="{path}:$PATH"\n')
 subprocess.run(['source',A],shell=True,check=True)