# TODO: Note to future self: Write a script to automatically generate the and truth table

from typing import List, Tuple
from collections.abc import Iterable

# and
def and_three(a: bool, b: bool, c: bool) -> bool:
    return a and b and c


def and_four(a: bool, b: bool, c: bool, d: bool) -> bool:
    return a and b and c and d


def and_five(a: bool, b: bool, c: bool, d: bool, e: bool) -> bool:
    return a and b and c and d and e


def and_six(a: bool, b: bool, c: bool, d: bool, e: bool, f: bool) -> bool:
    return a and b and c and d and e and f


def and_seven(a: bool, b: bool, c: bool, d: bool, e: bool, f: bool, g: bool) -> bool:
    return a and b and c and d and e and f and g


def and_eight(
    a: bool, b: bool, c: bool, d: bool, e: bool, f: bool, g: bool, h: bool
) -> bool:
    return a and b and c and d and e and f and g and h


def and_nine(
    a: bool, b: bool, c: bool, d: bool, e: bool, f: bool, g: bool, h: bool, i: bool
) -> bool:
    return a and b and c and d and e and f and g and h and i


def and_ten(
    a: bool,
    b: bool,
    c: bool,
    d: bool,
    e: bool,
    f: bool,
    g: bool,
    h: bool,
    i: bool,
    j: bool,
) -> bool:
    return a and b and c and d and e and f and g and h and i and j


# or
def or_three(a: bool, b: bool, c: bool) -> bool:
    return a or b or c


def or_four(a: bool, b: bool, c: bool, d: bool) -> bool:
    return a or b or c or d


def or_five(a: bool, b: bool, c: bool, d: bool, e: bool) -> bool:
    return a or b or c or d or e


def or_six(a: bool, b: bool, c: bool, d: bool, e: bool, f: bool) -> bool:
    return a or b or c or d or e or f


def or_seven(a: bool, b: bool, c: bool, d: bool, e: bool, f: bool, g: bool) -> bool:
    return a or b or c or d or e or f or g


def or_eight(
    a: bool, b: bool, c: bool, d: bool, e: bool, f: bool, g: bool, h: bool
) -> bool:
    return a or b or c or d or e or f or g or h


def or_nine(
    a: bool, b: bool, c: bool, d: bool, e: bool, f: bool, g: bool, h: bool, i: bool
) -> bool:
    return a or b or c or d or e or f or g or h or i


def or_ten(
    a: bool,
    b: bool,
    c: bool,
    d: bool,
    e: bool,
    f: bool,
    g: bool,
    h: bool,
    i: bool,
    j: bool,
) -> bool:
    return a or b or c or d or e or f or g or h or i or j


# nand
def nand(a: bool, b: bool) -> bool:
    return not (a and b)


def nand_three(a: bool, b: bool, c: bool) -> bool:
    return not (a and b and c)


def nand_any(*args: bool) -> bool:
    return not all(args)


# xor
def xor(a: bool, b: bool) -> bool:
    return a ^ b


def xor_three(a: bool, b: bool, c: bool) -> bool:
    return a ^ b ^ c


def xor_any(*args: bool) -> bool:
    return sum(args) % 2 == 1


# xnor
def xnor(a: bool, b: bool) -> bool:
    return not (a ^ b)


def xnor_three(a: bool, b: bool, c: bool) -> bool:
    return not (a ^ b ^ c)


def xnor_any(*args: bool) -> bool:
    return sum(args) % 2 == 0


# mux
def mux(a: bool, b: bool, c: bool) -> bool:
    return a if c else b


def mux_four(a: bool, b: bool, c: bool, d: bool, sel_1: bool, sel_0: bool) -> bool:
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
    inputs = [a, b, c, d, e, f, g, h]
    index = (sel_2 << 2) | (sel_1 << 1) | sel_0
    return inputs[index]


def mux_any(inputs: "Iterable[bool]", selectors: "Iterable[bool]") -> bool:
    if len(inputs) != 2 ** len(selectors):
        raise ValueError(
            "Number of inputs must be 2^n where n is the number of selectors."
        )

    index = 0
    for i, sel in enumerate(reversed(selectors)):
        index |= sel << i

    return inputs[index]


# nor
def nor(a: bool, b: bool, c: bool) -> bool:
    return not (a or b)


def nor_three(a: bool, b: bool, c: bool) -> bool:
    return not (a or b or c)


def nor_any(*args: bool) -> bool:
    return not any(args)


def binary_to_gray(
    b3: bool, b2: bool, b1: bool, b0: bool
) -> Tuple[bool, bool, bool, bool]:
    g3 = b3
    g2 = b3 ^ b2
    g1 = b2 ^ b1
    g0 = b1 ^ b0
    return g3, g2, g1, g0


def demux(input: bool, *select: bool) -> List[bool]:
    n = len(select)
    outputs = [False] * (2**n)

    index = 0
    for i in range(n):
        index |= select[i] << (n - 1 - i)

    outputs[index] = input
    return outputs


def half_adder(a: bool, b: bool) -> Tuple[bool, bool]:
    return xor(a, b), a and b


def full_adder(a: bool, b: bool, cin: bool = False) ->Tuple[bool, bool]:
    sum1, carry1 = half_adder(a, b)
    sum2, carry2 = half_adder(sum1, cin)
    return sum2, carry1 or carry2


def four_bit_adder(
    a: Tuple[bool, bool, bool, bool],
    b: Tuple[bool, bool, bool, bool],
    carry: bool = False,
) -> Tuple[bool, bool, bool, bool, bool]:
    carry, sum1 = full_adder(a[3], b[3], carry)
    carry, sum2 = full_adder(a[2], b[2], carry)
    carry, sum3 = full_adder(a[1], b[1], carry)
    carry, sum4 = full_adder(a[0], b[0], carry)
    return sum4, sum3, sum2, sum1, carry


def two_complement(b: Tuple[bool, bool, bool, bool]) -> Tuple[bool, bool, bool, bool]:
    # Invert the bits
    inverted_b = tuple((not (bit)) for bit in b)
    # Add 1 to the inverted bits
    one = (False, False, False, True)
    return four_bit_adder(inverted_b, one)[0:4]


def four_bit_subtractor(
    a:Tuple[bool, bool, bool, bool],
    b:Tuple[bool, bool, bool, bool],
    borrow: bool = False,
) ->Tuple[bool, bool, bool, bool, bool]:
    b_complement = two_complement(b)
    result, carry_out = four_bit_adder(a, b_complement, borrow)
    return result + (carry_out,)

def any_bit_adder(a: "Iterable[bool]", b: "Iterable[bool]", carry: bool = False) ->Tuple[List[bool], bool]:
    if len(a) != len(b):
        raise ValueError("Input lists must have the same length")

    n = len(a)
    result = []
    for i in range(n-1, -1, -1):
        sum_bit, carry = full_adder(a[i], b[i], carry)
        result.append(sum_bit)
    
    result.reverse()
    return result, carry


def number_to_bools(num: int) -> List[bool]:
    if num < 0:
        raise ValueError("Input number must be non-negative")

    if num == 0:
        num_bits = 1
    else:
        num_bits = num.bit_length()

    binary_str = bin(num)[2:]
    padded_binary_str = binary_str.zfill(num_bits)
    bool_list = [bit == '1' for bit in padded_binary_str]

    return bool_list

def bools_to_number(bools: "Iterable[bool]") -> int:
    num = 0
    bit_length = len(bools)
    for i in range(bit_length):
        if bools[i]:
            num += 1 << (bit_length - 1 - i)
    return num
