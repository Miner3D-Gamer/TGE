from typing import Any, Dict, List
def remove_duplicates_from_dictionary(dictionary: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Remove duplicates from a dictionary based on its values.

    Parameters:
    dictionary (dict): A dictionary to remove duplicates from based on values.

    Returns:
    dict: A new dictionary with unique values, where only the first occurrence
          of each value is retained, preserving the original key-value pairs.
    """
    unique_values = set(dictionary.values())
    new_dictionary:Dict[Any, Any] = {}

    for key, value in dictionary.items():
        if value in unique_values:
            new_dictionary[key] = value
            unique_values.remove(value)

    return new_dictionary


def get_from_dict_by_list(data_dict:Dict[Any,Any], keys:List[Any])->Any:
    """
    Access a nested dictionary with a list of keys.
    
    :param data_dict: Dictionary to access.
    :param keys: List of keys to access the dictionary.
    :return: Value from the dictionary.
    """
    for key in keys:
        data_dict = data_dict[key]
    return data_dict

def set_in_dict_by_list(data_dict:Dict[Any,Any], keys:List[Any], value:Any)->None:
    """
    Set a value in a nested dictionary with a list of keys.
    
    :param data_dict: Dictionary to set the value in.
    :param keys: List of keys to access the dictionary.
    :param value: Value to set in the dictionary.
    """
    for key in keys[:-1]:
        data_dict = data_dict.setdefault(key, {})
    data_dict[keys[-1]] = value

__all__ = ['remove_duplicates_from_dictionary', 'get_from_dict_by_list', 'set_in_dict_by_list']