from Xlib import X, XK
from typing import Final

class VirtualKey:
    pass

# Mapping Windows virtual key codes to X11 keysyms
backspace: Final[VirtualKey] = XK.XK_BackSpace
tab: Final[VirtualKey] = XK.XK_Tab
clear: Final[VirtualKey] = XK.XK_Clear
enter: Final[VirtualKey] = XK.XK_Return
shift: Final[VirtualKey] = XK.XK_Shift_L  # Left Shift
ctrl: Final[VirtualKey] = XK.XK_Control_L  # Left Control
alt: Final[VirtualKey] = XK.XK_Alt_L  # Left Alt
pause: Final[VirtualKey] = XK.XK_Pause
CAPS_LOCK: Final[VirtualKey] = XK.XK_Caps_Lock

escape: Final[VirtualKey] = XK.XK_Escape
space: Final[VirtualKey] = XK.XK_space
page_up: Final[VirtualKey] = XK.XK_Page_Up
page_down: Final[VirtualKey] = XK.XK_Page_Down
end: Final[VirtualKey] = XK.XK_End
home: Final[VirtualKey] = XK.XK_Home
left_arrow: Final[VirtualKey] = XK.XK_Left
up_arrow: Final[VirtualKey] = XK.XK_Up
right_arrow: Final[VirtualKey] = XK.XK_Right
down_arrow: Final[VirtualKey] = XK.XK_Down
select: Final[VirtualKey] = XK.XK_Select
print: Final[VirtualKey] = XK.XK_Print
ins: Final[VirtualKey] = XK.XK_Insert
del_key: Final[VirtualKey] = XK.XK_Delete
help: Final[VirtualKey] = XK.XK_Help

key_0: Final[VirtualKey] = XK.XK_0
key_1: Final[VirtualKey] = XK.XK_1
key_2: Final[VirtualKey] = XK.XK_2
key_3: Final[VirtualKey] = XK.XK_3
key_4: Final[VirtualKey] = XK.XK_4
key_5: Final[VirtualKey] = XK.XK_5
key_6: Final[VirtualKey] = XK.XK_6
key_7: Final[VirtualKey] = XK.XK_7
key_8: Final[VirtualKey] = XK.XK_8
key_9: Final[VirtualKey] = XK.XK_9

a: Final[VirtualKey] = XK.XK_a
b: Final[VirtualKey] = XK.XK_b
c: Final[VirtualKey] = XK.XK_c
d: Final[VirtualKey] = XK.XK_d
e: Final[VirtualKey] = XK.XK_e
f: Final[VirtualKey] = XK.XK_f
g: Final[VirtualKey] = XK.XK_g
h: Final[VirtualKey] = XK.XK_h
i: Final[VirtualKey] = XK.XK_i
j: Final[VirtualKey] = XK.XK_j
k: Final[VirtualKey] = XK.XK_k
l: Final[VirtualKey] = XK.XK_l
m: Final[VirtualKey] = XK.XK_m
n: Final[VirtualKey] = XK.XK_n
o: Final[VirtualKey] = XK.XK_o
p: Final[VirtualKey] = XK.XK_p
q: Final[VirtualKey] = XK.XK_q
r: Final[VirtualKey] = XK.XK_r
s: Final[VirtualKey] = XK.XK_s
t: Final[VirtualKey] = XK.XK_t
u: Final[VirtualKey] = XK.XK_u
v: Final[VirtualKey] = XK.XK_v
w: Final[VirtualKey] = XK.XK_w
x: Final[VirtualKey] = XK.XK_x
y: Final[VirtualKey] = XK.XK_y
z: Final[VirtualKey] = XK.XK_z

left_windows: Final[VirtualKey] = XK.XK_Super_L
right_windows: Final[VirtualKey] = XK.XK_Super_R
application: Final[VirtualKey] = XK.XK_Menu
computer_sleep: Final[VirtualKey] = XK.XK_Sleep

number_pad_0: Final[VirtualKey] = XK.XK_KP_0
number_pad_1: Final[VirtualKey] = XK.XK_KP_1
number_pad_2: Final[VirtualKey] = XK.XK_KP_2
number_pad_3: Final[VirtualKey] = XK.XK_KP_3
number_pad_4: Final[VirtualKey] = XK.XK_KP_4
number_pad_5: Final[VirtualKey] = XK.XK_KP_5
number_pad_6: Final[VirtualKey] = XK.XK_KP_6
number_pad_7: Final[VirtualKey] = XK.XK_KP_7
number_pad_8: Final[VirtualKey] = XK.XK_KP_8
number_pad_9: Final[VirtualKey] = XK.XK_KP_9

multiply: Final[VirtualKey] = XK.XK_KP_Multiply
add: Final[VirtualKey] = XK.XK_KP_Add
separator: Final[VirtualKey] = XK.XK_KP_Separator
subtract: Final[VirtualKey] = XK.XK_KP_Subtract
decimal: Final[VirtualKey] = XK.XK_KP_Decimal
divide: Final[VirtualKey] = XK.XK_KP_Divide

f1: Final[VirtualKey] = XK.XK_F1
f2: Final[VirtualKey] = XK.XK_F2
f3: Final[VirtualKey] = XK.XK_F3
f4: Final[VirtualKey] = XK.XK_F4
f5: Final[VirtualKey] = XK.XK_F5
f6: Final[VirtualKey] = XK.XK_F6
f7: Final[VirtualKey] = XK.XK_F7
f8: Final[VirtualKey] = XK.XK_F8
f9: Final[VirtualKey] = XK.XK_F9
f10: Final[VirtualKey] = XK.XK_F10
f11: Final[VirtualKey] = XK.XK_F11
f12: Final[VirtualKey] = XK.XK_F12
f13: Final[VirtualKey] = XK.XK_F13
f14: Final[VirtualKey] = XK.XK_F14
f15: Final[VirtualKey] = XK.XK_F15
f16: Final[VirtualKey] = XK.XK_F16
f17: Final[VirtualKey] = XK.XK_F17
f18: Final[VirtualKey] = XK.XK_F18
f19: Final[VirtualKey] = XK.XK_F19
f20: Final[VirtualKey] = XK.XK_F20
f21: Final[VirtualKey] = XK.XK_F21
f22: Final[VirtualKey] = XK.XK_F22
f23: Final[VirtualKey] = XK.XK_F23
f24: Final[VirtualKey] = XK.XK_F24

num_lock: Final[VirtualKey] = XK.XK_Num_Lock

left_shift: Final[VirtualKey] = XK.XK_Shift_L
right_shift: Final[VirtualKey] = XK.XK_Shift_R
left_control: Final[VirtualKey] = XK.XK_Control_L
right_control: Final[VirtualKey] = XK.XK_Control_R
left_alt: Final[VirtualKey] = XK.XK_Alt_L
right_alt: Final[VirtualKey] = XK.XK_Alt_R

comma: Final[VirtualKey] = XK.XK_comma
dot: Final[VirtualKey] = XK.XK_period
minus: Final[VirtualKey] = XK.XK_minus
plus: Final[VirtualKey] = XK.XK_plus

ä: Final[VirtualKey] = XK.XK_adiaeresis
ß: Final[VirtualKey] = XK.XK_ssharp
ö: Final[VirtualKey] = XK.XK_odiaeresis
ü: Final[VirtualKey] = XK.XK_udiaeresis

oem_1: Final[VirtualKey] = XK.XK_colon
oem_2: Final[VirtualKey] = XK.XK_slash
oem_3: Final[VirtualKey] = XK.XK_grave
oem_4: Final[VirtualKey] = XK.XK_bracketleft
oem_5: Final[VirtualKey] = XK.XK_backslash
oem_6: Final[VirtualKey] = XK.XK_bracketright
oem_7: Final[VirtualKey] = XK.XK_quoteright
oem_8: Final[VirtualKey] = XK.XK_Mode_switch
oem_102: Final[VirtualKey] = XK.XK_less