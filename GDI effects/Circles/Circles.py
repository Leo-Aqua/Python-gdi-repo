import win32gui
import win32con
import ctypes
import random
import time
from ctypes import wintypes

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

gdi32 = ctypes.WinDLL('gdi32')
gdi32.SelectClipRgn.argtypes = [wintypes.HDC, wintypes.HRGN]
gdi32.SelectClipRgn.restype = ctypes.c_int

hdc = win32gui.GetDC(0)


    
screen_size = win32gui.GetWindowRect(win32gui.GetDesktopWindow())

left = screen_size[0]
top = screen_size[1]
right = screen_size[2]
bottom = screen_size[3]

w = right - left - 500
h = bottom - top - 500



def ci(x,y,w,h):
    hdc = win32gui.GetDC(0)

    x = int(x)
    y = int(y)
    w = int(w)
    h = int(h)
    hrgn = win32gui.CreateEllipticRgnIndirect((x, y, x + w, y + h))
    gdi32.SelectClipRgn(hdc, hrgn.handle)
    win32gui.BitBlt(hdc, x, y, w, h, hdc, x, y, win32con.NOTSRCCOPY)

    # Remove clipping region by passing NULL (0)
    gdi32.SelectClipRgn(hdc, 0)

    win32gui.DeleteObject(hrgn)
    win32gui.ReleaseDC(0, hdc)



while(True):
    size = 1000
    x = random.randint(0, w + size - 1) - size / 2
    y = random.randint(0, h + size - 1) - size / 2
    i = 0
    while(i<size):
        ci(x - i / 2, y - i / 2, i, i)
        i+=100
        time.sleep(.01)




   


