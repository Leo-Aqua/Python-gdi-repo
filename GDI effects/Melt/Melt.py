import win32gui
import win32con
import ctypes
import random
import time


hdc = win32gui.GetDC(0)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]


x = y = 0
while True:
    hdc = win32gui.GetDC(0)
    x = random.randint(0, w)
    win32gui.BitBlt(hdc, x, 1, 10, h, hdc, x, 0, win32con.SRCCOPY)
    win32gui.ReleaseDC(0, hdc)
