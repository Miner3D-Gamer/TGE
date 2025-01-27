#type: ignore
import importlib.util,os,subprocess
_E='--version'
_D='python'
_C='pip'
_B=None
_A='install'
from.tbe import get_current_pip_path
__all__=['install_library','is_library_installed','install_missing_tge_libraries']
def is_library_installed(library_name):A=importlib.util.find_spec(library_name);return A is not _B
def install_library(library_name,pip_path=get_current_pip_path(),tried_commands=_B):
 H=False;E=pip_path;D=tried_commands;C=True;A=library_name
 if D is _B:D=[[E,_A,A]]if E else[[_D,'-m',_C,_A,A],['python3','-m',_C,_A,A],[_C,_A,A],['pip3',_A,A]]
 F=_B
 for G in D:
  try:I=subprocess.run(G,check=C,capture_output=C,text=C);return C,I.stdout
  except subprocess.CalledProcessError as B:F=f"Failed to install {A} using command: {' '.join(G)}. Return code: {B.returncode}. Output: {B.output.strip()}. Error: {B.stderr.strip()}."
  except FileNotFoundError:continue
  except Exception as B:return H,f"An unexpected error occurred: {str(B)}"
 return H,f"All installation attempts failed. Last error: {F}"
def get_installed_python_versions():
 A=os.getenv('PATH')
 if A is _B:return[]
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
  try:C=subprocess.check_output([A,_E],stderr=subprocess.STDOUT).decode().strip();print(f"Installing for {C} ({A})");subprocess.check_call([A,'-m',_C,_A,'git+'+github_repo_url])
  except subprocess.CalledProcessError as D:print(f"Failed to install for {A}: {D}")
def install_all_libraries(libs):
 A=[]
 for B in libs:
  if is_library_installed(B):continue
  A.append(install_library(B))
 return A
def install_missing_tge_libraries():
 with open(os.path.dirname(__file__)+'/requirements.txt','r')as B:C=B.readlines()
 for A in C:
  if not is_library_installed(A.strip()):install_library(A.strip())