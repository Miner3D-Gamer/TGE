from..import SYSTEM_NAME
if SYSTEM_NAME=='windows':
 import ctypes
 class POINT(ctypes.Structure):_fields_=[('x',ctypes.c_long),('y',ctypes.c_long)]
 USER32=ctypes.windll.user32;KERNEL32=ctypes.windll.kernel32;CURSOR_POINT=POINT();WHEEL_DELTA=120;MOUSE_EVENTF_MOVE=1;MOUSEEVENTF_LEFTDOWN=2;MOUSEEVENTF_LEFTUP=4;MOUSEEVENTF_RIGHTDOWN=8;MOUSEEVENTF_RIGHTUP=16;MOUSEEVENTF_MIDDLEDOWN=32;MOUSEEVENTF_MIDDLEUP=64;MOUSEEVENTF_WHEEL=2048;MOUSEEVENTF_HWHEEL=4096;MOUSE_EVENTF_ABSOLUTE=32768;CF_TEXT=1;CF_UNICODETEXT=13;GMEM_DDESHARE=8192;OPEN_EXISTING=3;GMEM_MOVEABLE=2;GMEM_ZEROINIT=64;GHND=GMEM_DDESHARE|GMEM_MOVEABLE;from.cursor.cursor_operations_ctypes import*
else:from.cursor.cursor_operations_pynput import*
def ClickMouseButton(button_number):ClickMouseButtonList[button_number]()
def HoldMouseButton(button_number):HoldMouseButtonList[button_number]()
def ReleaseMouseButton(button_number):ReleaseMouseButtonList[button_number]()
def ClickMouseButtonAt(button_number,x,y):ClickMouseButtonAtList[button_number](x,y)
def LeftClickAt(x,y):mouseTo(x,y);LeftClick()
def DoubleLeftClick():LeftClick();LeftClick()
def DoubleLeftClickAt(x,y):mouseTo(x,y);LeftClick();LeftClick()
def RightClickAt(x,y):MouseTo(x,y);RightClick()
def DoubleRightClick():RightClick();RightClick()
def MiddleClickAt(x,y):mouseTo(x,y);MiddleClick()
def drag_to(x,y):LeftMouseDown();mouseTo(x,y);LeftMouseUp()
def drag_obj_to(x,y,a,b):mouseTo(x,y);drag_to(a,b)
ClickMouseButtonList=[LeftClick,MiddleClick,RightClick]
ClickMouseButtonAtList=[LeftClickAt,MiddleClickAt,RightClickAt]
HoldMouseButtonList=[LeftMouseDown,RightMouseDown,MiddleMouseDown]
ReleaseMouseButtonList=[LeftMouseUp,RightMouseUp,MiddleMouseUp]