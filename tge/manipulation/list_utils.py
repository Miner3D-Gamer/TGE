from itertools import permutations as itertools_permutations
from collections.abc import Iterable
from typing import Any, Union, List


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

    for item in lst:
        if isinstance(item, (int, float)):
            prod = prod * item
    return prod


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


def calculate_average(lst: Iterable) -> float:
    """
    Calculate the average (mean) of a list of numbers.

    Args:
        lst (Iterable): The list of numbers to calculate the average of.

    Returns:
        float: The average of the numbers in the list. Returns 0 if the list is empty.
    """
    length = len(lst)

    if length == 0:
        return 0  # To avoid division by zero

    total = sum(lst)
    average = total / length
    return average


def find_common_elements(lst1: Iterable, lst2: Iterable) -> list:
    """
    Find common elements between two lists.

    Args:
        lst1 (Iterable): The first list of elements.
        lst2 (Iterable): The second list of elements.

    Returns:
        list: A list of elements that are common to both `lst1` and `lst2`.
    """
    result = []
    for item in lst1:
        if item in lst2:
            result.append(item)
    return result


def median(lst: Iterable) -> float:
    """
    Calculate the median of a list of numbers.

    Args:
        lst (Iterable): The list of numbers to find the median of.

    Returns:
        float: The median of the numbers in the list.
    """
    sorted_lst = sorted(lst)  # Ensure the list is sorted
    n = len(sorted_lst)
    if n % 2 == 0:
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    else:
        return sorted_lst[n // 2]


def reverse_list(lst: Iterable) -> list:
    """
    Reverse the order of elements in a list.

    Args:
        lst (Iterable): The list to reverse.

    Returns:
        list: A new list with the elements in reverse order.
    """
    return lst[::-1]


def find_max_min_difference(lst: Iterable) -> int:
    """
    Find the difference between the maximum and minimum values in a list.

    Args:
        lst (Iterable): The list of numbers.

    Returns:
        int: The difference between the maximum and minimum values in the list.
    """
    return max(lst) - min(lst)


def find_missing_number(lst: Iterable) -> int:
    """
    Find the missing number in a list of consecutive numbers.

    Assumes the list contains all numbers from 1 to `n`, except one.

    Args:
        lst (Iterable): The list of consecutive numbers with one missing.

    Returns:
        int: The missing number.
    """
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
    """
    Calculate the average of a list of numbers.

    Args:
        lst (Iterable): The list of numbers to average.

    Returns:
        float: The average of the numbers in the list.
    """
    return sum(lst) / len(lst)


def greatest_product(lst: Iterable, lst2: Iterable) -> int:
    """
    Compute the product of the largest elements from two lists.

    Args:
        lst (Iterable): The first list of numbers.
        lst2 (Iterable): The second list of numbers.

    Returns:
        int: The product of the maximum values from the two lists.
    """
    return max(lst) * max(lst2)


def permutations(lst: Iterable) -> list:
    """
    Generate all permutations of a list.

    Args:
        lst (Iterable): The list to permute.

    Returns:
        list: A list of tuples, where each tuple is a permutation of the input list.
    """
    return list(itertools_permutations(lst))


def limit_list(lst: Iterable, limit: int) -> list:
    """
    Limit a list to a specified number of elements.

    Args:
        lst (Iterable): The list to limit.
        limit (int): The maximum number of elements to include in the result.

    Returns:
        list: A list containing up to `limit` elements from the original list.
    """
    return lst[:limit]


def get_items_from_list(lst: Iterable, start: int, end: int) -> list:
    """
    Extract a sublist from a list based on start and end indices.

    Args:
        lst (Iterable): The list to slice.
        start (int): The starting index of the sublist.
        end (int): The ending index of the sublist.

    Returns:
        list: A sublist from the original list, starting at `start` and ending at `end`.
    """
    return lst[start:end]


def sort_list_of_dictionaries(lst: Iterable, key: str) -> tuple:
    """
    Sort a list of dictionaries by a specified key.

    Args:
        lst (Iterable): The list of dictionaries to sort.
        key (str): The key to sort the dictionaries by.

    Returns:
        tuple: A tuple containing the sorted list and a boolean indicating success.
    """
    try:
        return sorted(lst, key=lambda x: x[key]), True
    except:
        return lst, False


def zipper_insert(list1: list, list2: list) -> list:
    # Find the length of the shorter list
    min_length = min(len(list1), len(list2))

    # Initialize the result list
    result = []

    # Add elements from both lists in alternating fashion
    for i in range(min_length):
        result.append(list1[i])
        result.append(list2[i])

    # Append any remaining elements from the longer list
    result.extend(list1[min_length:])
    result.extend(list2[min_length:])

    return result


def compress_list(list_to_compress: list) -> Union[Any, list]:
    width = len(list_to_compress)
    new_sub_list = []
    char = list_to_compress[0]
    amount = 0
    add = lambda amount, char: (
        [amount, char] if amount > 1 and amount != width else [char]
    )
    for index in range(len(list_to_compress)):
        new_char = list_to_compress[index]
        if new_char == char:
            amount += 1
        else:
            new_sub_list += add(amount, char)
            char = new_char
            amount = 1
    else:
        new_sub_list += add(amount, char)
    if len(new_sub_list) == 1:
        new_sub_list = new_sub_list[0]
    return new_sub_list


def compress_list_of_lists(list_to_compress: List[list]) -> List[list]:
    new_list = []
    for sub_list in list_to_compress:
        new_list.append(compress_list(sub_list))
    return new_list


def decompress_list(list_to_decompress: Union[list, Any], width: int) -> list:
    if not isinstance(list_to_decompress, list):
        return [list_to_decompress] * width

    new_sub_list = []
    repeat_amount = 1
    for index in range(len(list_to_decompress)):
        item = list_to_decompress[index]
        if isinstance(item, int):
            repeat_amount = item
        else:
            new_sub_list += repeat_amount * [item]
            repeat_amount = 1
    return new_sub_list


def decompress_list_of_lists(list_to_decompress: List[list], width: int) -> List[list]:
    new_list = []
    for sub_list in list_to_decompress:
        new_list.append(decompress_list(sub_list, width))
    return new_list
