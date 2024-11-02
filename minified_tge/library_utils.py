#type: ignore
import importlib.util,os,subprocess
_E='--version'
_D='python'
_C=False
_B='pip'
_A='install'
from.tbe import get_current_pip_path
___all__=['download_library','is_library_installed','install_missing_tge_libraries']
PIP_c=get_current_pip_path()
found=_C
def is_library_installed(library_name):A=importlib.util.find_spec(library_name);return A is not None
def download_library(library_name):
 C=True;A=library_name;global PIP_c,found
 if not found:
  if not PIP_c:PIP_c=[[_D,'-m',_B,_A,A],['python3','-m',_B,_A,A],[_B,_A,A],['pip3',_A,A]]
  else:PIP_c=[[PIP_c,_A,A]]
 E=None
 for D in PIP_c:
  try:
   F=subprocess.run(D,check=C,capture_output=C,text=C)
   if not found:found=C;PIP_c=[D]
   return C,F.stdout
  except subprocess.CalledProcessError as B:E=f"Failed to install {A} using command: {' '.join(D)}. Return code: {B.returncode}. Output: {B.output}. Error: {B.stderr}."
  except FileNotFoundError:continue
  except Exception as B:return _C,f"An unexpected error occurred: {str(B)}"
 return _C,f"All installation attempts failed. Last error: {E}"
def get_installed_python_versions():
 A=os.getenv('PATH')
 if A is None:return[]
 E=A.split(os.pathsep);D=[]
 for A in E:
  try:
   for B in os.listdir(A):
    if B.startswith(_D)and(B.endswith('.exe')or B.endswith('.bat')):
     C=os.path.join(A,B)
     if os.access(C,os.X_OK):
      try:
       F=subprocess.check_output([C,_E],stderr=subprocess.STDOUT).decode().strip()
       if'Python'in F:D.append(C)
      except subprocess.SubprocessError:continue
  except FileNotFoundError:continue
 return D
def install_library_from_github(github_repo_url):
 B=get_installed_python_versions()
 for A in B:
  print(f"Python executable: {A}")
  try:C=subprocess.check_output([A,_E],stderr=subprocess.STDOUT).decode().strip();print(f"Installing for {C} ({A})");subprocess.check_call([A,'-m',_B,_A,'git+'+github_repo_url])
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