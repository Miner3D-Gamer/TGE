WHEEL_DELTA=120
import pynput
MOUSE=pynput.mouse.Controller()
from pyautogui import size as getScreenDimensions
SCREEN_WIDTH,SCREEN_HEIGHT=getScreenDimensions()
def set_mouse_to(coords):MOUSE.position=coords
def get_mouse_position():return MOUSE.position
def left_click():MOUSE.click(1)
def right_click():MOUSE.click(3)
def middle_click():MOUSE.click(2)
def scroll_vertical(clicks,wheel_delta=WHEEL_DELTA):MOUSE.scroll(dy=clicks)
def scroll_horizontal(clicks,wheel_delta=WHEEL_DELTA):MOUSE.scroll(dx=clicks)
def scroll(dx=None,dy=None,wheel_delta_x=WHEEL_DELTA,wheel_delta_y=WHEEL_DELTA):MOUSE.scroll(dy=dy,dx=dx)
def left_mouse_down():MOUSE.press(1)
def right_mouse_down():MOUSE.press(3)
def middle_mouse_down():MOUSE.press(2)
def left_mouse_up():MOUSE.release(1)
def right_mouse_up():MOUSE.release(3)
def middle_mouse_up():MOUSE.release(2)
def is_left_button_pressed():return _is_button_pressed(1)
def is_right_button_pressed():return _is_button_pressed(3)
def is_middle_button_pressed():return _is_button_pressed(2)
MOUSE
def _is_button_pressed(button):
 with pynput.mouse.Events()as B:
  for A in B:
   if isinstance(A,pynput.mouse.Events.Click)and A.button==button:return A.pressed
  return False