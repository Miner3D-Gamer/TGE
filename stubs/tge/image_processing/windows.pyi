from PIL import Image
import ctypes
__all__=['screenshot','get_pixel_color']
class BITMAPINFOHEADER(ctypes.Structure):...
class BITMAPINFO(ctypes.Structure):...
def screenshot(position:tuple[int,int],size:tuple[int,int])->Image.Image:...
def get_pixel_color(pos:tuple[int,int])->tuple[int,int,int]:...