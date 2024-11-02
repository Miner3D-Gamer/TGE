#type: ignore
from ast import parse as ast_parse,walk as ast_walk,FunctionDef as ast_FunctionDef
from typing import Union, List
from tkinter import filedialog
import hashlib,json,math,os,re,shutil,uuid,zipfile
_C='utf-8'
_B=True
_A=False
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
 A=path.replace('\\','/')
 if os.path.isdir(path):return A.split('/')[-1]
 else:B=A.split('/')[-2];return B
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
  with open(file_path,'r',encoding=_C)as B:C=ast_parse(B.read());A=[A.name for A in ast_walk(C)if isinstance(A,ast_FunctionDef)];return len(A),A
 except:return 0,[]
def count_functions_in_directory(directory_path):
 C={};D=0;E=[]
 for(G,K,H)in os.walk(directory_path):
  for F in H:
   if F.endswith('.py'):
    A=os.path.join(G,F)
    try:
     with open(A,'r',encoding=_C)as I:J=ast_parse(I.read());B=[A.name for A in ast_walk(J)if isinstance(A,ast_FunctionDef)];C[A]=len(B),B;D+=len(B)
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
  with open(B+C,'w',encoding=_C)as E:
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
def find_files_with_extension(root_dir,file_extension):
 A=[]
 for(C,E,D)in os.walk(root_dir):
  for B in D:
   if B.endswith(file_extension):A.append(os.path.join(C,B))
 return A
def find_files_with_extensions(root_dir,file_extensions):
 A=[]
 for B in file_extensions:A.extend(find_files_with_extension(root_dir,B))
 return A
NestedList=List[Union[(str,'NestedList')]]
def _compress_path_list_to_dict(paths):
 A='d';C='f';D={C:[],A:{}}
 for H in paths:
  G=H.split('/');B=D
  for E in G[:-1]:
   if A not in B:B[A]={}
   if E not in B[A]:B[A][E]={}
   B=B[A][E]
  if C not in B:B[C]=[]
  B[C].append(G[-1])
 def F(data):
  B=data
  if A in B:
   G=[]
   for(D,E)in B[A].items():
    F(E)
    if len(E[C])==1 and not E.get(A):
     if not C in B:B[C]=[]
     B[C].append(f"{D}/{E[C][0]}");G.append(D)
   for D in G:del B[A][D]
   if not B[A]:del B[A]
  if A in B and not B[A]:del B[A]
  else:
   for D in B.get(A,{}):F(B[A][D])
 F(D);return D
def _format_dict_file_paths_to_array(compressed):
 def E(data):
  B=data;A=[];C=B.get('f',[])
  if'd'in B:
   for(F,G)in B['d'].items():
    D=E(G)
    if len(D)==1:A.append([F,D[0]])
    else:A.append([F,D])
  return A if not C else[A,C]if A else C
 def B(data):
  A=data
  if isinstance(A,list):
   if len(A)==1:return B(A[0])
   else:return[B(A)for A in A]
  return A
 return B(E(compressed))
def _decompress_file_path_dict(data,current_path=''):
 C=current_path;A=data;B=[];D='d';E='f'
 if E in A:
  for F in A[E]:B.append(C+F)
 if D in A:
  for(G,H)in A[D].items():B.extend(_decompress_file_path_dict(H,C+G+'/'))
 return B
def _decompress_file_path_list(data,current=''):
 H='Expected strings but got %s';D=current;A=data;B=[]
 def G(data):
  dir=[]
  for A in data:
   if not isinstance(A,list):raise ValueError('Expected lists but got %s'%type(A))
   dir.extend(F(A))
  return dir
 def F(data):
  A=data;nonlocal D;dir=[]
  if isinstance(A,str):raise ValueError('Expected list but got %s'%type(A[0]))
  dir.extend(_decompress_file_path_list(A[1],E(A[0])));return dir
 E=lambda path:D+'/'+path if D else path;I=len(A)
 if I==2:
  if isinstance(A[0],list):
   if len(A[0])==2:
    if isinstance(A[0][0],list):B.extend(G(A[0]))
    else:B.extend(F(A[0]))
   else:B.extend(G(A[0]))
  elif isinstance(A[1],list):D=E(A[0]);B.extend(F(A[1]))
  else:
   for C in A:
    if not isinstance(C,str):raise ValueError(H%type(C))
    B.append(E(C))
 else:
  for C in A:
   if not isinstance(C,str):raise ValueError(H%type(C))
   B.append(E(C))
 return B
def decompress_file_paths(data):
 A=data
 if isinstance(A,list):return _decompress_file_path_list(A)
 else:return _decompress_file_path_dict(A)
def compress_file_paths(paths):
 A=_compress_path_list_to_dict(paths);B=_format_dict_file_paths_to_array(A)
 if len(object_to_optimal_string(A))>len(object_to_optimal_string(B)):return B
 return A
def object_to_optimal_string(data):
 A=json.dumps(data)
 for(B,C)in[('", "','","'),('": ','":'),(', "',',"')]:A=A.replace(B,C)
 return A
__all__=['make_legal_filename','create_missing_directory','delete_directory','move_file','copy_file','rename_file','copy_directory','move_directory','rename_directory','get_folder_name','does_file_exist','does_directory_exist','delete_file','compare_file','are_directories_the_same','count_files_in_directory','count_items_in_directory','get_current_working_directory','get_file_extension','find_files_by_extension','get_file_size','get_file_creation_time','count_functions_in_file','count_functions_in_directory','count_function_names_in_directory','save_counted_function_names_from_directory','input_file_path','ask_for_directory_path','unzip_file','zip_directory','get_appdata_path','get_latest_file_in_directory_from_all_filenames_that_are_real_numbers','is_directory_empty','get_filesize','get_file_size_of_directory','generate_uuid_from_directory','find_files_with_extension','find_files_with_extensions','decompress_file_paths','compress_file_paths','object_to_optimal_string']