_D='utf-8'
_C='/'
_B=True
_A=False
import os,shutil
from ast import parse as ast_parse,walk as ast_walk,FunctionDef as ast_FunctionDef
import zipfile,math,hashlib,uuid
from collections import defaultdict
import re
from tkinter import filedialog
def make_legal_filename(filename,replacer='_'):B='[\\\\/*?"<>|:]';A=re.sub(B,replacer,filename);A=A.strip();return A
def create_missing_directory(directory):
 A=directory
 if not os.path.exists(A):os.makedirs(A);return _B
 else:return _A
def delete_directory(directory):
 try:
  B=os.path.dirname(__file__);A=os.path.join(B,directory)
  if os.path.exists(A):shutil.rmtree(A);return _B,'Directory deleted'
  else:return _A,'Directory not found'
 except:return _A,'Error deleting directory'
def move_file(source_path,destination_path):shutil.move(source_path,destination_path)
def copy_file(source_path,destination_path):shutil.copy(source_path,destination_path)
def rename_file(source_path,name):A=source_path;B=os.path.dirname(A);C=os.path.join(B,name);os.rename(A,C)
def copy_directory(source_path,destination_path):A=destination_path;create_missing_directory(A);shutil.copytree(source_path,A)
def move_directory(source_path,destination_path):A=destination_path;create_missing_directory(A);shutil.move(source_path,A)
def rename_directory(source_path,name):A=source_path;B=os.path.dirname(A);C=os.path.join(B,name);os.rename(A,C)
def get_folder_name(path):
 A=path.replace('\\',_C)
 if os.path.isdir(path):return A.split(_C)[-1]
 else:B=A.split(_C)[-2];return B
def does_file_exist(directory):A=directory;return os.path.exists(A)and os.path.isfile(A)
def does_directory_exist(directory):A=directory;return os.path.exists(A)and os.path.isdir(A)
def delete_file(directory):os.remove(directory)
def compare_file(directory1,directory2):
 with open(directory1,'rb')as A,open(directory2,'rb')as B:return A.read()==B.read()
def are_directories_the_same(directory1,directory2,dir1_blacklist=[],dir2_blacklist=[]):return generate_uuid_from_directory(directory1,dir1_blacklist)==generate_uuid_from_directory(directory2,dir2_blacklist)
def count_files_in_directory(directory_path,extension_backlist=[]):
 A=0
 for(B,B,C)in os.walk(directory_path):
  for D in C:
   if D.endswith(tuple(extension_backlist)):continue
   A+=1
 return A
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
 else:return-1
def count_functions_in_file(file_path):
 try:
  with open(file_path,'r',encoding=_D)as B:C=ast_parse(B.read());A=[A.name for A in ast_walk(C)if isinstance(A,ast_FunctionDef)];return len(A),A
 except:return 0,[]
def count_functions_in_directory(directory_path):
 C={};D=0;E=[]
 for(G,K,H)in os.walk(directory_path):
  for F in H:
   if F.endswith('.py'):
    A=os.path.join(G,F)
    try:
     with open(A,'r',encoding=_D)as I:J=ast_parse(I.read());B=[A.name for A in ast_walk(J)if isinstance(A,ast_FunctionDef)];C[A]=len(B),B;D+=len(B)
    except IOError:E.append(A)
 return D,C,E
def count_function_names_in_directory(directory_path):
 A,C,A=count_functions_in_directory(directory_path);B=[]
 for(A,(A,D))in C.items():
  for E in D:B.append(E)
 return len(B),B
def save_counted_function_names_from_directory(directory_path,file_name,output_path,create_missing_directory_bool):
 C=file_name;B=output_path;A=directory_path;D=count_function_names_in_directory(A)[1]
 if A=='':A=get_current_working_directory()
 if B=='':B=A
 if C=='':C='functions.txt'
 if create_missing_directory_bool:create_missing_directory(B)
 try:
  with open(B+C,'w',encoding=_D)as E:
   for F in D:E.write(F+'\n')
  return _B
 except:return _A
def input_file_path(extension=None):return filedialog.asksaveasfilename(defaultextension=extension)
def ask_for_directory_path():A=filedialog.askdirectory();return A
def unzip_file(zip_path,extract_dir,create_missing_directory_bool=_A):
 C=create_missing_directory_bool;B=zip_path;A=extract_dir
 if B=='':return _A,_A
 if A=='':return _A,_A
 D=_A
 try:
  if C:D=create_missing_directory(A)
  with zipfile.ZipFile(B,'r')as E:E.extractall(A)
  return _B,_B
 except:
  if C:
   if D:delete_directory(A)
  return _A,_B
def zip_directory(directory_path,output_path,create_missing_directory_bool=_A):
 D='.zip';B=directory_path;A=output_path
 if B=='':return _A,_A
 if A=='':return _A,_A
 if not A.endswith(D):A+=D
 try:
  if create_missing_directory_bool:create_missing_directory(A)
  with zipfile.ZipFile(A,'w',zipfile.ZIP_DEFLATED)as E:
   for(F,I,G)in os.walk(B):
    for H in G:C=os.path.join(F,H);E.write(C,os.path.relpath(C,B))
  return _B,_B
 except:return _A,_B
def get_appdata_path():return os.path.expanduser('~\\AppData')
def get_latest_file_in_directory_from_all_filenames_that_are_real_numbers(path):
 E=os.listdir(path);B=-1;C=None
 for A in E:
  if os.path.isfile(os.path.join(path,A)):
   F,G=os.path.splitext(A)
   try:
    D=int(F)
    if D>B:B=D;C=A
   except ValueError:continue
 return C
def is_directory_empty(directory_path):return not os.listdir(directory_path)
def get_filesize(file_path):return os.path.getsize(file_path)
def get_file_size_of_directory(directory,blacklisted_file_extensions=[],chunk_size=4096):
 A=chunk_size;B=0
 for(E,I,F)in os.walk(directory):
  for C in F:
   if any(C.endswith(A)for A in blacklisted_file_extensions):continue
   D=os.path.join(E,C)
   if not os.path.islink(D):G=os.path.getsize(D);H=math.ceil(G/A)*A;B+=H
 return B
def generate_uuid_from_directory(directory,blacklisted_extensions=[]):
 A=hashlib.md5()
 for(E,L,F)in os.walk(directory):
  for B in sorted(F):
   C=_B
   for G in blacklisted_extensions:
    if B.endswith(G):break
   else:C=_A
   if C:continue
   D=os.path.join(E,B)
   if os.path.isfile(D):
    with open(D,'rb')as H:
     for I in iter(lambda:H.read(4096),b''):A.update(I)
 J=A.hexdigest();K=uuid.UUID(J[:32]);return K
class _compress_directory_list_trie_node:
 def __init__(A):A.children=defaultdict(_compress_directory_list_trie_node);A.is_end_of_path=_A
def _compress_directory_list_insert_path(root,path):
 A=root
 for B in path:A=A.children[B]
 A.is_end_of_path=_B
def _compress_directory_list_build_trie(paths):
 A=_compress_directory_list_trie_node()
 for B in paths:_compress_directory_list_insert_path(A,B.split(_C))
 return A
def _compress_directory_list_serialize_trie(node):
 C=node
 if not C.children:return{}
 if len(C.children)==1 and C.is_end_of_path==_A:
  B,D=next(iter(C.children.items()));A=_compress_directory_list_serialize_trie(D)
  if isinstance(A,list)and not A:return B
  if isinstance(A,str):return f"{B}/{A}"
  return{B:A}
 E={}
 for(B,D)in C.children.items():
  A=_compress_directory_list_serialize_trie(D)
  if isinstance(A,list)and not A:E.setdefault('files',[]).append(B)
  else:E[B]=A
 return E
def find_files_with_extension(root_dir,file_extension):
 A=[]
 for(C,E,D)in os.walk(root_dir):
  for B in D:
   if B.endswith(file_extension):A.append(os.path.join(C,B))
 return A
def compress_directory_list(paths):A=_compress_directory_list_build_trie(paths);B=_compress_directory_list_serialize_trie(A);return B
def decompress_directory_list(compressed):
 B=[]
 def D(node,current_path=''):
  C=current_path;A=node
  if isinstance(A,list):B.append(f"{C}/{A[0]}".strip(_C));return
  if isinstance(A,str):B.append(A);return
  for(E,F)in A.items():
   if E=='files':
    for G in F:B.append(f"{C}/{G}".strip(_C))
   else:D(F,f"{C}/{E}".strip(_C))
 D(compressed);return B
def find_files_with_extensions(root_dir,file_extensions):
 A=[]
 for B in file_extensions:A.extend(find_files_with_extension(root_dir,B))
 return A