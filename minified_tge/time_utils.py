#type: ignore
from datetime import datetime
import time
_A=None
class Timer:
 def __init__(A,start_time,offset=0):A.start_time=start_time;A.offset=offset
 def add_time(A,amount):A.offset+=amount;return A.offset
 def subtract_time(A,amount):A.offset-=amount;return A.offset
 def get_timer_start_time(A):return A.start_time
 def get_timer_offset(A):return A.offset
 def set_start_time(A,value):A.start_time=value
 def set_offset(A,value):A.offset=value
 def get_time(A):return time.time()-A.start_time+A.offset
class TimerManager:
 def __init__(A):A.timers={}
 def start_timer(A,timer_name):A.timers[timer_name]=Timer(time.time())
 def stop_timer(B,timer_name):
  A=B.timers.pop(timer_name,_A)
  if not A is _A:return A.get_time()
  return-1
 def get_timer(B,timer_name):
  A=B.timers.get(timer_name,_A)
  if not A is _A:return A.get_time()
  return-1
 def does_timer_exist(A,timer_name):return timer_name in A.timers
 def get_all_timers(A):return[A for A in A.timers]
 def add_time_to_timer(B,timer_name,amount):
  A=B.timers.get(timer_name,_A)
  if not A is _A:return A.add_time(amount)
  return-1.
 def remove_time_from_timer(B,timer_name,amount):
  A=B.timers.get(timer_name,_A)
  if not A is _A:return A.subtract_time(amount)
  return-1.
def get_date():B=' ';C=datetime.now();D=datetime.weekday(C);A=str(C).replace('-',B).replace(':',B).replace('.',B).split(B);return int(A[0]),int(A[1]),int(A[2]),int(A[3]),int(A[4]),int(A[5]),int(D)
def get_timezone_offset():return int(time.timezone/3600)
def unix_converter(time):return datetime.fromtimestamp(time).strftime('%Y %m %d %H %M %S')