import importlib.util
import sys

def load_module_lazily(module_name):
    """
    Loads a module by name without executing it immediately.

    Args:
        module_name (str): The name of the module to load.

    Returns:
        module: The loaded module object, ready for later execution.
    """
    # Step 1: Find the module specification using the module name
    spec = importlib.util.find_spec(module_name)
    
    # Check if the module spec was found
    if spec is None:
        raise ImportError(f"Module '{module_name}' not found.")
    
    # Step 2: Create a module object from the specification
    module = importlib.util.module_from_spec(spec)
    
    # Store the module in sys.modules to avoid duplicate imports
    sys.modules[module_name] = module
    
    return module

def execute_module(module):
    """
    Executes a previously loaded module.

    Args:
        module: The module object to execute.
    """
    # Ensure the module has a loader to execute
    if hasattr(module, '__spec__') and module.__spec__.loader:
        module.__spec__.loader.exec_module(module)
    else:
        raise ImportError("Cannot execute module; missing loader.")

# Usage Example
# Load the module without executing it

from tge.tbe import profile_function
lazy_module = load_module_lazily('setup_tge')


profile_function(execute_module, "profile", lazy_module)


    