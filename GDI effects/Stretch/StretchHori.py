import win32gui
import win32con
import ctypes


hdc = win32gui.GetDC(0)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

while True:
    hdc = win32gui.GetDC(0)
    win32gui.StretchBlt(hdc, -20, 0, sw + 40, sh, hdc, 0, 0, sw, sh, win32con.SRCCOPY)
    win32gui.ReleaseDC(0, hdc)
