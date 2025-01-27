#type: ignore
from screeninfo import get_monitors
import pynput
_A='middle_mouse_down'
WHEEL_DELTA=120
MOUSE=pynput.mouse.Controller()
def getScreenDimensions():return get_monitors()[0].width,get_monitors()[0].width
SCREEN_WIDTH,SCREEN_HEIGHT=getScreenDimensions()
def set_mouse_to(coords):MOUSE.position=coords
def get_mouse_position():return MOUSE.position
def left_click():MOUSE.click(pynput.mouse.Button.left)
def right_click():MOUSE.click(pynput.mouse.Button.right)
def middle_click():MOUSE.click(pynput.mouse.Button.middle)
def scroll_vertical(clicks,wheel_delta=WHEEL_DELTA):MOUSE.scroll(dy=clicks,dx=0)
def scroll_horizontal(clicks,wheel_delta=WHEEL_DELTA):MOUSE.scroll(dx=clicks,dy=0)
def scroll(dx=None,dy=None,wheel_delta_x=WHEEL_DELTA,wheel_delta_y=WHEEL_DELTA):
 if not dx:dx=0
 if not dy:dy=0
 MOUSE.scroll(dy=dy,dx=dx)
def left_mouse_down():MOUSE.press(pynput.mouse.Button.left)
def right_mouse_down():MOUSE.press(pynput.mouse.Button.right)
def middle_mouse_down():MOUSE.press(pynput.mouse.Button.middle)
def left_mouse_up():MOUSE.release(pynput.mouse.Button.left)
def right_mouse_up():MOUSE.release(pynput.mouse.Button.right)
def middle_mouse_up():MOUSE.release(pynput.mouse.Button.middle)
def is_left_button_pressed():return _is_button_pressed(1)
def is_right_button_pressed():return _is_button_pressed(3)
def is_middle_button_pressed():return _is_button_pressed(2)
def _is_button_pressed(button):
 with pynput.mouse.Events()as B:
  for A in B:
   if isinstance(A,pynput.mouse.Events.Click)and A.button==button:return A.pressed
  return False
__all__=['left_click','right_click','middle_click','set_mouse_to','get_mouse_position','is_right_button_pressed','is_middle_button_pressed','is_left_button_pressed','middle_mouse_up','right_mouse_up',_A,'left_mouse_up','scroll','scroll_horizontal','scroll_vertical','left_mouse_down','right_mouse_down',_A]