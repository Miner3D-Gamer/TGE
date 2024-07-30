_E='-lG'
_D='Window not found'
_C=True
_B=None
_A='wmctrl'
import subprocess
def is_window_minimized_linux(window_name):
 B=subprocess.run([_A,_E],stdout=subprocess.PIPE,text=_C);C=B.stdout.splitlines()
 for A in C:
  if window_name in A:D=A.split();E=D[8];return E=='0'
 return False
def minimize_window_linux(window_name):
 C=subprocess.run([_A,'-l'],stdout=subprocess.PIPE,text=_C);D=C.stdout.splitlines();A=_B
 for B in D:
  if window_name in B:A=B.split()[0];break
 if A is _B:raise ValueError(_D)
 subprocess.run([_A,'-i','-r',A,'-b','add,hidden'])
def get_window_position_linux(window_name):
 C=subprocess.run([_A,_E],stdout=subprocess.PIPE,text=_C);D=C.stdout.splitlines()
 for A in D:
  if window_name in A:B=A.split();E,F=int(B[2]),int(B[3]);return E,F
 raise ValueError(_D)
def maximize_window_linux(window_name):
 C=subprocess.run([_A,'-l'],stdout=subprocess.PIPE,text=_C);D=C.stdout.splitlines();A=_B
 for B in D:
  if window_name in B:A=B.split()[0];break
 if A is _B:raise ValueError(_D)
 subprocess.run([_A,'-i','-r',A,'-b','add,maximized_vert,maximized_horz'])
def set_window_position_linux(window_name,x,y,width,height):
 C=subprocess.run([_A,_E],stdout=subprocess.PIPE,text=_C);D=C.stdout.splitlines();A=_B
 for B in D:
  if window_name in B:A=B.split()[0];break
 if A is _B:raise ValueError(_D)
 subprocess.run([_A,'-i','-r',A,'-e',f"0,{x},{y},{width},{height}"])