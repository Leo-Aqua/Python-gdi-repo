import win32gui
import ctypes
import time

hdc = win32gui.GetDC(0)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
while True:
    win32gui.InvertRect(hdc, (0, 0, w, h))
    time.sleep(0.2)  # Adjust delay to your liking
