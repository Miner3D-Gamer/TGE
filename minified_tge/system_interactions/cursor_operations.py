from..import SYSTEM_NAME
from.shared import*
if SYSTEM_NAME=='windows':from.cursor.cursor_operations_ctypes import left_click,right_click,middle_click,set_mouse_to,get_mouse_position,is_right_button_pressed,is_middle_button_pressed,is_left_button_pressed,middle_mouse_up,right_mouse_up,middle_mouse_down,left_mouse_up,scroll,scroll_horizontal,scroll_vertical,left_mouse_down,right_mouse_down,middle_mouse_down
else:from.cursor.cursor_operations_pynput import left_click,right_click,middle_click,set_mouse_to,get_mouse_position,is_right_button_pressed,is_middle_button_pressed,is_left_button_pressed,middle_mouse_up,right_mouse_up,middle_mouse_down,left_mouse_up,scroll,scroll_horizontal,scroll_vertical,left_mouse_down,right_mouse_down,middle_mouse_down
def click_mouse_button(button_number):ClickMouseButtonList[button_number]()
def hold_mouse_button(button_number):HoldMouseButtonList[button_number]()
def release_mouse_button(button_number):ReleaseMouseButtonList[button_number]()
def click_mouse_button_at(button_number,x,y):ClickMouseButton_atList[button_number](x,y)
def left_click_at(x,y):set_mouse_to((x,y));left_click()
def double_left_click():left_click();left_click()
def double_left_click_at(x,y):set_mouse_to((x,y));left_click();left_click()
def right_click_at(x,y):set_mouse_to((x,y));right_click()
def double_right_click():right_click();right_click()
def MiddleClick_at(x,y):set_mouse_to((x,y));middle_click()
def drag_to(x,y):left_mouse_down();set_mouse_to((x,y));left_mouse_up()
def drag_obj_to(x,y,a,b):set_mouse_to((x,y));drag_to(a,b)
ClickMouseButtonList=[left_click,middle_click,right_click]
ClickMouseButton_atList=[left_click_at,MiddleClick_at,right_click_at]
HoldMouseButtonList=[left_mouse_down,middle_mouse_down,right_mouse_down]
ReleaseMouseButtonList=[left_mouse_up,right_mouse_up,middle_mouse_up]