import win32gui
import win32con
import win32api
import ctypes
import random
import colorsys

hdc = win32gui.GetDC(0)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
color = 0

x = y = 0
while True:
    hdc = win32gui.GetDC(0)

    # Increment and wrap the hue value adjust as needed (default is 0.02)
    color = (color + 0.02) % 1.0

    rgb_color = colorsys.hsv_to_rgb(color, 1.0, 1.0)
    p = [(random.randint(0, w), random.randint(0, h)) for _ in range(4)]

    hPen = win32gui.CreatePen(
        win32con.PS_SOLID,
        5,
        win32api.RGB(
            int(rgb_color[0] * 255), int(rgb_color[1] * 255), int(rgb_color[2] * 255)
        ),
    )

    win32gui.SelectObject(hdc, hPen)
    win32gui.PolyBezier(hdc, p)
    win32gui.DeleteObject(hPen)
    win32gui.ReleaseDC(0, hdc)
