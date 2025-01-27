from typing import Any, Union, List, Optional
from collections.abc import Iterable
import math
__all__ = ['list_mul', 'remove_duplicates', 'count_occurrences', 'calculate_average', 'find_common_elements', 'median', 'reverse_list', 'find_max_min_difference', 'find_missing_number', 'greatest_product', 'zipper_insert', 'compress_list', 'compress_list_of_lists', 'decompress_list', 'decompress_list_of_lists', 'MaxSizeList']

def list_mul(lst: List[Union[int, float]]) -> Union[int, float]:
    """
    Multiply all the numbers in the given list and return the result along with a success message.

    :param lst: A list of numbers to multiply.
    :type lst: list
    :return: A tuple containing the product of the numbers in the list and a success message.
    :rtype: tuple
    :raises TypeError: If the list contains non-numeric values.
    """

    return math.prod(lst)


def remove_duplicates(list: List[Any]) -> List[Any]:
    """
    Removes duplicates from a given list and returns it.

    :param list: A list of items.
    :type list: list
    :return: A new list containing no duplicates.
    :rtype: list
    """
    result: List[Any] = []
    for item in list:
        if item not in result:
            result.append(item)
    return result


def count_occurrences(list: List[Any], item: Any) -> int:
    """
    Counts the number of occurrences of a given item in a list.

    :param list: The list to search for occurrences.
    :type list: list
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


def calculate_average(lst: List[Union[int, float]]) -> float:
    """
    Calculate the average (mean) of a list of numbers.

    Args:
        lst (list): The list of numbers to calculate the average of.

    Returns:
        float: The average of the numbers in the list. Returns 0 if the list is empty.
    """
    length = len(lst)

    if length == 0:
        return 0

    total = sum(lst)
    average = total / length
    return average


def find_common_elements(lst1: List[Any], lst2: List[Any]) -> List[Any]:
    """
    Find common elements between two lists.

    Args:
        lst1 (list): The first list of elements.
        lst2 (list): The second list of elements.

    Returns:
        list: A list of elements that are common to both `lst1` and `lst2`.
    """
    result: List[Any] = []
    for item in lst1:
        if item in lst2:
            result.append(item)
    return result


def median(lst: List[Union[int, float]]) -> float:
    """
    Calculate the median of a list of numbers.

    Args:
        lst (list): The list of numbers to find the median of.

    Returns:
        float: The median of the numbers in the list.
    """
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    else:
        return sorted_lst[n // 2]


def reverse_list(lst: List[Any]) -> List[Any]:
    """
    Reverse the order of elements in a list.

    Args:
        lst (list): The list to reverse.

    Returns:
        list: A new list with the elements in reverse order.
    """
    return lst[::-1]


def find_max_min_difference(lst: List[int]) -> int:
    """
    Find the difference between the maximum and minimum values in a list.

    Args:
        lst (list): The list of numbers.

    Returns:
        int: The difference between the maximum and minimum values in the list.
    """
    return max(lst) - min(lst)


def find_missing_number(lst: List[int]) -> int:
    """
    Find the missing number in a list of consecutive numbers.

    Assumes the list contains all numbers from 1 to `n`, except one.

    Args:
        lst (list): The list of consecutive numbers with one missing.

    Returns:
        int: The missing number.
    """
    return sum(range(1, len(lst) + 1)) - sum(lst)


def greatest_product(lst: List[int], lst2: List[int]) -> int:
    """
    Compute the product of the largest elements from two lists.

    Args:
        lst (list): The first list of numbers.
        lst2 (list): The second list of numbers.

    Returns:
        int: The product of the maximum values from the two lists.
    """
    return max(lst) * max(lst2)


def zipper_insert(list1: List[Any], list2: List[Any]) -> List[Any]:
    """
    Merges two lists by alternating elements from each list.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: A new list with elements from `list1` and `list2` interleaved.
              Remaining elements from the longer list are appended at the end.
    """
    min_length = min(len(list1), len(list2))

    result: List[Any] = []

    for i in range(min_length):
        result.append(list1[i])
        result.append(list2[i])

    result.extend(list1[min_length:])
    result.extend(list2[min_length:])

    return result


def compress_list(list_to_compress: List[Any]) -> Union[Any, List[Any]]:
    """
    Compresses a list by converting consecutive identical elements into a count-value pair.

    Args:
        list_to_compress (list): The list to compress.

    Returns:
        Union[Any, list]: A compressed list where consecutive identical elements are represented as [count, value],
                          or a single value if the compressed list has only one element.

    Example:
        >>> compress_list([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
        []
    """
    width = len(list_to_compress)
    new_sub_list: List[Any] = []
    char = list_to_compress[0]
    amount = 0

    def add(amount: int, char: Any) -> List[Any]:
        """Helper function to add a count-value pair to the new_sub_list."""
        if amount > 1 and amount != width:
            return [amount, char]
        else:
            return [char]

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


def compress_list_of_lists(list_to_compress: List[List[Any]]) -> List[List[Any]]:
    """
    Compresses a list of lists by applying `compress_list` to each sublist.

    Args:
        list_to_compress (List[list]): A list containing sub-lists to compress.

    Returns:
        List[list]: A list of compressed sub-lists.
    """
    new_list: List[List[Any]] = []
    for sub_list in list_to_compress:
        new_list.append(compress_list(sub_list))
    return new_list


def decompress_list(
    list_to_decompress: Union[List[Optional[Union[int, str]]], Any], width: int
) -> List[Any]:
    """
    Decompresses a list by expanding count-value pairs into repeated elements.

    Args:
        list_to_decompress (Union[list, Any]): The list or single value to decompress.
        width (int): The width used to repeat single values.

    Returns:
        list: A decompressed list with expanded count-value pairs or repeated single values.
    """
    if not isinstance(list_to_decompress, list):
        return [list_to_decompress] * width

    new_sub_list: List[Any] = []
    repeat_amount = 1
    for item in list_to_decompress:
        if isinstance(item, int):
            repeat_amount = item
        else:
            new_sub_list += repeat_amount * [item]
            repeat_amount = 1
    return new_sub_list


def decompress_list_of_lists(list_to_decompress: List[Union[List[Union[int, Any]], Any]], width: int) -> List[List[Any]]:
    """
    Decompresses a list of lists by applying `decompress_list` to each sublist.

    Args:
        list_to_decompress (List[list]): A list containing sub-lists to decompress.
        width (int): The width used to repeat single values.

    Returns:
        List[list]: A list of decompressed sub-lists.
    """
    new_list: List[List[Any]] = []
    for sub_list in list_to_decompress:
        new_list.append(decompress_list(sub_list, width))
    return new_list


class MaxSizeList(List[Any]):
    def __init__(self, max_size: int):
        """
        Initializes a MaxSizeList object with a specified maximum size.

        Parameters:
        max_size (int): The maximum number of elements the list can hold. Once this limit is reached,
        the oldest elements are removed when new elements are added.
        """
        super().__init__()
        self.max_size = max_size

    def append(self, item: Any):
        """
        Appends an item to the list, and if the list exceeds the maximum size,
        removes the oldest element to maintain the size limit.

        Parameters:
        item: The item to append to the list.
        """
        super().append(item)
        if len(self) > self.max_size:
            self.pop(0)

    def extend(self, iterable: "Iterable[Any]"):
        """
        Extends the list by appending elements from an iterable, and removes the oldest elements
        if the list exceeds the maximum size.

        Parameters:
        iterable (iterable): An iterable containing the elements to extend the list with.
        """
        super().extend(iterable)
        while len(self) > self.max_size:
            self.pop(0)
