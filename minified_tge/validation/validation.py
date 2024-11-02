#type: ignore
from ipaddress import IPv4Address,IPv6Address,AddressValueError
import re
_C='!@#$%^&*()_-+=<>?/\\'
_B=True
_A=False
from.import minecraft
from.import numbers
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
def check_valid_ipv6(ip_address):
 try:A=IPv6Address(ip_address)
 except AddressValueError:return _A
 else:return _B
def check_valid_ipv4(ip_address):
 try:A=IPv4Address(ip_address)
 except AddressValueError:return _A
 else:return _B
__all__=['minecraft','numbers','check_valid_ipv4','check_valid_ipv6','validate_email','validate_password','validate_strong_password','validate_credit_card']