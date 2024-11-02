# TODO: Note to future self: Write a script to automatically generate the and truth table

from typing import List, Tuple


# nand
def nand(a: bool, b: bool) -> bool:
    """ Returns true if all arguments are false. """
    return not (a and b)


def nand_three(a: bool, b: bool, c: bool) -> bool:
    """ Returns true if all arguments are false. """
    return not (a and b and c)


def nand_any(*args: bool) -> bool:
    """ Returns true if all arguments are false. """
    return not all(args)


# xor
def xor(a: bool, b: bool) -> bool:
    """ Returns true if all arguments are false. """
    return a ^ b


def xor_three(a: bool, b: bool, c: bool) -> bool:
    """ Returns true if all arguments are false. """
    return a ^ b ^ c


def xor_any(*args: bool) -> bool:
    """ Returns true if all arguments are false. """
    return sum(args) % 2 == 1


# xnor
def xnor(a: bool, b: bool) -> bool:
    """ Returns true if all arguments are false. """
    return not (a ^ b)


def xnor_three(a: bool, b: bool, c: bool) -> bool:
    """ Returns true if all arguments are false. """
    return not (a ^ b ^ c)


def xnor_any(*args: bool) -> bool:
    """ Returns true if all arguments are false. """
    return sum(args) % 2 == 0


# mux


def mux_four(a: bool, b: bool, c: bool, d: bool, sel_1: bool, sel_0: bool) -> bool:
    """ Multiplexes 4 inputs based on 2 selectors. """
    inputs = [a, b, c, d]
    index = (sel_1 << 1) | sel_0
    return inputs[index]


def mux_eight(
    a: bool,
    b: bool,
    c: bool,
    d: bool,
    e: bool,
    f: bool,
    g: bool,
    h: bool,
    sel_2: bool,
    sel_1: bool,
    sel_0: bool,
) -> bool:
    """ Multiplexes 8 inputs based on 3 selectors. """
    inputs = [a, b, c, d, e, f, g, h]
    index = (sel_2 << 2) | (sel_1 << 1) | sel_0
    return inputs[index]


def mux_any(inputs: List[bool], selectors: List[bool]) -> bool:
    """ Multiplexes a list of inputs based on a list of selectors. """
    if len(inputs) != 2 ** len(selectors):
        raise ValueError(
            "Union[int,float] of inputs must be 2^n where n is the number of selectors."
        )

    index = 0
    for i, sel in enumerate(reversed(selectors)):
        index |= sel << i

    return inputs[index]


# nor
def nor(a: bool, b: bool, c: bool) -> bool:
    """ Returns true if all arguments are false. """
    return not (a or b)


def nor_three(a: bool, b: bool, c: bool) -> bool:
    """ Returns true if all arguments are false. """
    return not (a or b or c)


def nor_any(*args: bool) -> bool:
    """ Returns true if all arguments are false. """
    return not any(args)


#
def binary_to_gray(
    b3: bool, b2: bool, b1: bool, b0: bool
) -> Tuple[bool, bool, bool, bool]:
    """ Converts a 4-bit binary number to a 4-bit gray code. """
    g3 = b3
    g2 = b3 ^ b2
    g1 = b2 ^ b1
    g0 = b1 ^ b0
    return g3, g2, g1, g0


def demux(input: bool, *select: bool) -> List[bool]:
    """ Demultiplexes a single bit input. """
    n = len(select)
    outputs = [False] * (2**n)

    index = 0
    for i in range(n):
        index |= select[i] << (n - 1 - i)

    outputs[index] = input
    return outputs


def half_adder(a: bool, b: bool) -> Tuple[bool, bool]:
    """ Adds two bits. """
    return xor(a, b), a and b


def full_adder(a: bool, b: bool, cin: bool = False) -> Tuple[bool, bool]:
    """ Adds two bits with an optional carry input. """
    sum1, carry1 = half_adder(a, b)
    sum2, carry2 = half_adder(sum1, cin)
    return sum2, carry1 or carry2


def four_bit_adder(
    a: Tuple[bool, bool, bool, bool],
    b: Tuple[bool, bool, bool, bool],
    carry: bool = False,
) -> Tuple[bool, bool, bool, bool, bool]:
    """
    Adds two 4-bit binary numbers with an optional carry input.

    Args:
        a (Tuple[bool, bool, bool, bool]): First 4-bit binary number.
        b (Tuple[bool, bool, bool, bool]): Second 4-bit binary number.
        carry (bool, optional): Carry input from previous addition. Defaults to False.

    Returns:
        Tuple[bool, bool, bool, bool, bool]: 4-bit sum and carry out.
    """
    carry, sum1 = full_adder(a[3], b[3], carry)
    carry, sum2 = full_adder(a[2], b[2], carry)
    carry, sum3 = full_adder(a[1], b[1], carry)
    carry, sum4 = full_adder(a[0], b[0], carry)
    return sum4, sum3, sum2, sum1, carry


def flip_four_bits(b: Tuple[bool, bool, bool, bool]) -> Tuple[bool, bool, bool, bool]:
    """
    Flips the bits of a 4-bit binary number.

    Args:
        b (Tuple[bool, bool, bool, bool]): 4-bit binary number to flip.

    Returns:
        Tuple[bool, bool, bool, bool]: 4-bit binary number with flipped bits.
    """
    return (not b[0], not b[1], not b[2], not b[3])


def two_complement(
    b: Tuple[bool, bool, bool, bool]
) -> Tuple[bool, bool, bool, bool, bool]:
    """
    Computes the two's complement of a 4-bit binary number.
    This means it negates the bits. (3 -> -3, 2 -> -2, etc.)

    Args:
        b (Tuple[bool, bool, bool, bool]): 4-bit binary number to negate.

    Returns:
        Tuple[bool, bool, bool, bool]: 4-bit two's complement representation.
    """
    inverted_b = flip_four_bits(b)
    one = (False, False, False, True)
    return four_bit_adder(inverted_b, one)


def four_bit_subtractor(
    a: Tuple[bool, bool, bool, bool],
    b: Tuple[bool, bool, bool, bool],
    borrow: bool = False,
) -> Tuple[bool, bool, bool, bool, bool]:
    """
    Subtracts one 4-bit binary number from another using two's complement.

    Args:
        a (Tuple[bool, bool, bool, bool]): Minuend (number to be subtracted from).
        b (Tuple[bool, bool, bool, bool]): Subtrahend (number to be subtracted).
        borrow (bool, optional): Borrow input from previous subtraction. Defaults to False.

    Returns:
        Tuple[bool, bool, bool, bool, bool]: 4-bit difference and borrow out.
    """
    b_complement = two_complement(b)
    result = four_bit_adder(a[:4], b_complement[:4], borrow)
    return result


def any_bit_adder(
    a: List[bool], b: List[bool], carry: bool = False
) -> Tuple[List[bool], bool]:
    """
    Adds two lists of booleans with an optional carry input.

    Args:
        a (List[bool]): First list of booleans.
        b (List[bool]): Second list of booleans.
        carry (bool, optional): Carry input from previous addition. Defaults to False.

    Returns:
        Tuple[List[bool], bool]: List of booleans sum and carry out.
    """
    if len(a) != len(b):
        raise ValueError("Input lists must have the same length")

    n = len(a)
    result: List[bool] = []
    for i in range(n - 1, -1, -1):
        sum_bit, carry = full_adder(a[i], b[i], carry)
        result.append(sum_bit)

    result.reverse()
    return result, carry


def number_to_bools(num: int) -> List[bool]:
    """
    Converts an integer to a list of booleans.
    """
    if num < 0:
        raise ValueError("Input number must be non-negative")

    if num == 0:
        num_bits = 1
    else:
        num_bits = num.bit_length()

    binary_str = bin(num)[2:]
    padded_binary_str = binary_str.zfill(num_bits)
    bool_list = [bit == "1" for bit in padded_binary_str]

    return bool_list


def bools_to_number(bools: List[bool]) -> int:
    """
    Converts a list of booleans to an integer.
    """
    num = 0
    bit_length = len(bools)
    for i in range(bit_length):
        if bools[i]:
            num += 1 << (bit_length - 1 - i)
    return num


__all__ = [
    "nand",
    "nand_three",
    "nand_any",
    "xor",
    "xor_three",
    "xor_any",
    "xnor",
    "xnor_three",
    "xnor_any",
    #"mux",
    "mux_four",
    "mux_eight",
    "mux_any",
    "nor",
    "nor_three",
    "nor_any",
    "binary_to_gray",
    "demux",
    "half_adder",
    "full_adder",
    "four_bit_adder",
    "flip_four_bits",
    "two_complement",
    "four_bit_subtractor",
    "any_bit_adder",
    "number_to_bools",
    "bools_to_number",
]
