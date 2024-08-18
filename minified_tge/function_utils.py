_B='function_name'
_A='type'
import inspect
from types import FunctionType
from typing import get_type_hints
import importlib
def get_docstring(obj):
 try:return inspect.getdoc(obj)
 except:return''
def check_for_functions_in_module_with_missing_notations(library_module):
 functions_with_missing_annotations=[]
 for(name,obj)in inspect.getmembers(library_module):
  if isinstance(obj,FunctionType):
   input_parameters=get_function_inputs(obj);missing_input_types=[param for param in input_parameters if param[_A]is NoInputType];return_type=get_return_type(obj)
   if missing_input_types or return_type is MissingReturnType:functions_with_missing_annotations.append({_B:name,'missing_input_types':missing_input_types,'return_type':return_type})
 return functions_with_missing_annotations
def print_check_for_functions_in_module_with_missing_notations(library_module):
 data=check_for_functions_in_module_with_missing_notations(library_module)
 for i in data:print(f"Function '{i[_B]}' of type {'Missing Return'if i[_B]is MissingReturnType else'Missing Input type'}")
def get_return_type(func):
 signature=inspect.signature(func);return_type=signature.return_annotation
 if return_type==inspect.Signature.empty:return MissingReturnType
 else:return return_type
def get_function_inputs(func):
 B='default';A='name';signature=inspect.signature(func);type_hints=get_type_hints(func);input_parameters=[]
 for(param_name,param)in signature.parameters.items():
  param_type=type_hints.get(param_name,None)
  if param.default is not inspect.Parameter.empty:default_value=param.default;input_parameters.append({A:param_name,_A:param_type,B:default_value})
  else:input_parameters.append({A:param_name,_A:param_type,B:NoInputType})
 return input_parameters
def get_function_id_by_name(func_name):
 if func_name in globals():
  func_obj=globals()[func_name]
  if callable(func_obj):return func_obj
def count_functions_in_module(module,library_name):
 function_count=0
 for(name,obj)in inspect.getmembers(module):
  if inspect.isfunction(obj):function_count+=1
  elif inspect.ismodule(obj)and obj.__package__.startswith(library_name):function_count+=count_functions_in_module(obj,library_name)
 return function_count
def count_functions_in_library(library_name):
 try:module=importlib.import_module(library_name)
 except ModuleNotFoundError:return-1
 function_count=count_functions_in_module(module,library_name);return function_count
class NoInputType:0
class MissingReturnType:0