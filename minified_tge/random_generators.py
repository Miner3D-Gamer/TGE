_A='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
import random
from requests import get as requests_get
from.codec.codec import html
def generate_name(gender):
 D='both';A=gender
 if A==0 or'm'or'male':A='m'
 elif A==1 or'f'or'female':A='f'
 elif A==2 or'u'or'unisex'or'unidentified':A='u'
 elif A==3 or D or'b':A=D
 else:raise ValueError('Invalid gender input.')
 E='https://www.behindthename.com/random/random.php';F={'gender':A,'number':'1','sets':'1','surname':'','all':'yes'};G=requests_get(E,params=F);B=str(G.text.split('\n')[165]);H=B.find('class="plain">')+14;B=B[H:];I=B.find('<');C=B[:I];C=html.decode(C);return C
def generate_password(length):A=_A;return''.join(random.choice(A)for B in range(length))
def random_bool():return bool(random.getrandbits(1))
def generate_random_hex_color():return'#'+''.join(random.choice('0123456789ABCDEF')for A in range(6))
def generate_random_color():return random.randint(0,255),random.randint(0,255),random.randint(0,255)
def generate_random_string(length=1):return''.join(random.choice(_A)for A in range(length))
def random_int(min,max,float=False):
 if min<max:
  if float:return random.uniform(min,max)
  else:return random.randint(min,max)
 elif min==max:return min
 else:return 0