import win32gui
import win32con
import ctypes
import random

hdc = win32gui.GetDC(0)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]


while True:
    win32gui.DrawIcon(
        hdc,
        random.randint(0, w),
        random.randint(0, h),
        win32gui.LoadIcon(None, win32con.IDI_ERROR),
    )  # Change IDI_ERROR to something else to change the icon being displayed
