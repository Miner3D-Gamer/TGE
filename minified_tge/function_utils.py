#type: ignore
from types import ModuleType
from typing import get_type_hints
import concurrent,importlib,inspect,os
_B='function_name'
_A='type'
__all__=['run_function_with_timeout','get_docstring','check_for_functions_in_module_with_missing_notations','print_check_for_functions_in_module_with_missing_notations','get_function_inputs','get_return_type']
def get_docstring(obj):
 try:return inspect.getdoc(obj)
 except:return''
def check_for_functions_in_module_with_missing_notations(library_module):
 raise Exception("This function is broken, I'm just done with the bs this function caused me");functions_with_missing_annotations=[]
 for(name,obj)in inspect.getmembers(library_module):
  if isinstance(obj,FunctionType):
   input_parameters=get_function_inputs(obj);missing_input_types=[param for param in input_parameters if param[_A]is NoInputType];return_type=get_return_type(obj)
   if missing_input_types or return_type is MissingReturnType:functions_with_missing_annotations.append({'file':library_module.__file__,_B:name,'missing_input_types':missing_input_types,'return_type':return_type})
  elif isinstance(obj,ModuleType):
   if obj.__name__.startswith(library_module.__name__):functions_with_missing_annotations.extend(check_for_functions_in_module_with_missing_notations(obj))
 return functions_with_missing_annotations
def print_check_for_functions_in_module_with_missing_notations(library_module):
 data=check_for_functions_in_module_with_missing_notations(library_module)
 for i in data:print(f"\nIn File '{i['file']}' Function '{i[_B]}'",i)
def get_return_type(func):
 signature=inspect.signature(func);return_type=signature.return_annotation
 if return_type==inspect.Signature.empty:return MissingReturnType
 else:return return_type
def get_function_inputs(func):
 B='default';A='name';signature=inspect.signature(func)
 try:type_hints=get_type_hints(func)
 except TypeError:return[{A:None,_A:UnknownInputType,B:NoInputType}]
 input_parameters=[]
 for(param_name,param)in signature.parameters.items():
  param_type=type_hints.get(param_name,None)
  if param.default is not inspect.Parameter.empty:default_value=param.default;input_parameters.append({A:param_name,_A:param_type,B:default_value})
  else:print(param,param_name);quit();input_parameters.append({A:param_name,_A:param_type,B:NoInputType})
 return input_parameters
class UnknownInputType:...
def get_function_id_by_name(func_name):
 if func_name in globals():
  func_obj=globals()[func_name]
  if callable(func_obj):return func_obj
def count_functions_in_module(module,library_name):
 function_count=0
 for(_,obj)in inspect.getmembers(module):
  if inspect.isfunction(obj):function_count+=1;continue
  if not inspect.ismodule(obj):continue
  thing=obj.__package__
  if thing is None:continue
  if thing.startswith(library_name):function_count+=count_functions_in_module(obj,library_name)
 return function_count
def count_functions_in_library(library_name):
 try:module=importlib.import_module(library_name)
 except ModuleNotFoundError:return-1
 function_count=count_functions_in_module(module,library_name);return function_count
class NoInputType:0
class MissingReturnType:0
def restrict_to_directory(allowed_dir):
 def decorator(func):
  def wrapper(file_path,*args,**kwargs):
   real_allowed_dir=os.path.realpath(allowed_dir);real_file_path=os.path.realpath(file_path)
   if not real_file_path.startswith(real_allowed_dir):raise PermissionError(f"Access denied: {file_path} is outside the allowed directory")
   return func(file_path,*args,**kwargs)
  return wrapper
 return decorator
class TimeoutResult:...
def run_function_with_timeout(func,timeout,*args,**kwargs):
 with concurrent.futures.ThreadPoolExecutor()as executor:
  future=executor.submit(func,*args,**kwargs)
  try:return future.result(timeout=timeout)
  except concurrent.futures.TimeoutError:return TimeoutResult