HEX_CHARACTERS='0123456789ABCDEF'
def convert_binary_to_decimal(binary):
	'\n    Convert a binary number to its decimal equivalent.\n\n    Parameters:\n    binary (str): A binary number represented as a string.\n\n    Returns:\n    int: The decimal equivalent of the given binary number.\n    ';A=0;B=0
	for C in reversed(str(binary)):
		if C=='1':A+=2**B
		B+=1
	return A
def convert_decimal_to_binary(decimal):
	"\n    Convert a decimal integer to its binary representation.\n\n    Parameters:\n    decimal (int): The decimal integer to be converted.\n\n    Returns:\n    str: The binary representation of the input decimal integer.\n\n    Examples:\n    >>> convert_decimal_to_binary(10)\n    '1010'\n    >>> convert_decimal_to_binary(23)\n    '10111'\n    >>> convert_decimal_to_binary(0)\n    '0'\n    ";A=decimal;B=''
	while A>0:B+=str(A%2);A//=2
	return B[::-1]
def convert_decimal_to_hexadecimal(decimal):
	'\n    Convert a decimal integer to its hexadecimal representation.\n\n    Parameters:\n    decimal (int): The decimal integer to be converted.\n\n    Returns:\n    str: The hexadecimal representation of the input decimal number.\n    ';A=decimal
	if A==0:return'0'
	B=''
	while A>0:C=A%16;D=HEX_CHARACTERS[C];B=D+B;A=A//16
	return B
def convert_hexadecimal_to_decimal(hexadecimal):
	'\n    Convert a hexadecimal string to its decimal representation.\n\n    Parameters:\n    hexadecimal (str): A string representing a hexadecimal number.\n\n    Returns:\n    int: The decimal representation of the input hexadecimal number.\n\n    Raises:\n    ValueError: If the input is not a valid hexadecimal string.\n    ';A=hexadecimal
	if A=='0':return 0
	B=0
	for C in reversed(A):B=B*16+HEX_CHARACTERS.index(C)