_D='middle'
_C='right'
_B='left'
_A=False
from..import SYSTEM_NAME
if SYSTEM_NAME=='windows':WINDOWS=True
else:WINDOWS=_A
if WINDOWS:
	import ctypes
	class POINT(ctypes.Structure):_fields_=[('x',ctypes.c_long),('y',ctypes.c_long)]
	USER32=ctypes.windll.user32;KERNEL32=ctypes.windll.kernel32;CURSOR_POINT=POINT();WHEEL_DELTA=120;MOUSE_EVENTF_MOVE=1;MOUSEEVENTF_LEFTDOWN=2;MOUSEEVENTF_LEFTUP=4;MOUSEEVENTF_RIGHTDOWN=8;MOUSEEVENTF_RIGHTUP=16;MOUSEEVENTF_MIDDLEDOWN=32;MOUSEEVENTF_MIDDLEUP=64;MOUSEEVENTF_WHEEL=2048;MOUSEEVENTF_HWHEEL=4096;MOUSE_EVENTF_ABSOLUTE=32768;CF_TEXT=1;CF_UNICODETEXT=13;GMEM_DDESHARE=8192;OPEN_EXISTING=3;GMEM_MOVEABLE=2;GMEM_ZEROINIT=64;GHND=GMEM_DDESHARE|GMEM_MOVEABLE
import pyautogui as pygui
if WINDOWS:from.cursor.cursor_operations_ctypes import*
else:from.cursor.cursor_operations_pynput import*
def ClickMouseButton(button_number):ClickMouseButtonList[button_number]()
def HoldMouseButton(button_number):HoldMouseButtonList[button_number]()
def ReleaseMouseButton(button_number):ReleaseMouseButtonList[button_number]()
def ClickMouseButtonAt(button_number,x,y):ClickMouseButtonAtList[button_number](x,y)
def LeftClick():Click()
def ClickAt(x,y):mouseTo(x,y);Click()
def DoubleClick():Click();Click()
def DoubleClickAt(x,y):mouseTo(x,y);Click();Click()
def TripleClick():Click();Click();Click()
def TripleClickAt(x,y):mouseTo(x,y);Click();Click();Click()
def RightClickAt(x,y):MouseTo(x,y);RightClick()
def DoubleRightClick():RightClick();RightClick()
def DoubleRightClickAt(x,y):mouseTo(x,y);RightClick();RightClick()
def TripleRightClickAt(x,y):mouseTo(x,y);RightClick();RightClick();RightClick()
def TripleRightClick():RightClick();RightClick();RightClick()
def MiddleClickAt(x,y):mouseTo(x,y);MiddleClick()
def DoubleMiddleClickAt(x,y):mouseTo(x,y);MiddleClick();MiddleClick()
def DoubleMiddleClick():MiddleClick();MiddleClick()
def TripleMiddleClick():MiddleClick();MiddleClick();MiddleClick()
def TripleMiddleClickAt(x,y):mouseTo(x,y);MiddleClick();MiddleClick();MiddleClick()
def drag_to(x,y):pygui.dragTo(x,y)
def drag_obj_to(x,y,a,b):mouseTo(x,y);hold_left_mouse();drag_to(a,b);release_left_mouse()
def hold_left_mouse():pygui.mouseDown(_B)
def release_left_mouse():pygui.mouseUp(_B)
def hold_right_mouse():pygui.mouseDown(_C)
def release_right_mouse():pygui.mouseUp(_C)
def hold_middle_mouse():pygui.mouseDown(_D)
def release_middle_mouse():pygui.mouseUp(_D)
def hold_mouse(mouse):
	if is_valid_mouse_buttons():pygui.mouseDown(mouse);return True
	else:return _A
def release_mouse(mouse):
	if is_valid_mouse_buttons(mouse):pygui.mouseUp(mouse);return True
	else:return _A
def is_valid_mouse_buttons(x):return x in[_B,_C,_D]
ClickMouseButtonList=[Click,MiddleClick,RightClick]
ClickMouseButtonAtList=[ClickAt,MiddleClickAt,RightClickAt]
HoldMouseButtonList=[LeftMouseDown,RightMouseDown,MiddleMouseDown]
ReleaseMouseButtonList=[LeftMouseUp,RightMouseUp,MiddleMouseUp]