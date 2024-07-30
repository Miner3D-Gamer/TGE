from..import SYSTEM_NAME
from.shared import*
if SYSTEM_NAME=='windows':from.cursor.cursor_operations_ctypes import*
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