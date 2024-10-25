from..import SYSTEM_NAME
if SYSTEM_NAME=='windows':from.clipboard.clipboard_windows import get_clipboard,copy_to_clipboard,clear_clipboard;from.keyboard.windows import press_key,key_to_virtual_key
else:from.clipboard.clipboard_pyperclip import get_clipboard,copy_to_clipboard,clear_clipboard;from.keyboard.linux import press_key,key_to_virtual_key
def save_clipboard_to_file(file_path):
 A=get_clipboard()
 try:
  with open(file_path,'w',encoding='utf-8')as B:B.write(A if A else'')
  return True
 except:return False
def load_clipboard_from_file(file_path):
 try:A=open(file_path,'r',encoding='utf-8');B=A.read();A.close();copy_to_clipboard(B);return True
 except:return False
def append_to_clipboard(text):A=get_clipboard();A+=text;copy_to_clipboard(A)
def prepend_to_clipboard(text):A=get_clipboard();A=text+A;copy_to_clipboard(A)
def get_clipboard_size():return len(get_clipboard())
def get_clipboard_file_extension():return get_clipboard().split('.')[-1]
def write_out_clipboard():
 A=get_clipboard()
 for B in A.splitlines(True):
  for C in B:press_key(key_to_virtual_key(C))