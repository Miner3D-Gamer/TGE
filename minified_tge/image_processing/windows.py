_A=None
import ctypes
from ctypes import wintypes
from PIL import Image
SRCCOPY=13369376
DIB_RGB_COLORS=0
class BITMAPINFOHEADER(ctypes.Structure):_fields_=[('biSize',wintypes.DWORD),('biWidth',wintypes.LONG),('biHeight',wintypes.LONG),('biPlanes',wintypes.WORD),('biBitCount',wintypes.WORD),('biCompression',wintypes.DWORD),('biSizeImage',wintypes.DWORD),('biXPelsPerMeter',wintypes.LONG),('biYPelsPerMeter',wintypes.LONG),('biClrUsed',wintypes.DWORD),('biClrImportant',wintypes.DWORD)]
class BITMAPINFO(ctypes.Structure):_fields_=[('bmiHeader',BITMAPINFOHEADER)]
user32=ctypes.windll.user32
gdi32=ctypes.windll.gdi32
hdc_screen=user32.GetDC(_A)
hdc_mem=gdi32.CreateCompatibleDC(hdc_screen)
hbm=gdi32.CreateCompatibleBitmap(hdc_screen,1,1)
hbm_old=gdi32.SelectObject(hdc_mem,hbm)
def screenshot(position,size):
 H=position;B=size;E=user32.GetDC(_A);D=gdi32.CreateCompatibleDC(E);G=gdi32.CreateCompatibleBitmap(E,B[0],B[1]);J=gdi32.SelectObject(D,G);gdi32.BitBlt(D,0,0,B[0],B[1],E,H[0],H[1],SRCCOPY);A=BITMAPINFO();A.bmiHeader.biSize=ctypes.sizeof(BITMAPINFOHEADER);A.bmiHeader.biWidth=B[0];A.bmiHeader.biHeight=-B[1];A.bmiHeader.biPlanes=1;A.bmiHeader.biBitCount=32;A.bmiHeader.biCompression=0;A.bmiHeader.biSizeImage=B[0]*B[1]*4;A.bmiHeader.biXPelsPerMeter=0;A.bmiHeader.biYPelsPerMeter=0;A.bmiHeader.biClrUsed=0;A.bmiHeader.biClrImportant=0;I=ctypes.create_string_buffer(A.bmiHeader.biSizeImage);gdi32.GetDIBits(D,G,0,B[1],I,ctypes.byref(A),0);gdi32.SelectObject(D,J);gdi32.DeleteObject(G);gdi32.DeleteDC(D);user32.ReleaseDC(_A,E);K=I.raw;C=bytearray(A for A in K)
 for F in range(0,len(C),4):C[F],C[F+2]=C[F+2],C[F]
 return Image.frombytes('RGBA',B,bytes(C))
def get_pixel_color(pos):gdi32.BitBlt(hdc_mem,0,0,1,1,hdc_screen,pos[0],pos[1],SRCCOPY);A=BITMAPINFO();A.bmiHeader.biSize=ctypes.sizeof(BITMAPINFOHEADER);A.bmiHeader.biWidth=1;A.bmiHeader.biHeight=-1;A.bmiHeader.biPlanes=1;A.bmiHeader.biBitCount=32;A.bmiHeader.biCompression=0;A.bmiHeader.biSizeImage=0;A.bmiHeader.biXPelsPerMeter=0;A.bmiHeader.biYPelsPerMeter=0;A.bmiHeader.biClrUsed=0;A.bmiHeader.biClrImportant=0;C=ctypes.create_string_buffer(4);gdi32.GetDIBits(hdc_mem,hbm,0,1,C,ctypes.byref(A),DIB_RGB_COLORS);gdi32.SelectObject(hdc_mem,hbm_old);gdi32.DeleteObject(hbm);gdi32.DeleteDC(hdc_mem);user32.ReleaseDC(_A,hdc_screen);B=C.raw;return B[2],B[1],B[0]