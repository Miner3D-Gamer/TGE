from types import MethodType
from typing import Any,Callable,TypeVar
__all__=['run_function_with_timeout','get_docstring','get_function_inputs','get_return_type','count_functions_in_library']
def get_docstring(obj:object)->str|None:...
def get_return_type(func:MethodType)->Any:...
def get_function_inputs(func:MethodType)->list[dict[str,Any]]:...
class UnknownInputType:...
def count_functions_in_library(library_name:str)->int:...
class NoInputType:...
class MissingReturnType:...
T=TypeVar('T')
def run_function_with_timeout(func:Callable[...,T],timeout:int|float,*args:Any,**kwargs:Any)->T|TimeoutError:...