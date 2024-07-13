def b_lshift(a,b):return a<<b
def b_rshift(a,b):return a>>b
def b_and(a,b):return a&b
def b_or(a,b):return a|b
def b_xor(a,b):return a^b
def b_not(a):return~a
def b_nand(a,b):return~(a&b)
def b_nor(a,b):return~(a|b)
def b_nxor(a,b):return~(a^b)
def b_three_nand(a,b,c):return~(a&b&c)&1
def b_three_nor(a,b,c):return~(a|b|c)&1
def b_three_nxor(a,b,c):return~(a^b^c)&1
def b_three_xor(a,b,c):return~(a^b^c)