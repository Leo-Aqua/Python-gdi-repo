import ctypes
import time
import win32con
import win32gui
import win32ui
import win32api

# Define BITMAPINFOHEADER + BITMAPINFO
class BITMAPINFOHEADER(ctypes.Structure):
    _fields_ = [
        ("biSize", ctypes.c_uint32),
        ("biWidth", ctypes.c_int32),
        ("biHeight", ctypes.c_int32),
        ("biPlanes", ctypes.c_uint16),
        ("biBitCount", ctypes.c_uint16),
        ("biCompression", ctypes.c_uint32),
        ("biSizeImage", ctypes.c_uint32),
        ("biXPelsPerMeter", ctypes.c_int32),
        ("biYPelsPerMeter", ctypes.c_int32),
        ("biClrUsed", ctypes.c_uint32),
        ("biClrImportant", ctypes.c_uint32),
    ]

class BITMAPINFO(ctypes.Structure):
    _fields_ = [("bmiHeader", BITMAPINFOHEADER), ("bmiColors", ctypes.c_uint32 * 1)]

# Get screen size
width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)

# Create screen DC and compatible DC
hdc_screen = win32gui.GetDC(0)
hdc_screen_ui = win32ui.CreateDCFromHandle(hdc_screen)
hdc_mem = hdc_screen_ui.CreateCompatibleDC()

# Set up BITMAPINFO
bmi = BITMAPINFO()
bmi.bmiHeader.biSize = ctypes.sizeof(BITMAPINFOHEADER)
bmi.bmiHeader.biWidth = width
bmi.bmiHeader.biHeight = -height  # top-down
bmi.bmiHeader.biPlanes = 1
bmi.bmiHeader.biBitCount = 32
bmi.bmiHeader.biCompression = win32con.BI_RGB

# Prepare pointer for pixel data
pixel_ptr = ctypes.c_void_p()

# Call CreateDIBSection from gdi32
gdi32 = ctypes.windll.gdi32
dib = gdi32.CreateDIBSection(
    hdc_screen,                     # HDC
    ctypes.byref(bmi),              # BITMAPINFO*
    win32con.DIB_RGB_COLORS,        # color usage
    ctypes.byref(pixel_ptr),        # output: pixel buffer ptr
    None, 0                         # no file mapping
)

# Wrap handle in PyCBitmap
bitmap = win32ui.CreateBitmapFromHandle(dib)
hdc_mem.SelectObject(bitmap)

# Cast pixel_ptr to a pointer to array of 32-bit ints
pixel_array = ctypes.cast(pixel_ptr, ctypes.POINTER(ctypes.c_uint32))

# Infinite fractal loop
while True:
    hdc_screen = win32gui.GetDC(0)

    # Capture screen
    win32gui.BitBlt(hdc_mem.GetSafeHdc(), 0, 0, width, height, hdc_screen, 0, 0, win32con.SRCCOPY)

    # Apply XOR fractal effect
    for i in range(width * height):
        x = i % width
        y = i // width
        xor_val = x ^ y

        color = pixel_array[i] # Change colors below
        r = (color >> 16) & 0xFF
        g = (color >> 8) & 0xFF
        b = color & 0xFF

        r = (r + xor_val) & 0xFF
        g = (g + xor_val) & 0xFF
        b = (b + xor_val) & 0xFF

        pixel_array[i] = r | (g << 8) | (b << 16)

    # Draw back to screen
    hdc_screen_ui.BitBlt((0, 0), (width, height), hdc_mem, (0, 0), win32con.SRCCOPY)

    win32gui.ReleaseDC(0, hdc_screen)

