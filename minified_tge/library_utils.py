_D='--version'
_C='python'
_B='pip'
_A='install'
import importlib.util
import subprocess
import os
def is_library_installed(library_name):A=importlib.util.find_spec(library_name);return A is not None
def download_library(library_name):
 E=False;C=True;A=library_name;F=[[_C,'-m',_B,_A,A],['python3','-m',_B,_A,A],[_B,_A,A],['pip3',_A,A]]
 for D in F:
  try:G=subprocess.run(D,check=C,capture_output=C,text=C);return C,G.stdout
  except subprocess.CalledProcessError as B:H=f"Failed to install {A} using command: {' '.join(D)}. Return code: {B.returncode}. Output: {B.output}. Error: {B.stderr}."
  except FileNotFoundError:continue
  except Exception as B:return E,f"An unexpected error occurred: {str(B)}"
 return E,f"All installation attempts failed. Last error: {H}"
def get_installed_python_versions():
 E=os.getenv('PATH').split(os.pathsep);C=[]
 for D in E:
  try:
   for A in os.listdir(D):
    if A.startswith(_C)and(A.endswith('.exe')or A.endswith('.bat')):
     B=os.path.join(D,A)
     if os.access(B,os.X_OK):
      try:
       F=subprocess.check_output([B,_D],stderr=subprocess.STDOUT).decode().strip()
       if'Python'in F:C.append(B)
      except subprocess.SubprocessError:continue
  except FileNotFoundError:continue
 return C
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
  if not is_library_installed(A.strip()):raise ModuleNotFoundError(f"Library not found: {A.strip()}")