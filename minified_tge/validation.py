_C='!@#$%^&*()_-+=<>?/\\'
_B=True
_A=False
import re,requests
from ipaddress import IPv4Address,IPv6Address,AddressValueError
from.manipulation.string_utils import reverse_string
def is_empty(text):return text==''
def is_prime(number):
	A=number
	if A<=1:return _A
	for B in range(2,A):
		if A%B==0:return _A
	return _B
def is_palindrome(string):A=string;return A==reverse_string(A)
def is_leap_year(year):A=year;return A%4==0 and(A%100!=0 or A%400==0)
def is_even(number):return number%2==0
def is_odd(number):return number%2==1
def is_url(url):A=re.compile('^(?:http|https)://(?:[\\w-]+\\.)*[\\w-]+(?:\\.[a-zA-Z]{2,})(?:/?|(?:/[^\\s]+)+)?$');return bool(re.match(A,url))
def is_url_available(url,check_url=_B):
	A=check_url
	if A:A=not is_url(url)
	if not A:return _A
	try:
		B=requests.get(url)
		if B.status_code==200:return _B
		else:return _A
	except requests.exceptions.ConnectionError or requests.exceptions.ConnectTimeout:return
def validate_email(email):A='^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$';return re.match(A,email)is not None
def validate_password(password,length,upper,lower,digit,overwrite_special_characters,overwritten_special_characters):
	A=password
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
def validate_strong_password(password):return validate_password(password,12,upper=_B,lower=_B,digit=_B,overwrite_special_characters=_B,overwritten_special_characters=_C)
def validate_credit_card(number):
	A=number;A=A.replace(' ','').replace('-','')
	if not A.isdigit():return _A
	C=A[::-1];D=0
	for E in range(len(C)):
		B=int(C[E])
		if E%2==1:B*=2
		if B>9:B-=9
		D+=B
	return D%10==0
def isStr(input_string):return isinstance(input_string,str)
def isDic(input_string):return isinstance(input_string,dict)
def isInt(input_string):return isinstance(input_string,int)
def isFloat(input_string):return isinstance(input_string,float)
def check_valid_ipv6(ip_address):
	try:A=IPv6Address(ip_address);return _B
	except AddressValueError:return _A
def check_valid_ipv4(ip_address):
	try:A=IPv4Address(ip_address);return _B
	except AddressValueError:return _A
def compare(file1,file2):return file1==file2