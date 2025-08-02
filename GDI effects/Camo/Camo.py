import win32gui
import win32con
import ctypes
import random
import time


hdc = win32gui.GetDC(0)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]


while True:
    hdc = win32gui.GetDC(0)
    x = random.randint(0, w)
    win32gui.BitBlt(hdc, random.randint(0, 666), random.randint(0, 666), w, h, hdc, random.randint(0, 666), random.randint(0, 666), win32con.NOTSRCERASE)
    win32gui.ReleaseDC(0, hdc)
    time.sleep(.01)
