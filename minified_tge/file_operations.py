_C='utf-8'
_B=True
_A=False
import os,shutil
from filecmp import dircmp as file_dircmp,cmp as file_cmp
from ast import parse as ast_parse,walk as ast_walk,FunctionDef as ast_FunctionDef
import zipfile
from pathlib import Path as pathlib_path
from typing import List,Union,Tuple,Any
import tkinter as tk,pyshortcuts
from.codec.codec import decode,base
def create_missing_directory(directory):
	A=directory
	if not os.path.exists(A):os.makedirs(A);return _B
	else:return _A
def delete_directory(directory):
	try:
		B=pathlib_path(__file__).resolve().parent;A=os.path.join(B,directory)
		if os.path.exists(A):shutil.rmtree(A);return _B,'Directory deleted'
		else:return _A,'Directory not found'
	except:return _A,'Error deleting directory'
def write_save_data(name,dir,data):
	A=name
	try:
		A=A.replace('.save','');B=os.path.join(dir,f"{A}.save")
		with open(B,'w')as C:C.write(data);return _B,'File saved'
	except Exception as D:return _A,f"Error saving file: {str(D)}"
def load_save_data(name,dir):
	A=name
	try:
		A=A.rstrip('.save','');B=os.path.join(dir,f"{A}.save")
		if os.path.exists(B):
			with open(B,'rb')as D:
				E=D.read();F,C=decode(E)
				if F:return _B,C
				else:return _A,C
		else:return _A,'File not found'
	except Exception as G:return _A,f"Error loading file: {str(G)}"
def move_file(source_path,destination_path):
	B=destination_path;A=source_path
	if doesDirectoryFileExist(A):create_missing_directory(B);shutil.move(A,B);return _B
	else:return _A
def copy_file(source_path,destination_path):
	B=destination_path;A=source_path
	try:
		if doesDirectoryFileExist(A):create_missing_directory(B);shutil.copy(A,B);return _B
		else:return _A
	except:return _A
def rename_file(source_path,name):
	A=source_path
	try:
		if doesDirectoryFileExist(A):B=os.path.dirname(A);C=os.path.join(B,name);os.rename(A,C);return _B
		else:return _A
	except:return _A
def copy_directory(source_path,destination_path):
	B=destination_path;A=source_path
	try:
		if doesDirectoryFileExist(A):create_missing_directory(B);shutil.copytree(A,B);return _B
		else:return _A
	except:return _A
def move_directory(source_path,destination_path):
	B=destination_path;A=source_path
	try:
		if doesDirectoryFileExist(A):create_missing_directory(B);shutil.move(A,B);return _B
		else:return _A
	except:return _A
def rename_directory(source_path,name):
	A=source_path
	try:
		if doesDirectoryFileExist(A):B=os.path.dirname(A);C=os.path.join(B,name);os.rename(A,C);return _B
		else:return _A
	except:return _A
def get_parent_path(path):return os.path.dirname(path)
def get_parent_folder(path):
	A='/';B=path.replace('\\',A)
	if os.path.isdir(path):return B.split(A)[-1]
	else:C=B.split(A)[-2];return C
def combine_files(directory,output_directory,name):
	D=directory
	try:
		E=[]
		for A in os.listdir(D):
			F=os.path.join(D,A)
			if os.path.isfile(F):
				with open(F,'rb')as B:C=B.read();E.append((A,C))
		G=b''
		for(A,C)in E:G+=A.encode()+b':'+C+b'|'
		H=base.encode_base64(G);I=os.path.join(output_directory,name+'.encrypted')
		with open(I,'wb')as B:B.write(H)
		return _B
	except:return _A
def split_file(directory,output_directory):
	try:
		with open(directory,'rb')as A:B=A.read()
		C=base.decode_base64(B);D=C.split(b'|')[:-1]
		for E in D:
			F,G=E.split(b':',1);H=os.path.join(output_directory,F.decode())
			with open(H,'wb')as A:A.write(G)
		return _B
	except:return _A
def doesDirectoryFileExist(is_file,directory):
	A=directory
	if is_file:
		if os.path.isfile(f"{pathlib_path(__file__).resolve().parent}/{A}")or os.path.isfile(A):return _B
		else:return _A
	elif os.path.exists(f"{pathlib_path(__file__).resolve().parent}/{A}")or os.path.exists(A):return _B
	else:return _A
def doesFileExist(directory):A=directory;return os.path.exists(A)and os.path.isfile(A)
def doesDirectoryExist(directory):A=directory;return os.path.exists(A)and os.path.isdir(A)
def delete_file(name,dir):
	if os.path.isfile(f"{pathlib_path(__file__).resolve().parent}/{dir}/{name}"):os.system(f"rm {f'{pathlib_path(__file__).resolve().parent}/{dir}/{name}'}");return _B
	else:return _A
def compare_file(directory1,directory2):
	try:
		with open(directory1,'r')as A,open(directory2,'r')as B:return A.read()==B.read(),_B
	except:return _A,_A
def compare_directory(directory1,directory2):
	B=directory2;A=directory1
	try:
		C=file_dircmp(A,B)
		for D in C.common_files:
			F=os.path.join(A,D);G=os.path.join(B,D)
			if not file_cmp(F,G):return _A
		for E in C.subdirs.values():
			if not compare_directory(os.path.join(A,E.left),os.path.join(B,E.right)):return _A
		return _B,'Files are compared successfully'
	except OSError as H:return _A,'Error: '+str(H)
def count_items_in_directory(directory_path):return len(os.listdir(directory_path))
def get_current_working_directory():
	try:return os.getcwd()
	except:return''
def get_file_extension(file_path):return os.path.splitext(file_path)[1][1:]
def find_files_by_extension(directory_path,extension):
	A=[]
	for B in os.listdir(directory_path):
		D,C=os.path.splitext(B)
		if C==extension:A.append(B)
	return A
def get_file_size(file_path):
	A=file_path
	if os.path.isfile(A):return os.path.getsize(A)
	else:return 0
def get_file_creation_time(file_path):
	A=file_path
	if os.path.isfile(A):return os.path.getctime(A)
	else:return''
def count_functions_in_file(file_path):
	try:
		with open(file_path,'r',encoding=_C)as B:C=ast_parse(B.read());A=[A.name for A in ast_walk(C)if isinstance(A,ast_FunctionDef)];return len(A),A
	except:return 0,[]
def count_functions_in_directory(directory_path):
	D={};E=0;F=[]
	for(G,J,H)in os.walk(directory_path):
		for A in H:
			if A.endswith('.py'):
				B=os.path.join(G,A)
				try:
					with open(B,'r',encoding=_C)as A:I=ast_parse(A.read());C=[A.name for A in ast_walk(I)if isinstance(A,ast_FunctionDef)];D[B]=len(C),C;E+=len(C)
				except IOError:F.append(B)
	return E,D,F
def count_function_names_in_directory(directory_path):
	E,B,F=count_functions_in_directory(directory_path);A=[]
	for(G,(H,C))in B.items():
		for D in C:A.append(D)
	return len(A),A
def save_counted_function_names_from_directory(directory_path,file_name,output_path,create_missing_directory_bool):
	C=file_name;B=output_path;A=directory_path;D=count_function_names_in_directory(A)[1]
	if A=='':A=get_current_working_directory()
	if B=='':B=A
	if C=='':C='functions.txt'
	if create_missing_directory_bool:create_missing_directory(B)
	try:
		with open(B+C,'w',encoding=_C)as E:
			for F in D:E.write(F+'\n')
		return _B
	except:return _A
def input_file_path(extension=None):return tk.filedialog.asksaveasfilename(defaultextension=extension)
def input_directory_path():A=tk.filedialog.askdirectory();return A
def unzip_file(zip_path,extract_dir,create_missing_directory_bool=_A):
	C=create_missing_directory_bool;B=zip_path;A=extract_dir
	if B=='':return _A,_A
	if A=='':return _A,_A
	try:
		if C:D=create_missing_directory(A)
		with zipfile.ZipFile(B,'r')as E:E.extractall(A)
		return _B,_B
	except:
		if C:
			if D:delete_directory(A)
		return _A,_B
def zip_directory(directory_path,output_path,create_missing_directory_bool=_A):
	E='.zip';B=directory_path;A=output_path
	if B=='':return _A,_A
	if A=='':return _A,_A
	if not A.endswith(E):A+=E
	try:
		if create_missing_directory_bool:create_missing_directory(A)
		with C.ZipFile(A,'w',C.ZIP_DEFLATED)as C:
			for(F,I,G)in os.walk(B):
				for H in G:D=os.path.join(F,H);C.write(D,os.path.relpath(D,B))
		return _B,_B
	except:return _A,_B
def get_appdata_path():return os.path.expanduser('~\\AppData')
def create_shortcut(name,target_path,shortcut_path,description=''):A=target_path;B=os.path.dirname(A);pyshortcuts.make_shortcut(name=name,script=A,working_dir=B,folder=shortcut_path,description=description,executable=A)
def get_latest_file_in_directory_from_all_filenames_that_are_real_numbers(path):
	E=os.listdir(path);C=-1;A=None
	for B in E:
		if os.path.isfile(os.path.join(path,B)):
			F,G=os.path.splitext(B)
			try:
				D=int(F)
				if D>C:C=D;A=B
			except ValueError:continue
	if A is not None:return A
	else:return
def is_directory_empty(directory_path):return not os.listdir(directory_path)