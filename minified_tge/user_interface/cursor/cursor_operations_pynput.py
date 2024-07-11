from..cursor_operations import WHEEL_DELTA
from...import PYAUTOGUI
import pynput
MOUSE=pynput.mouse.Controller()
if PYAUTOGUI:
	from pyautogui import size as pyautogui_size
	def getScreenDimensions():return pyautogui_size()
else:
	from...import TKINTER
	if TKINTER:
		from tkinter import Tk;TK_ROOT=Tk()
		def getScreenDimensions():return TK_ROOT.winfo_screenwidth(),TK_ROOT.winfo_screenheight()
	else:
		from...import SCREENINFO
		if SCREENINFO:
			from screeninfo import get_monitors
			def getScreenDimensions():
				D=get_monitors();A=0;B=0
				for C in D:A+=C.width;B+=C.height
				return A,B
		else:
			def getScreenDimensions():return-1,-1
SCREEN_WIDTH,SCREEN_HEIGHT=getScreenDimensions()
def MouseTo(x,y):MOUSE.position=x,y
def mouseGet():return MOUSE.position
def Click():MOUSE.click(1)
def RightClick():MOUSE.click(3)
def MiddleClick():MOUSE.click(2)
def ScrollV(clicks,wheel_delta=WHEEL_DELTA):MOUSE.scroll(dy=clicks)
def ScrollH(clicks,wheel_delta=WHEEL_DELTA):MOUSE.scroll(dx=clicks)
def Scroll(dx=None,dy=None,wheel_delta_x=WHEEL_DELTA,wheel_delta_y=WHEEL_DELTA):MOUSE.scroll(dy=dy,dx=dx)
def LeftMouseDown():MOUSE.press(1)
def RightMouseDown():MOUSE.press(3)
def MiddleMouseDown():MOUSE.press(2)
def LeftMouseUp():MOUSE.release(1)
def RightMouseUp():MOUSE.release(3)
def MiddleMouseUp():MOUSE.release(2)