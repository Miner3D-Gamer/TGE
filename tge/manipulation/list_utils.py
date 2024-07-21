from itertools import permutations as itertools_permutations
from collections.abc import Iterable




def list_sum(lst: Iterable) -> int:
    total = 0
    for item in lst:
        if isinstance(item, (int, float)):
            total += item
    return total

def list_mul(lst: Iterable) -> tuple:
    """
    Multiply all the numbers in the given list and return the result along with a success message.

    :param lst: A list of numbers to multiply.
    :type lst: Iterable
    :return: A tuple containing the product of the numbers in the list and a success message.
    :rtype: tuple
    :raises TypeError: If the list contains non-numeric values.
    """
    prod = 1
    try:
        for item in lst:
            if isinstance(item, (int, float)):
                prod = prod * item
        return prod
    except TypeError:
        return 0
    
def remove_duplicates(list: Iterable) -> list:
    """
    Removes duplicates from a given list and returns it.

    :param list: A list of items.
    :type list: Iterable
    :return: A new list containing no duplicates.
    :rtype: Iterable
    """
    result = []
    for item in list:
        if item not in result:
            result.append(item)
    return result

def count_occurrences(list: Iterable, item: str) -> int:
    """
    Counts the number of occurrences of a given item in a list.

    :param list: The list to search for occurrences.
    :type list: Iterable
    :param item: The item to count occurrences of.
    :type item: str
    :return: The number of occurrences of the given item in the list.
    :rtype: int
    """
    count = 0
    for obj in list:
        if obj == item:
            count += 1
    return count

def calculate_average(lst: Iterable) -> int:
    total = list_sum(lst)
    length = len([item for item in lst if isinstance(item, (int, float))])
    
    if length == 0:
        return 0  # To avoid division by zero
    
    average = total / length
    return average

def find_common_elements(lst1: Iterable, lst2: Iterable) -> list:
    result = []
    for item in lst1:
        if item in lst2:
            result.append(item)
    return result

def median(lst: Iterable) -> int:
    lst.sort()
    if len(lst) % 2 == 0:
        return (lst[len(lst) // 2 - 1] + lst[len(lst) // 2]) / 2
    else:
        return lst[len(lst) // 2]
    
def reverse_list(lst: Iterable) -> list:
    return lst[::-1]

def find_max_min_difference(lst: Iterable) -> int:
    return max(lst) - min(lst)

def find_missing_number(lst: Iterable) -> int:
    return sum(range(1, len(lst) + 1)) - sum(lst)

def remove_whitespace_from_list(lst: Iterable) -> list:
    """
    Removes whitespace characters from all elements in a list of strings.
    
    Args:
        lst (list): Iterable of strings
        
    Returns:
        list: Iterable with whitespace removed from all elements
    """
    return [string.replace(" ", "") for string in lst]

def exponential_average(lst: Iterable) -> float:
    return sum(lst) / len(lst)

def greatest_product(lst: Iterable, lst2: Iterable) -> int:
    return max(lst) * max(lst2)

def permutations(lst: Iterable) -> list:
    return list(itertools_permutations(lst))

def limit_list(list: Iterable, limit: int) -> list:
    return list[:limit]

def get_items_from_list(list: Iterable, start: int, end: int) -> list:
    return list[start:end]

def sort_list_of_dictionaries(lst, key: str) -> tuple:
    try:
        return sorted(lst, key=lambda x: x[key]), True
    except:
        return lst, False