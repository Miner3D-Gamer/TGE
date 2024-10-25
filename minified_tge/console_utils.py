_D=False
_C='\n'
_B=True
_A=None
import time,os
from random import random,choice
import sys
from.tbe import determine_affirmative
if os.name=='nt':
 def clear():os.system('cls')
else:
 def clear():os.system('clear')
def typing_print(text,delay):
 A=delay
 if not A>0:A=.05
 for B in text:sys.stdout.write(B);sys.stdout.flush();time.sleep(A)
def typingInput(text,delay=0):
 A=delay
 if not A>0:A=.05
 for B in text:sys.stdout.write(B);sys.stdout.flush();time.sleep(A)
 C=input('');return C
def write_sentences_to_console(text,type_delay,line_delay=.7):
 for A in text:typing_print(A,type_delay);time.sleep(line_delay)
def choose_from_text_menu(menu_list,prompt='',destroy=_D):
 H=destroy;G=prompt;B=menu_list;raise BaseException('This function needs a revamp :/');C='';D=C.count(_C)+G.count(_C)+2
 for(E,F)in enumerate(B):C+=f"{E+1}: {F}\n"
 while _B:
  print(C);A=input(G)
  if A.isdigit():
   A=int(A)
   if A>0 and A<len(B)+1:
    if H:clear_lines(D)
    return A-1
  else:
   for(E,F)in enumerate(B):
    if A==F:
     if H:clear_lines(D)
     return E
  clear_lines(D)
def skip_line():print(_C)
def print_table(data):
 B='+';A='';C=[max(len(str(A))for A in A)for A in zip(*data)];D=B+B.join('-'*(A+2)for A in C)+B;A+=D+_C
 for E in data:F='| '+' | '.join(str(A).ljust(B)for(A,B)in zip(E,C))+' |';A+=F+_C
 A+=D;return A
def progress_bar(progress_name,current,total,length,show_float=_B,empty_tile='-',full_tile='#'):
 E=length;D=progress_name;B=total;A=current;A+=1
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
 B=prefix;A=lines
 if A is _A:A=[]
 if B=='':I=os.path.basename(path);A.append(f"[{I}]")
 C=_D;F='└──';G='├──';J='│   ';K='   '
 try:
  with os.scandir(path)as L:
   H=list(L)
   for(M,D)in enumerate(H):
    C=M==len(H)-1;E=F if C else G
    if D.is_dir():A.append(f"{B}{E}[{D.name}]");N=B+J if not C else B+K;visualize_directory(D.path,N,A)
    else:A.append(f"{B}{E}/{D.name}")
 except PermissionError:E=F if C else G;A.append(f"{B}{E}(Access Denied)")
 return A
def clear_lines(num_lines,move_front=_D):
 A='\x1b[F';sys.stdout.write(A*num_lines);sys.stdout.write('\x1b[K')
 if move_front:sys.stdout.write(A)
def prompt_bool(question,allow_undeterminable=_D,tries=0,delete_lines=_B):
 C=tries;D=0
 while _B:
  D+=1;A=str(input(question)).lower();B=determine_affirmative(A)
  if not B is _A:return B,A
  if allow_undeterminable:return B,A
  if C>0:
   if D>=C:return _A,A
  if delete_lines:clear_lines(1)
def prompt_number(question,min=_A,max=_A,delete_lines=_B,tries=0):
 B=tries;C=0
 while _B:
  if B>0:
   if C>=B:return
  C+=1;D=input(question)
  if delete_lines:clear_lines(1)
  if not D.isdigit():continue
  A=int(D)
  if not min is _A:
   if A<min:continue
  if not max is _A:
   if A>max:continue
  else:return A
def matrix_rain(rows,columns,speed=.1,density=.2,duration=_A,symbols=['0','1'],callable_stop_if_return_true=lambda:_D):
 E=duration;D=columns;C=rows;H=time.time();A=[[' 'for A in range(D)]for A in range(C)]
 while _B:
  for B in range(D):
   if random()<density:A[0][B]=choice(symbols)
   else:A[0][B]=' '
  for B in range(C-1,0,-1):
   for F in range(D):A[B][F]=A[B-1][F]
  G='';I=0
  for J in A[1:]:G+=''.join(J)+_C;I+=1
  clear_lines(C+1);print(G)
  if E is not _A:
   if time.time()-H>E:break
  if callable_stop_if_return_true():break
  time.sleep(speed)
class SuppressPrint:
 def __enter__(A):A._original_stdout=sys.stdout;sys.stdout=open(os.devnull,'w')
 def __exit__(A,exc_type,exc_value,traceback):sys.stdout.close();sys.stdout=A._original_stdout