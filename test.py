import ctypes
import os

SPI_SETDESKWALLPAPER = 20

# image_path = os.path.join(os.getcwd(), "back")

image_path = "/back.png"

# برای پایتون 2.5 و بالاتر
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, image_path, 0)

# برای پایتون 3.5 و بالاتر
#ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)
