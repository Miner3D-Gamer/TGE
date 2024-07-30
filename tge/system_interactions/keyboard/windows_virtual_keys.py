from typing import Final
class VirtualKey():
    ...
backspace: Final[VirtualKey] = 0x08
tab: Final[VirtualKey] = 0x09
clear: Final[VirtualKey] = 0x0C
enter: Final[VirtualKey] = 0x0D
shift: Final[VirtualKey] = 0x10
ctrl: Final[VirtualKey] = 0x11
alt: Final[VirtualKey] = 0x12
pause: Final[VirtualKey] = 0x13
CAPS_LOCK: Final[VirtualKey] = 0x14
#
escape: Final[VirtualKey] = 0x1B
#
space: Final[VirtualKey] = 0x20
page_up: Final[VirtualKey] = 0x21
page_down: Final[VirtualKey] = 0x22
end: Final[VirtualKey] = 0x23
home: Final[VirtualKey] = 0x24
left_arrow: Final[VirtualKey] = 0x25
up_arrow: Final[VirtualKey] = 0x26
right_arrow: Final[VirtualKey] = 0x27
down_arrow: Final[VirtualKey] = 0x28
select: Final[VirtualKey] = 0x29
print: Final[VirtualKey] = 0x2A
ins: Final[VirtualKey] = 0x2D
del_key: Final[VirtualKey] = 0x2E
help: Final[VirtualKey] = 0x2F
key_0: Final[VirtualKey] = 0x30
key_1: Final[VirtualKey] = 0x31
key_2: Final[VirtualKey] = 0x32
key_3: Final[VirtualKey] = 0x33
key_4: Final[VirtualKey] = 0x34
key_5: Final[VirtualKey] = 0x35
key_6: Final[VirtualKey] = 0x36
key_7: Final[VirtualKey] = 0x37
key_8: Final[VirtualKey] = 0x38
key_9: Final[VirtualKey] = 0x39
a: Final[VirtualKey] = 0x41
b: Final[VirtualKey] = 0x42
c: Final[VirtualKey] = 0x43
d: Final[VirtualKey] = 0x44
e: Final[VirtualKey] = 0x45
f: Final[VirtualKey] = 0x46
g: Final[VirtualKey] = 0x47
h: Final[VirtualKey] = 0x48
i: Final[VirtualKey] = 0x49
j: Final[VirtualKey] = 0x4A
k: Final[VirtualKey] = 0x4B
l: Final[VirtualKey] = 0x4C
m: Final[VirtualKey] = 0x4D
n: Final[VirtualKey] = 0x4E
o: Final[VirtualKey] = 0x4F
p: Final[VirtualKey] = 0x50
q: Final[VirtualKey] = 0x51
r: Final[VirtualKey] = 0x52
s: Final[VirtualKey] = 0x53
t: Final[VirtualKey] = 0x54
u: Final[VirtualKey] = 0x55
v: Final[VirtualKey] = 0x56
w: Final[VirtualKey] = 0x57
x: Final[VirtualKey] = 0x58
y: Final[VirtualKey] = 0x59
z: Final[VirtualKey] = 0x5A
left_windows: Final[VirtualKey] = 0x5B
right_windows: Final[VirtualKey] = 0x5C
application: Final[VirtualKey] = 0x5D
computer_sleep: Final[VirtualKey] = 0x5F
number_pad_0: Final[VirtualKey] = 0x60
number_pad_1: Final[VirtualKey] = 0x61
number_pad_2: Final[VirtualKey] = 0x62
number_pad_3: Final[VirtualKey] = 0x63
number_pad_4: Final[VirtualKey] = 0x64
number_pad_5: Final[VirtualKey] = 0x65
number_pad_6: Final[VirtualKey] = 0x66
number_pad_7: Final[VirtualKey] = 0x67
number_pad_8: Final[VirtualKey] = 0x68
number_pad_9: Final[VirtualKey] = 0x69
multiply: Final[VirtualKey] = 0x6A
add: Final[VirtualKey] = 0x6B
separator: Final[VirtualKey] = 0x6C
subtract: Final[VirtualKey] = 0x6D
decimal: Final[VirtualKey] = 0x6E
divide: Final[VirtualKey] = 0x6F
f1: Final[VirtualKey] = 0x70
f2: Final[VirtualKey] = 0x71
f3: Final[VirtualKey] = 0x72
f4: Final[VirtualKey] = 0x73
f5: Final[VirtualKey] = 0x74
f6: Final[VirtualKey] = 0x75
f7: Final[VirtualKey] = 0x76
f8: Final[VirtualKey] = 0x77
f9: Final[VirtualKey] = 0x78
f10: Final[VirtualKey] = 0x79
f11: Final[VirtualKey] = 0x7A
f12: Final[VirtualKey] = 0x7B
f13: Final[VirtualKey] = 0x7C
f14: Final[VirtualKey] = 0x7D
f15: Final[VirtualKey] = 0x7E
f16: Final[VirtualKey] = 0x7F
f17: Final[VirtualKey] = 0x80
f18: Final[VirtualKey] = 0x81
f19: Final[VirtualKey] = 0x82
f20: Final[VirtualKey] = 0x83
f21: Final[VirtualKey] = 0x84
f22: Final[VirtualKey] = 0x85
f23: Final[VirtualKey] = 0x86
f24: Final[VirtualKey] = 0x87
num_lock: Final[VirtualKey] = 0x91
#
left_shift: Final[VirtualKey] = 0xA0
right_shift: Final[VirtualKey] = 0xA1
left_control: Final[VirtualKey] = 0xA2
right_control: Final[VirtualKey] = 0xA3
left_alt: Final[VirtualKey] = 0xA4
right_alt: Final[VirtualKey] = 0xA5
### THE REST IS UNFINISHED
# https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes

comma: Final[VirtualKey] = 0xBC
dot : Final[VirtualKey]= 0xBE
minus : Final[VirtualKey]= 0xBD
plus : Final[VirtualKey]= 0xbb

ä: Final[VirtualKey] = 0xDE
ß: Final[VirtualKey] = 0xDD
ö: Final[VirtualKey] = 0xC0
ü: Final[VirtualKey] = 0xB4



oem_1 : Final[VirtualKey]= 0xba
oem_2 : Final[VirtualKey]= 0xbf
oem_3 : Final[VirtualKey]= 0xc0
oem_4 : Final[VirtualKey]= 0xdb
oem_5 : Final[VirtualKey]= 0xdc
oem_6 : Final[VirtualKey]= 0xdd
oem_7 : Final[VirtualKey]= 0xde
oem_8: Final[VirtualKey] = 0xdf
oem_102 : Final[VirtualKey]= 0xe2


