_B='middle'
_A=False
from..cursor_operations import WHEEL_DELTA
import pyautogui as pygui
def getScreenDimensions():return pygui.size()
SCREEN_WIDTH,SCREEN_HEIGHT=getScreenDimensions()
def mouseTo(x,y):pygui.moveTo(x,y)
def mouseGet():return pygui.position()
def Click():pygui.click(_pause=_A)
def RightClick():pygui.rightClick(_pause=_A)
def MiddleClick():pygui.middleClick(_pause=_A)
def ScrollV(clicks,wheel_delta=WHEEL_DELTA):0
def ScrollH(clicks,wheel_delta=WHEEL_DELTA):0
def Scroll(clicks,wheel_delta=WHEEL_DELTA):pygui.scroll(clicks,_pause=_A)
def LeftMouseDown():pygui.keyDown('left',_pause=_A)
def RightMouseDown():pygui.keyDown('right',_pause=_A)
def MiddleMouseDown():pygui.keyDown(_B,_pause=_A)
def LeftMouseUp():pygui.keyUp('left',_pause=_A)
def RightMouseUp():pygui.keyUp('right',_pause=_A)
def MiddleMouseUp():pygui.keyUp(_B,_pause=_A)