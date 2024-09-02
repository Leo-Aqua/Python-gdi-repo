# a 1

import win32api
import win32con
import win32gui
import math
import time
import ctypes


def sines():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    desktop = win32gui.GetDesktopWindow()
    hdc = win32gui.GetWindowDC(desktop)
    sw = win32api.GetSystemMetrics(0)
    sh = win32api.GetSystemMetrics(1)
    angle = 0

    while True:
        hdc = win32gui.GetWindowDC(desktop)
        n = 0
        for i in range(int(sw + sh)):
            a = int(math.sin(n) * 20)
            win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, a, 0, win32con.SRCCOPY)
            n += 0.1
        win32gui.ReleaseDC(desktop, hdc)
        time.sleep(0.01)


if __name__ == "__main__":
    sines()
