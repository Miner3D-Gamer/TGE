from.import minecraft as minecraft,numbers as numbers
__all__=['minecraft','numbers','check_valid_ipv4','check_valid_ipv6','validate_email','validate_password','validate_strong_password','validate_credit_card']
def validate_email(email:str)->bool:...
def validate_password(password:str,length:int,upper:bool,lower:bool,digit:bool,overwrite_special_characters:bool,overwritten_special_characters:str)->bool:...
def validate_strong_password(password:str)->bool:...
def validate_credit_card(number:str)->bool:...
def check_valid_ipv6(ip_address:str)->bool:...
def check_valid_ipv4(ip_address:str)->bool:...