_C='!@#$%^&*()_-+=<>?/\\'
_B=True
_A=False
import re,requests
from ipaddress import IPv4Address,IPv6Address,AddressValueError
from.manipulation.string_utils import reverse_string
def is_empty(text):'\n    Returns a boolean indicating whether the given text is empty or not.\n\n    :param text: A string to check if it is empty.\n    :type text: str\n    :return: True if the given text is empty, False otherwise.\n    :rtype: bool\n    ';return text==''
def is_prime(number):
	'\n    Determines whether a given integer is a prime number or not.\n    \n    :param number: An integer to check for primality.\n    :type number: int\n    :return: True if the given number is prime, False otherwise.\n    :rtype: bool\n    ';A=number
	if A<=1:return _A
	for B in range(2,A):
		if A%B==0:return _A
	return _B
def is_palindrome(string):'\n    Check if a given string is a palindrome.\n\n    :param string: A string to be checked.\n    :type string: str\n    :return: True if the string is a palindrome, False otherwise.\n    :rtype: bool\n    ';A=string;return A==reverse_string(A)
def is_leap_year(year):'\n    Determine if a given year is a leap year or not.\n\n    A leap year occurs every 4 years, except for years that are both divisible\n    by 100 and not divisible by 400. These exceptions ensure that the calendar\n    year remains synchronized with the astronomical year.\n\n    Args:\n        year (int): The year to be checked for leap year status.\n\n    Returns:\n        bool: True if the input year is a leap year, False otherwise.\n    ';A=year;return A%4==0 and(A%100!=0 or A%400==0)
def is_even(number):'\n    Determine whether the given integer is an even number.\n\n    Parameters:\n    number (int): The integer to be checked for evenness.\n\n    Returns:\n    bool: True if the input number is even, False otherwise.\n    ';return number%2==0
def is_odd(number):"\n    Determine whether an integer is odd.\n\n    Args:\n        number (int): The integer to be checked for oddness.\n\n    Returns:\n        bool: True if the input integer is odd, False if it's even.\n    ";return number%2==1
def is_url(url):"\n    Check if a given string is a valid URL.\n\n    This function uses regular expressions to determine whether the input string\n    follows the typical pattern of a URL. It checks for patterns starting with\n    'http://' or 'https://' followed by a valid domain name, and optional\n    paths or query parameters.\n\n    Args:\n        url (str): The string to be checked as a potential URL.\n\n    Returns:\n        bool: True if the input string appears to be a valid URL, False otherwise.\n    ";A=re.compile('^(?:http|https)://(?:[\\w-]+\\.)*[\\w-]+(?:\\.[a-zA-Z]{2,})(?:/?|(?:/[^\\s]+)+)?$');return bool(re.match(A,url))
def is_url_available(url,check_url=_B):
	'\n    Check the availability of a URL by sending a GET request and evaluating the response status code.\n\n    Parameters:\n    url (str): The URL to be checked for availability.\n    check_url (bool, optional): If True, performs a basic URL format check before proceeding (default: True).\n\n    Returns:\n    bool: True if the URL is available and returns a status code of 200, False otherwise.\n    ';A=check_url
	if A:A=not is_url(url)
	if not A:return _A
	try:
		B=requests.get(url)
		if B.status_code==200:return _B
		else:return _A
	except requests.exceptions.ConnectionError or requests.exceptions.ConnectTimeout:return
def validate_email(email):'\n    Validate an email address using a regular expression pattern match.\n\n    :param email: A string representing an email address.\n    :type email: str\n    :return: A boolean indicating whether the email address is valid or not.\n    :rtype: bool\n    ';A='^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$';return re.match(A,email)is not None
def validate_password(password,length,upper,lower,digit,overwrite_special_characters,overwritten_special_characters):
	'\n    Validates a password based on specified criteria.\n\n    Args:\n        password (str): The password string to be validated.\n        length (int): The minimum required length of the password.\n        upper (bool): Whether the password must contain at least one uppercase letter.\n        lower (bool): Whether the password must contain at least one lowercase letter.\n        digit (bool): Whether the password must contain at least one digit.\n        overwrite_special_characters (bool): If True, the provided special characters will be used for validation.\n                                            If False, a default set of special characters will be used.\n        overwritten_special_characters (str): A string containing special characters to be used for validation,\n                                            applicable only if overwrite_special_characters is True.\n\n    Returns:\n        bool: True if the password is valid based on the specified criteria, False otherwise.\n    ';A=password
	if len(A)<length:return _A
	if upper:
		if not any(A.isupper()for A in A):return _A
	if lower:
		if not any(A.islower()for A in A):return _A
	if digit:
		if not any(A.isdigit()for A in A):return _A
	if overwrite_special_characters:B=overwritten_special_characters
	else:B=_C
	if not any(A in B for A in A):return _A
	return _B
def validate_strong_password(password):'\n    Validate if a given password meets the criteria for a strong password.\n\n    A strong password must satisfy the following conditions:\n    - Have a minimum length of 12 characters.\n    - Contain at least one uppercase letter.\n    - Contain at least one lowercase letter.\n    - Contain at least one digit.\n    - Optionally, special characters can be included, with the possibility to overwrite the default set of characters.\n\n    Args:\n        password (str): The password string to be validated.\n\n    Returns:\n        bool: True if the password meets the strong password criteria, False otherwise.\n    ';return validate_password(password,12,upper=_B,lower=_B,digit=_B,overwrite_special_characters=_B,overwritten_special_characters=_C)
def validate_credit_card(number):
	'\n    Validates a credit card number using the Luhn algorithm.\n\n    This function takes an integer representing a credit card number and performs the\n    Luhn algorithm to determine its validity.\n\n    The Luhn algorithm, also known as the "modulus 10" or "mod 10" algorithm, is a\n    simple checksum formula used to validate a variety of identification numbers,\n    including credit card numbers. It works by performing a series of mathematical\n    operations on the digits of the credit card number and checking whether the\n    resulting sum is divisible by 10.\n\n    Args:\n        number (int): The credit card number to be validated.\n\n    Returns:\n        bool: True if the credit card number is valid according to the Luhn algorithm,\n            False otherwise.\n    ';A=number;A=A.replace(' ','').replace('-','')
	if not A.isdigit():return _A
	C=A[::-1];D=0
	for E in range(len(C)):
		B=int(C[E])
		if E%2==1:B*=2
		if B>9:B-=9
		D+=B
	return D%10==0
def isStr(input_string):'Return True if the given input is a string, False otherwise.\n\n    This function is an alternative for checking if a variable is a string with the\n    isinstance built-in function.\n\n    Args:\n        input_string (str): The input to check if it is a string.\n\n    Returns:\n        bool: True if the input is a string, False otherwise.\n    ';return isinstance(input_string,str)
def isDic(input_string):'\n    This function is an alternative for checking if a variable is a dictionary with the\n    isinstance built-in function.\n\n    Args:\n        input_string (Any): The input object to check.\n\n    Returns:\n        bool: True if the input is a dictionary object, False otherwise.\n    ';return isinstance(input_string,dict)
def isInt(input_string):'\n    This function is an alternative for checking if a variable is an integer with the\n    isinstance built-in function.\n\n    Args:\n        input_string (any): The variable to be checked.\n\n    Returns:\n        bool: True if input_string is an integer, False otherwise.\n    ';return isinstance(input_string,int)
def isFloat(input_string):'\n    This function is an alternative for checking if a variable is a float with the\n    isinstance built-in function.\n\n    Args:\n        input_string (any): The input value to check.\n\n    Returns:\n        bool: True if the input value is a float, False otherwise.\n    ';return isinstance(input_string,float)
def check_valid_ipv6(ip_address):
	'\n    Check the validity of an IPv6 address.\n\n    This function takes an IPv6 address in string format and attempts to create an IPv6Address\n    object from the \'ip_address\' parameter. If the address is valid, the function returns True;\n    otherwise, it returns False.\n\n    Parameters:\n    ip_address (str): A string representing the IPv6 address to be checked.\n\n    Returns:\n    bool: True if the IPv6 address is valid, False if it is not.\n\n    Example:\n    >>> check_valid_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334")\n    True\n    >>> check_valid_ipv6("invalid_address")\n    False\n    '
	try:A=IPv6Address(ip_address);return _B
	except AddressValueError:return _A
def check_valid_ipv4(ip_address):
	'\n    Check the validity of an IPv4 address.\n\n    This function takes an IPv4 address in string format and attempts\n    to create an IPv4Address object from the `ipaddress` module. If the\n    address is valid, the function returns True. If the address is not\n    a valid IPv4 address, it returns False.\n\n    Args:\n        ip_address (str): The IPv4 address to be checked.\n\n    Returns:\n        bool: True if the input is a valid IPv4 address, False otherwise.\n    '
	try:A=IPv4Address(ip_address);return _B
	except AddressValueError:return _A
def compare(file1,file2):'\n    Compare two files and return a boolean indicating whether they are equal or not.\n\n    Args:\n        file1 (str): The path to the first file.\n        file2 (str): The path to the second file.\n\n    Returns:\n        bool: True if the files are equal, False otherwise.\n    ';return file1==file2