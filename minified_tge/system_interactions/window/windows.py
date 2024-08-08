import ctypes.wintypes
from..shared import*
from ctypes import wintypes
class RECT(ctypes.Structure):_fields_=[('left',wintypes.LONG),('top',wintypes.LONG),('right',wintypes.LONG),('bottom',wintypes.LONG)]
def is_window_minimized(hwnd,user32=USER32):return user32.IsIconic(hwnd)!=0
def minimize_window(hwnd,user32=USER32):user32.ShowWindow(hwnd,6)
def maximize_window(hwnd):ctypes.windll.user32.ShowWindow(hwnd,3)
def get_window_position(hwnd):
 rect=RECT();ctypes.windll.user32.GetWindowRect(hwnd,ctypes.byref(rect))
 if rect.left==-32000 and rect.top==-32000:return
 return rect.left,rect.top,rect.right-rect.left,rect.bottom-rect.top
def set_window_position(hwnd,x,y,width,height):SWP_NOSIZE=1;SWP_NOZORDER=4;flags=SWP_NOZORDER|SWP_NOSIZE;return ctypes.windll.user32.SetWindowPos(hwnd,None,x,y,width,height,flags)
def get_window_by_title(title):return ctypes.windll.user32.FindWindowW(None,title)