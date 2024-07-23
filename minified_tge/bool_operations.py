_A=False
from typing import List
from collections.abc import Iterable
def and_three(a,b,c):return a and b and c
def and_four(a,b,c,d):return a and b and c and d
def and_five(a,b,c,d,e):return a and b and c and d and e
def and_six(a,b,c,d,e,f):return a and b and c and d and e and f
def and_seven(a,b,c,d,e,f,g):return a and b and c and d and e and f and g
def and_eight(a,b,c,d,e,f,g,h):return a and b and c and d and e and f and g and h
def and_nine(a,b,c,d,e,f,g,h,i):return a and b and c and d and e and f and g and h and i
def and_ten(a,b,c,d,e,f,g,h,i,j):return a and b and c and d and e and f and g and h and i and j
def or_three(a,b,c):return a or b or c
def or_four(a,b,c,d):return a or b or c or d
def or_five(a,b,c,d,e):return a or b or c or d or e
def or_six(a,b,c,d,e,f):return a or b or c or d or e or f
def or_seven(a,b,c,d,e,f,g):return a or b or c or d or e or f or g
def or_eight(a,b,c,d,e,f,g,h):return a or b or c or d or e or f or g or h
def or_nine(a,b,c,d,e,f,g,h,i):return a or b or c or d or e or f or g or h or i
def or_ten(a,b,c,d,e,f,g,h,i,j):return a or b or c or d or e or f or g or h or i or j
def nand(a,b):return not(a and b)
def nand_three(a,b,c):return not(a and b and c)
def nand_any(*A):return not all(A)
def xor(a,b):return a^b
def xor_three(a,b,c):return a^b^c
def xor_any(*A):return sum(A)%2==1
def xnor(a,b):return not a^b
def xnor_three(a,b,c):return not a^b^c
def xnor_any(*A):return sum(A)%2==0
def mux(a,b,c):return a if c else b
def mux_four(a,b,c,d,sel_1,sel_0):A=[a,b,c,d];B=sel_1<<1|sel_0;return A[B]
def mux_eight(a,b,c,d,e,f,g,h,sel_2,sel_1,sel_0):A=[a,b,c,d,e,f,g,h];B=sel_2<<2|sel_1<<1|sel_0;return A[B]
def mux_any(inputs,selectors):
	B=selectors;A=inputs
	if len(A)!=2**len(B):raise ValueError('Number of inputs must be 2^n where n is the number of selectors.')
	C=0
	for(D,E)in enumerate(reversed(B)):C|=E<<D
	return A[C]
def nor(a,b,c):return not(a or b)
def nor_three(a,b,c):return not(a or b or c)
def nor_any(*A):return not any(A)
def binary_to_gray(b3,b2,b1,b0):A=b3;B=b3^b2;C=b2^b1;D=b1^b0;return A,B,C,D
def demux(input,*B):
	A=len(B);C=[_A]*2**A;D=0
	for E in range(A):D|=B[E]<<A-1-E
	C[D]=input;return C
def half_adder(a,b):return xor(a,b),a and b
def full_adder(a,b,cin=_A):A,B=half_adder(a,b);C,D=half_adder(A,cin);return C,B or D
def four_bit_adder(a,b,carry=_A):A=carry;A,B=full_adder(a[3],b[3],A);A,C=full_adder(a[2],b[2],A);A,D=full_adder(a[1],b[1],A);A,E=full_adder(a[0],b[0],A);return E,D,C,B,A
def two_complement(b):A=tuple(not A for A in b);B=_A,_A,_A,True;return four_bit_adder(A,B)[0:4]
def four_bit_subtractor(a,b,borrow=_A):A=two_complement(b);B,C=four_bit_adder(a,A,borrow);return B+(C,)
def any_bit_adder(a,b,carry=_A):
	A=carry
	if len(a)!=len(b):raise ValueError('Input lists must have the same length')
	D=len(a);B=[]
	for C in range(D-1,-1,-1):E,A=full_adder(a[C],b[C],A);B.append(E)
	B.reverse();return B,A
def number_to_bools(num):
	A=num
	if A<0:raise ValueError('Input number must be non-negative')
	if A==0:B=1
	else:B=A.bit_length()
	C=bin(A)[2:];D=C.zfill(B);E=[A=='1'for A in D];return E
def bools_to_number(bools):
	A=bools;B=0;C=len(A)
	for D in range(C):
		if A[D]:B+=1<<C-1-D
	return B