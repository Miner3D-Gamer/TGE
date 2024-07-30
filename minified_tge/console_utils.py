_C=False
_B=True
_A=None
import time,os
from random import random,choice
import sys
from.tbe import determine_affirmative
__all__=['typingPrint']
if os.name=='nt':
 def clear():os.system('cls')
else:
 def clear():os.system('clear')
def typingPrint(text,delay):
 A=delay
 if not A>0:A=.05
 for B in text:sys.stdout.write(B);sys.stdout.flush();time.sleep(A)
def typingInput(text,delay=0):
 A=delay
 if not A>0:A=.05
 for B in text:sys.stdout.write(B);sys.stdout.flush();time.sleep(A)
 C=input('');return C
def writeSentencesToConsole(punctuations,o_text,type_delay,line_delay):
 H=type_delay;G='Þ';E=line_delay;D=punctuations;A=o_text
 try:
  A=str(A)
  if type(D)!=list:D[D]
 except:return _C
 D=['.','!','?',':',';']
 for I in D:A=A.replace(I,I+G)
 F=A.split(G);B=0;C=0
 if not E>=0:E=.7
 typingPrint(A[C:len(F[B])+C],H);time.sleep(E);C+=len(F[B])+1;B+=1
 for K in range(A.count(G)-1):
  print(' ');time.sleep(E);J=A[C:len(F[B])+C][1:]
  if not J=='':typingPrint(J,H)
  C+=len(F[B])+1;B+=1
 return _B
def chooseFromTextMenu(text,prompt,ans_prompt):
 B=text;C=_B;print(prompt)
 while C:
  for D in range(len(B)):typingPrint(f"{D}: {B[D]}");print(' ');time.sleep(.05)
  time.sleep(.25);A=typingInput(ans_prompt)
  try:
   if A in B:return B.index(A)
   A=int(A);print('')
  except:print('')
  if type(A)==int:
   if A<=len(B)and A>=0:C=_C;return int(A)
def skip_line():print('\n')
def print_table(data):
 A='+'
 try:
  B=[max(len(str(A))for A in A)for A in zip(*data)];C=A+A.join('-'*(A+2)for A in B)+A;print(C)
  for D in data:E='| '+' | '.join(str(A).ljust(B)for(A,B)in zip(D,B))+' |';print(E)
  print(C);return _B,''
 except:return _C,'Unable to print table, make sure the data is a list of lists'
def progress_bar(progress_name,current,total,length,show_float=_B,empty_tile='-',full_tile='#'):
 E=length;D=progress_name;B=total;A=current
 if show_float:C=float(int(float(A/B*100)*10)/10)
 else:C=int(A/B*100)
 F=int(E*A//B);G=f"{full_tile}"*F+f"{empty_tile}"*(E-F)
 if D=='':sys.stdout.write(f"\r[{G}] {C}%");sys.stdout.flush()
 else:sys.stdout.write(f"\r{D}: [{G}] {C}%");sys.stdout.flush()
def colorize_text(text,color):
 C='reset';B=color;A={'black':'\x1b[30m','red':'\x1b[31m','green':'\x1b[32m','yellow':'\x1b[33m','blue':'\x1b[34m','magenta':'\x1b[35m','cyan':'\x1b[36m','white':'\x1b[37m','bright_black':'\x1b[90m','bright_red':'\x1b[91m','bright_green':'\x1b[92m','bright_yellow':'\x1b[93m','bright_blue':'\x1b[94m','bright_magenta':'\x1b[95m','bright_cyan':'\x1b[96m','bright_white':'\x1b[97m','bg_black':'\x1b[40m','bg_red':'\x1b[41m','bg_green':'\x1b[42m','bg_yellow':'\x1b[43m','bg_blue':'\x1b[44m','bg_magenta':'\x1b[45m','bg_cyan':'\x1b[46m','bg_white':'\x1b[47m','bg_bright_black':'\x1b[100m','bg_bright_red':'\x1b[101m','bg_bright_green':'\x1b[102m','bg_bright_yellow':'\x1b[103m','bg_bright_blue':'\x1b[104m','bg_bright_magenta':'\x1b[105m','bg_bright_cyan':'\x1b[106m','bg_bright_white':'\x1b[107m',C:'\x1b[0m'}
 if B not in A:raise ValueError('Invalid color specified.')
 return A[B]+text+A[C]
def visualize_directory(path,prefix='',lines=_A):
 H='├──';G='└──';B=prefix;A=lines
 if A is _A:A=[]
 if B=='':I=os.path.basename(path);A.append(f"[{I}]")
 C=_C
 try:
  with os.scandir(path)as D:
   D=list(D)
   for(J,E)in enumerate(D):
    C=J==len(D)-1;F=G if C else H
    if E.is_dir():A.append(f"{B}{F}[{E.name}]");K=B+'│   'if not C else B+'    ';visualize_directory(E.path,K,A)
    else:A.append(f"{B}{F}/{E.name}")
 except PermissionError:F=G if C else H;A.append(f"{B}{F}(Access Denied)")
 return A
def clear_lines(num_lines,move_front=_C):
 A='\x1b[F';sys.stdout.write(A*num_lines);sys.stdout.write('\x1b[K')
 if move_front:sys.stdout.write(A)
def prompt_bool(question,allow_undeterminable=_C,tries=0,delete_lines=_B,return_value_when_tries_are_depleted=_A):
 C=tries;D=0
 while _B:
  D+=1;A=str(input(question)).lower();B=determine_affirmative(A)
  if B is not _A:return B,A
  elif allow_undeterminable:return B,A
  if C>0:
   if D>=C:return return_value_when_tries_are_depleted,A
  if delete_lines:clear_lines(1)
def prompt_number(question,min=_A,max=_A,incorrect=_A,error=_A,delete_lines=_B,tries=0,try_return=_A):
 G=delete_lines;F=error;E=incorrect;C=try_return;B=tries;D=0
 while _B:
  D+=1
  try:
   A=int(input(question))
   if min is _A or max is _A:return A
   elif min<=A<=max:return A
   else:
    if B>0:
     if D>=B:
      if C is not _A:return C(A)
      else:return
    if G:clear_lines(1)
    if E is not _A:return E(A)
  except:
   if B>0:
    if D>=B:
     if C is not _A:return C(A)
     else:return
   if G:clear_lines(1)
   if F is not _A:return F(A)
def matrix_rain(rows,columns,speed=.1,density=.2,duration=_A,symbols=['0','1']):
 E=duration;D=columns;C=rows;global tge_matrix_console_stop;tge_matrix_console_stop=_C;H=time.time();A=[[' 'for A in range(D)]for A in range(C)]
 while _B:
  for B in range(D):
   if random()<density:A[0][B]=choice(symbols)
   else:A[0][B]=' '
  for B in range(C-1,0,-1):
   for F in range(D):A[B][F]=A[B-1][F]
  G='';I=0
  for J in A[1:]:G+=''.join(J)+'\n';I+=1
  clear_lines(C+1);print(G)
  if E is not _A:
   if time.time()-H>E:break
  elif tge_matrix_console_stop:break
  time.sleep(speed)
from io import StringIO
class ConsoleCapture:
 def __init__(A):A.original_stdout=sys.stdout;A.captured_output=StringIO();A.capturing=_C
 def start_capture(A):
  if A.capturing==_C:sys.stdout=A.captured_output
 def stop_capture(A):
  if A.capturing==_B:sys.stdout=A.original_stdout
 def get_captured_output(A):A.captured_output.seek(0);return A.captured_output.read()
def suppress_print():global console_capture;console_capture=ConsoleCapture();console_capture.start_capture()
def enable_print():global console_capture;console_capture.stop_capture();A=console_capture.get_captured_output();return A