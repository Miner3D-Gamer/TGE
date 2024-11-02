#type: ignore
from random import shuffle
from hashlib import sha256
__all__=['get_hello_world','print_hello_world']
def get_hello_world(reminder_start=10000,reminder_every=10):
 D=b'\x7f\x83\xb1e\x7f\xf1\xfcS\xb9-\xc1\x81H\xa1\xd6]\xfc-K\x1f\xa3\xd6w(J\xdd\xd2\x00\x12m\x90i'
 def E(word):A=list(word);shuffle(A);return''.join(A)
 A=0;B=reminder_start
 while True:
  A+=1
  if A%B==reminder_every:print(f"At {A} attempts");B*=10
  C=E('Hell oWl!dor')
  if sha256(C.encode()).digest()==D:break
 return C,A
def print_hello_world():print('%s in %s attempts'%get_hello_world(reminder_start=-1))