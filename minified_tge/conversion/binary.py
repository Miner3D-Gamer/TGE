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