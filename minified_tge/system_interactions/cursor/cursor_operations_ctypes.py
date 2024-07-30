from..shared import ctypes
class POINT(ctypes.Structure):_fields_=[('x',ctypes.c_long),('y',ctypes.c_long)]
CURSOR_POINT=POINT()
WHEEL_DELTA=120
MOUSE_EVENTF_MOVE=1
MOUSEEVENTF_LEFTDOWN=2
MOUSEEVENTF_LEFTUP=4
MOUSEEVENTF_RIGHTDOWN=8
MOUSEEVENTF_RIGHTUP=16
MOUSEEVENTF_MIDDLEDOWN=32
MOUSEEVENTF_MIDDLEUP=64
MOUSEEVENTF_WHEEL=2048
MOUSEEVENTF_HWHEEL=4096
MOUSE_EVENTF_ABSOLUTE=32768
CF_TEXT=1
OPEN_EXISTING=3
GMEM_ZEROINIT=64
def getScreenDimensions():return ctypes.windll.user32.GetSystemMetrics(0),ctypes.windll.user32.GetSystemMetrics(1)
SCREEN_WIDTH,SCREEN_HEIGHT=getScreenDimensions()
def mouseTo(x,y,screen_width=SCREEN_WIDTH,screen_height=SCREEN_HEIGHT):A=int(65535*(x/screen_width));B=int(65535*(y/screen_height));ctypes.windll.user32.mouse_event(MOUSE_EVENTF_MOVE|MOUSE_EVENTF_ABSOLUTE,A,B,0,0)
def mouseGet():ctypes.windll.user32.GetCursorPos(ctypes.byref(CURSOR_POINT));return CURSOR_POINT.x,CURSOR_POINT.y
def LeftClick():ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN,0,0,0,0);ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP,0,0,0,0)
def RightClick():ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTDOWN,0,0,0,0);ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTUP,0,0,0,0)
def MiddleClick():ctypes.windll.user32.mouse_event(MOUSEEVENTF_MIDDLEDOWN,0,0,0,0);ctypes.windll.user32.mouse_event(MOUSEEVENTF_MIDDLEUP,0,0,0,0)
def ScrollV(clicks,wheel_delta=WHEEL_DELTA):ctypes.windll.user32.mouse_event(MOUSEEVENTF_WHEEL,0,0,wheel_delta*clicks,0)
def ScrollH(clicks,wheel_delta=WHEEL_DELTA):ctypes.windll.user32.mouse_event(MOUSEEVENTF_HWHEEL,0,0,wheel_delta*clicks,0)
def Scroll(dx=None,dy=None,wheel_delta_x=WHEEL_DELTA,wheel_delta_y=WHEEL_DELTA):
 if dx:ScrollH(dx,wheel_delta=wheel_delta_x)
 if dy:ScrollV(dy,wheel_delta=wheel_delta_y)
def LeftMouseDown():ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTDOWN,0,0,0,0)
def RightMouseDown():ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
def MiddleMouseDown():ctypes.windll.user32.mouse_event(MOUSEEVENTF_MIDDLEDOWN,0,0,0,0)
def LeftMouseUp():ctypes.windll.user32.mouse_event(MOUSEEVENTF_LEFTUP,0,0,0,0)
def RightMouseUp():ctypes.windll.user32.mouse_event(MOUSEEVENTF_RIGHTUP,0,0,0,0)
def MiddleMouseUp():ctypes.windll.user32.mouse_event(MOUSEEVENTF_MIDDLEUP,0,0,0,0)