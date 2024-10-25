from Xlib import  XK
from typing import Final



# Mapping Windows virtual key codes to X11 keysyms
backspace: Final[int] = XK.XK_BackSpace
tab: Final[int] = XK.XK_Tab
clear: Final[int] = XK.XK_Clear
enter: Final[int] = XK.XK_Return
shift: Final[int] = XK.XK_Shift_L  # Left Shift
ctrl: Final[int] = XK.XK_Control_L  # Left Control
alt: Final[int] = XK.XK_Alt_L  # Left Alt
pause: Final[int] = XK.XK_Pause
CAPS_LOCK: Final[int] = XK.XK_Caps_Lock

escape: Final[int] = XK.XK_Escape
space: Final[int] = XK.XK_space
page_up: Final[int] = XK.XK_Page_Up
page_down: Final[int] = XK.XK_Page_Down
end: Final[int] = XK.XK_End
home: Final[int] = XK.XK_Home
left_arrow: Final[int] = XK.XK_Left
up_arrow: Final[int] = XK.XK_Up
right_arrow: Final[int] = XK.XK_Right
down_arrow: Final[int] = XK.XK_Down
select: Final[int] = XK.XK_Select
print: Final[int] = XK.XK_Print
ins: Final[int] = XK.XK_Insert
del_key: Final[int] = XK.XK_Delete
help: Final[int] = XK.XK_Help

key_0: Final[int] = XK.XK_0
key_1: Final[int] = XK.XK_1
key_2: Final[int] = XK.XK_2
key_3: Final[int] = XK.XK_3
key_4: Final[int] = XK.XK_4
key_5: Final[int] = XK.XK_5
key_6: Final[int] = XK.XK_6
key_7: Final[int] = XK.XK_7
key_8: Final[int] = XK.XK_8
key_9: Final[int] = XK.XK_9

a: Final[int] = XK.XK_a
b: Final[int] = XK.XK_b
c: Final[int] = XK.XK_c
d: Final[int] = XK.XK_d
e: Final[int] = XK.XK_e
f: Final[int] = XK.XK_f
g: Final[int] = XK.XK_g
h: Final[int] = XK.XK_h
i: Final[int] = XK.XK_i
j: Final[int] = XK.XK_j
k: Final[int] = XK.XK_k
l: Final[int] = XK.XK_l
m: Final[int] = XK.XK_m
n: Final[int] = XK.XK_n
o: Final[int] = XK.XK_o
p: Final[int] = XK.XK_p
q: Final[int] = XK.XK_q
r: Final[int] = XK.XK_r
s: Final[int] = XK.XK_s
t: Final[int] = XK.XK_t
u: Final[int] = XK.XK_u
v: Final[int] = XK.XK_v
w: Final[int] = XK.XK_w
x: Final[int] = XK.XK_x
y: Final[int] = XK.XK_y
z: Final[int] = XK.XK_z

left_windows: Final[int] = XK.XK_Super_L
right_windows: Final[int] = XK.XK_Super_R
application: Final[int] = XK.XK_Menu
# computer_sleep: Final[int] = None

number_pad_0: Final[int] = XK.XK_KP_0
number_pad_1: Final[int] = XK.XK_KP_1
number_pad_2: Final[int] = XK.XK_KP_2
number_pad_3: Final[int] = XK.XK_KP_3
number_pad_4: Final[int] = XK.XK_KP_4
number_pad_5: Final[int] = XK.XK_KP_5
number_pad_6: Final[int] = XK.XK_KP_6
number_pad_7: Final[int] = XK.XK_KP_7
number_pad_8: Final[int] = XK.XK_KP_8
number_pad_9: Final[int] = XK.XK_KP_9

multiply: Final[int] = XK.XK_KP_Multiply
add: Final[int] = XK.XK_KP_Add
separator: Final[int] = XK.XK_KP_Separator
subtract: Final[int] = XK.XK_KP_Subtract
decimal: Final[int] = XK.XK_KP_Decimal
divide: Final[int] = XK.XK_KP_Divide

f1: Final[int] = XK.XK_F1
f2: Final[int] = XK.XK_F2
f3: Final[int] = XK.XK_F3
f4: Final[int] = XK.XK_F4
f5: Final[int] = XK.XK_F5
f6: Final[int] = XK.XK_F6
f7: Final[int] = XK.XK_F7
f8: Final[int] = XK.XK_F8
f9: Final[int] = XK.XK_F9
f10: Final[int] = XK.XK_F10
f11: Final[int] = XK.XK_F11
f12: Final[int] = XK.XK_F12
f13: Final[int] = XK.XK_F13
f14: Final[int] = XK.XK_F14
f15: Final[int] = XK.XK_F15
f16: Final[int] = XK.XK_F16
f17: Final[int] = XK.XK_F17
f18: Final[int] = XK.XK_F18
f19: Final[int] = XK.XK_F19
f20: Final[int] = XK.XK_F20
f21: Final[int] = XK.XK_F21
f22: Final[int] = XK.XK_F22
f23: Final[int] = XK.XK_F23
f24: Final[int] = XK.XK_F24

num_lock: Final[int] = XK.XK_Num_Lock

left_shift: Final[int] = XK.XK_Shift_L
right_shift: Final[int] = XK.XK_Shift_R
left_control: Final[int] = XK.XK_Control_L
right_control: Final[int] = XK.XK_Control_R
left_alt: Final[int] = XK.XK_Alt_L
right_alt: Final[int] = XK.XK_Alt_R

comma: Final[int] = XK.XK_comma
dot: Final[int] = XK.XK_period
minus: Final[int] = XK.XK_minus
plus: Final[int] = XK.XK_plus

ä: Final[int] = XK.XK_adiaeresis
ß: Final[int] = XK.XK_ssharp
ö: Final[int] = XK.XK_odiaeresis
ü: Final[int] = XK.XK_udiaeresis

oem_1: Final[int] = XK.XK_colon
oem_2: Final[int] = XK.XK_slash
oem_3: Final[int] = XK.XK_grave
oem_4: Final[int] = XK.XK_bracketleft
oem_5: Final[int] = XK.XK_backslash
oem_6: Final[int] = XK.XK_bracketright
oem_7: Final[int] = XK.XK_quoteright
oem_8: Final[int] = XK.XK_Mode_switch
oem_102: Final[int] = XK.XK_less