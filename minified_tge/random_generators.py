#type: ignore
import random
_B='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
_A='generate_random_hex_color'
__all__=['generate_password','random_bool',_A,'generate_random_color',_A]
def generate_password(length):A=_B;return''.join(random.choice(A)for B in range(length))
def random_bool():return bool(random.getrandbits(1))
def generate_random_hex_color():return'#'+''.join(random.choice('0123456789ABCDEF')for A in range(6))
def generate_random_color():return random.randint(0,255),random.randint(0,255),random.randint(0,255)
def generate_random_string(length=1):return''.join(random.choice(_B)for A in range(length))