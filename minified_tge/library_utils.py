_D='--version'
_C='python'
_B='pip'
_A='install'
import importlib.util
import subprocess
import os
from.tbe import get_current_pip_path
def is_library_installed(library_name):A=importlib.util.find_spec(library_name);return A is not None
def download_library(library_name):
 F=False;D=True;A=library_name;B=get_current_pip_path()
 if not B:B=[[_C,'-m',_B,_A,A],['python3','-m',_B,_A,A],[_B,_A,A],['pip3',_A,A]]
 else:B=[B,_A,A]
 for E in B:
  try:G=subprocess.run(E,check=D,capture_output=D,text=D);return D,G.stdout
  except subprocess.CalledProcessError as C:H=f"Failed to install {A} using command: {' '.join(E)}. Return code: {C.returncode}. Output: {C.output}. Error: {C.stderr}."
  except FileNotFoundError:continue
  except Exception as C:return F,f"An unexpected error occurred: {str(C)}"
 return F,f"All installation attempts failed. Last error: {H}"
def get_installed_python_versions():
 A=os.getenv('PATH')
 if A is None:return[]
 E=A.split(os.pathsep);D=[]
 for A in E:
  try:
   for B in os.listdir(A):
    if B.startswith(_C)and(B.endswith('.exe')or B.endswith('.bat')):
     C=os.path.join(A,B)
     if os.access(C,os.X_OK):
      try:
       F=subprocess.check_output([C,_D],stderr=subprocess.STDOUT).decode().strip()
       if'Python'in F:D.append(C)
      except subprocess.SubprocessError:continue
  except FileNotFoundError:continue
 return D
def install_library_from_github(github_repo_url):
 B=get_installed_python_versions()
 for A in B:
  print(f"Python executable: {A}")
  try:C=subprocess.check_output([A,_D],stderr=subprocess.STDOUT).decode().strip();print(f"Installing for {C} ({A})");subprocess.check_call([A,'-m',_B,_A,'git+'+github_repo_url])
  except subprocess.CalledProcessError as D:print(f"Failed to install for {A}: {D}")
def install_all_libraries(libs):
 A=[]
 for B in libs:
  if is_library_installed(B):continue
  A.append(download_library(B))
 return A
def install_missing_tge_libraries():
 with open(os.path.dirname(__file__)+'/requirements.txt','r')as B:C=B.readlines()
 for A in C:
  if not is_library_installed(A.strip()):download_library(A.strip())