import inspect
from types import FunctionType, ModuleType, MethodType
from typing import Any, List, get_type_hints, Union
import importlib
import os

def get_docstring(obj: object) -> str:
    """
    Retrieve the docstring of a given object.

    This function attempts to extract and return the docstring of the provided object.

    Args:
        obj (object): The object for which the docstring is to be retrieved.

    Returns:
        str: The docstring of the object if available, otherwise an empty string.
    """
    try:
        return inspect.getdoc(obj)
    except:
        return ""


def check_for_functions_in_module_with_missing_notations(
    library_module: ModuleType,
) -> List[dict]:
    """
    Check all functions in a given library module for missing input type or return type annotations.
    Parameters:
    library_module (module): The library module to analyze.
    Returns:
    list: A list of dictionaries containing information about functions with missing type annotations.
    """
    functions_with_missing_annotations = []

    for name, obj in inspect.getmembers(library_module):
        if isinstance(obj, FunctionType):
            input_parameters = get_function_inputs(obj)
            missing_input_types = [
                param for param in input_parameters if param["type"] is NoInputType
            ]

            return_type = get_return_type(obj)
            if missing_input_types or return_type is MissingReturnType:
                functions_with_missing_annotations.append(
                    {
                        "function_name": name,
                        "missing_input_types": missing_input_types,
                        "return_type": return_type,
                    }
                )

    return functions_with_missing_annotations


def print_check_for_functions_in_module_with_missing_notations(
    library_module: ModuleType,
) -> None:
    """Print details of functions in a module that are missing type annotations.

    Args:
        library_module (ModuleType): The module to check for missing type annotations.

    Details:
        Prints each function with missing type annotations, specifying whether the issue is a missing return type or missing input type.
    """
    data = check_for_functions_in_module_with_missing_notations(library_module)
    for i in data:
        print(
            f"Function '{i['function_name']}' of type {'Missing Return' if i['function_name'] is MissingReturnType else 'Missing Input type'}"
        )


def get_return_type(func: MethodType) -> Any:
    """
    Retrieve the return type annotation of a given function.

    Parameters:
    func (callable): The function to analyze.

    Returns:
    type: The return type of the function. Returns `NoReturnType` if no type annotation is specified.
    """
    signature = inspect.signature(func)

    return_type = signature.return_annotation

    if return_type == inspect.Signature.empty:
        return MissingReturnType
    else:
        return return_type


def get_function_inputs(func: MethodType) -> List[dict]:
    """
    Retrieve all input parameters of a given function along with their types and default values.

    Parameters:
    func (callable): The function to analyze.

    Returns:
    list: A list of dictionaries containing {'name': parameter_name, 'type': parameter_type, 'default': default_value}.
    """
    signature = inspect.signature(func)

    type_hints = get_type_hints(func)

    input_parameters = []
    for param_name, param in signature.parameters.items():
        param_type = type_hints.get(param_name, None)

        if param.default is not inspect.Parameter.empty:
            default_value = param.default

            input_parameters.append(
                {"name": param_name, "type": param_type, "default": default_value}
            )
        else:
            input_parameters.append(
                {"name": param_name, "type": param_type, "default": NoInputType}
            )

    return input_parameters

def get_function_id_by_name(func_name)->Union[None,ModuleType]:
    """
    Retrieve the function object (ID) from its name.

    Parameters:
    func_name (str): The name of the function to retrieve.

    Returns:
    callable or None: The function object if found, None if not found.
    """
    if func_name in globals():
        func_obj = globals()[func_name]
        if callable(func_obj):
            return func_obj
    return None


def count_functions_in_module(module:ModuleType, library_name:str)->int:
    """Count the number of functions in a module and its submodules.

Args:
    module (ModuleType): The module to analyze.
    library_name (str): The library name to use for identifying submodules.

Returns:
    int: The total number of functions in the module and its submodules.
"""
    function_count = 0
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj):
            function_count += 1
        elif inspect.ismodule(obj) and obj.__package__.startswith(library_name):
            function_count+=count_functions_in_module(obj, library_name)
    return function_count

def count_functions_in_library(library_name:str)->int:
    """Count the number of functions in a library by importing it and analyzing its modules.

Args:
    library_name (str): The name of the library to import and analyze.

Returns:
    int: The total number of functions in the library, or -1 if the library could not be found."""
    try:
        module = importlib.import_module(library_name)
    except ModuleNotFoundError:
        return -1
    function_count = count_functions_in_module(module,library_name)
    
    return function_count

class NoInputType:
    """Custom class to indicate that no input type annotation is specified."""

    pass


class MissingReturnType:
    """Custom class to indicate that no return type annotation is specified."""

    pass

def restrict_to_directory(allowed_dir):
    def decorator(func):
        def wrapper(file_path, *args, **kwargs):
            # Get absolute paths to compare
            real_allowed_dir = os.path.realpath(allowed_dir)
            real_file_path = os.path.realpath(file_path)

            # Check if the file is within the allowed directory
            if not real_file_path.startswith(real_allowed_dir):
                raise PermissionError(f"Access denied: {file_path} is outside the allowed directory")

            return func(file_path, *args, **kwargs)
        return wrapper
    return decorator
