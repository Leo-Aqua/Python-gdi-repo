
import win32gui
import win32con
import ctypes
import math

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
hdc = win32gui.GetDC(0)
dx = dy = 1
angle = 0
size = 1
speed = 5
while True:
    
    win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, dx, dy, win32con.SRCCOPY)
    dx = math.ceil(math.sin(angle) * size * 10)
    dy = math.ceil(math.cos(angle) * size * 10)
    angle += speed / 10
    if angle > math.pi :
        angle = math.pi * -1
