import win32con
import win32gui
import win32ui
import ctypes
import random


def draw_gradient_triangle(hdc):
    for _ in range(25):
        l, t, r, b = win32gui.GetClientRect(win32gui.GetDesktopWindow())
        vertices = (
            {
                "x": int(random.random() * r),
                "y": int(random.random() * b),
                "Red": int(random.random() * 0xFF00),
                "Green": 0,
                "Blue": 0,
                "Alpha": 0,
            },
            {
                "x": int(random.random() * r),
                "y": int(random.random() * b),
                "Red": 0,
                "Green": int(random.random() * 0xFF00),
                "Blue": 0,
                "Alpha": 0,
            },
            {
                "x": int(random.random() * r),
                "y": int(random.random() * b),
                "Red": 0,
                "Green": 0,
                "Blue": int(random.random() * 0xFF00),
                "Alpha": 0,
            },
        )
        mesh = ((0, 1, 2),)
        win32gui.GradientFill(hdc, vertices, mesh, win32con.GRADIENT_FILL_TRIANGLE)


def main():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()

    hdc_screen = win32gui.GetDC(0)

    try:
        while True:
            draw_gradient_triangle(hdc_screen)
    finally:
        win32gui.ReleaseDC(0, hdc_screen)


if __name__ == "__main__":
    main()
