#type: ignore
from typing import get_type_hints
from concurrent import futures
import functools,importlib,inspect,os
_A=None
__all__=['run_function_with_timeout','get_docstring','get_function_inputs','get_return_type','count_functions_in_library']
def get_docstring(obj):
 try:return inspect.getdoc(obj)
 except:return''
def get_return_type(func):
 signature=inspect.signature(func);return_type=signature.return_annotation
 if return_type==inspect.Signature.empty:return MissingReturnType
 else:return return_type
def get_function_inputs(func):
 C='default';B='type';A='name';signature=inspect.signature(func)
 try:type_hints=get_type_hints(func)
 except TypeError:return[{A:_A,B:UnknownInputType,C:NoInputType}]
 input_parameters=[]
 for(param_name,param)in signature.parameters.items():
  param_type=type_hints.get(param_name,_A)
  if param.default is not inspect.Parameter.empty:default_value=param.default;input_parameters.append({A:param_name,B:param_type,C:default_value})
  else:print(param,param_name);quit();input_parameters.append({A:param_name,B:param_type,C:NoInputType})
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
  if thing is _A:continue
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
 with futures.ThreadPoolExecutor()as executor:
  future=executor.submit(func,*args,**kwargs)
  try:return future.result(timeout=timeout)
  except futures.TimeoutError:return TimeoutResult
def lazy_load(func_loader):
 func=_A
 @functools.wraps(func_loader)
 def wrapper(*args,**kwargs):
  nonlocal func
  if func is _A:func=func_loader()
  return func(*args,**kwargs)
 return wrapper