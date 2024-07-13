_C='--version'
_B='install'
_A='python'
import importlib.util
from typing import List,Union,Tuple,Any,Optional,Dict
import subprocess
def is_library_installed(library_name):'\n    Tests for the accessability of a library using a custom mini \n    version of "import_lib" mostly only using the essential \n    functions needed for existence a library.\n    ';A=importlib.util.find_spec(library_name);return A is not None
def download_library(library_name):
	'\n    Downloads and installs a Python library using pip.\n\n    Parameters:\n        library_name (str): The name of the library to be installed.\n\n    Returns:\n        tuple: A tuple containing a boolean indicating whether the installation was successful\n        and a message string providing additional information in case of an error.\n    ';D=False;C=library_name;B=True;E=[_A,'-m','pip',_B,C]
	try:F=subprocess.run(E,check=B,capture_output=B,text=B);return B,F.stdout
	except subprocess.CalledProcessError as A:G=f"Failed to install {C}. Return code: {A.returncode}. Output: {A.output}. Error: {A.stderr}.";return D,G
	except Exception as A:return D,f"An unexpected error occurred: {str(A)}"
import os
def get_installed_python_versions():
	'Get a list of installed Python executables in the system PATH.';E=os.getenv('PATH').split(os.pathsep);C=[]
	for D in E:
		try:
			for A in os.listdir(D):
				if A.startswith(_A)and(A.endswith('.exe')or A.endswith('.bat')):
					B=os.path.join(D,A)
					if os.access(B,os.X_OK):
						try:
							F=subprocess.check_output([B,_C],stderr=subprocess.STDOUT).decode().strip()
							if'Python'in F:C.append(B)
						except subprocess.SubprocessError:continue
		except FileNotFoundError:continue
	return C
def install_library_from_github(github_repo_url):
	'Install the library from the given GitHub repository URL to all installed Python versions.';B=get_installed_python_versions()
	for A in B:
		print(f"Python executable: {A}")
		try:C=subprocess.check_output([A,_C],stderr=subprocess.STDOUT).decode().strip();print(f"Installing for {C} ({A})");subprocess.check_call([A,'-m','pip',_B,'git+'+github_repo_url])
		except subprocess.CalledProcessError as D:print(f"Failed to install for {A}: {D}")
def install_all_libraries(libs):
	A=[]
	for B in libs:
		if is_library_installed(B):continue
		A.append(download_library(B))
	return A
def are_all_required_libraries_installed():
	with open('requirements.txt','r')as B:C=B.readlines()
	for A in C:
		if not is_library_installed(A):ModuleNotFoundError(A)