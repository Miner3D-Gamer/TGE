from..import SYSTEM_NAME
if SYSTEM_NAME=='windows':from.clipboard.clipboard_windows import*;from.keyboard.windows.keyboard import press_key,key_to_virtual_key
else:from.clipboard.clipboard_pyperclip import*;from.keyboard.linux.keyboard import press_key,key_to_virtual_key
def save_clipboard_to_file(file_path):
 try:file=open(file_path,'w',encoding='utf-8');file.write(get_clipboard());file.close();return True
 except:return False
def load_clipboard_from_file(file_path):
 try:file=open(file_path,'r',encoding='utf-8');text=file.read();file.close();copy_to_clipboard(text);return True
 except:return False
def append_to_clipboard(text):clip=get_clipboard();clip+=text;copy_to_clipboard(clip)
def prepend_to_clipboard(text):clip=get_clipboard();clip=text+clip;copy_to_clipboard(clip)
def get_clipboard_size():return len(get_clipboard())
def get_clipboard_file_extension():return get_clipboard().split('.')[-1]
def paste_clipboard():
 clipboard=get_clipboard()
 for line in clipboard.splitlines(True):
  for character in line:press_key(key_to_virtual_key(character))