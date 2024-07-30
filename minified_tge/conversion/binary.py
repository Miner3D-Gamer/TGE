_C='gigabytes'
_B='megabytes'
_A='kilobytes'
from math import ceil
HEX_CHARACTERS='0123456789ABCDEF'
def convert_binary_to_decimal(binary):
 A=0;B=0
 for C in reversed(str(binary)):
  if C=='1':A+=2**B
  B+=1
 return A
def convert_decimal_to_binary(decimal):
 A=decimal;B=''
 while A>0:B+=str(A%2);A//=2
 return B[::-1]
def convert_decimal_to_hexadecimal(decimal):
 A=decimal
 if A==0:return'0'
 B=''
 while A>0:C=A%16;D=HEX_CHARACTERS[C];B=D+B;A=A//16
 return B
def convert_hexadecimal_to_decimal(hexadecimal):
 A=hexadecimal
 if A=='0':return 0
 B=0
 for C in reversed(A):B=B*16+HEX_CHARACTERS.index(C)
def convert_bytes(value,from_unit,to_unit):
 C=to_unit;B=from_unit;A=['bytes',_A,_B,_C,'terabytes','petabytes','exabytes','zettabytes','yottabytes','brontobytes','geopbytes','xobibytes','yobibytes']
 if B not in A or C not in A:raise ValueError('Invalid unit specified')
 D=value*1024**A.index(B);return ceil(D/1024**A.index(C))
def convert_byte_to_kilobyte(bytes):return convert_bytes(bytes,'bytes',_A)
def convert_kilobyte_to_megabyte(kilobytes):return convert_bytes(kilobytes,_A,_B)
def convert_megabyte_to_gigabyte(megabytes):return convert_bytes(megabytes,_B,_C)