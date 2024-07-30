from datetime import datetime
from time import timezone
def get_date():B=' ';A=datetime.now();C=datetime.weekday(A);A=str(A).replace('-',B).replace(':',B).replace('.',B).split(B);return int(A[0]),int(A[1]),int(A[2]),int(A[3]),int(A[4]),int(A[5]),int(C)
def get_timezone_offset():return int(timezone/3600)
def unix_converter(time):return datetime.fromtimestamp(time).strftime('%Y %m %d %H %M %S')