import ctypes
import os
from PIL import Image
import io
import base64
from time import sleep

SPI_SETDESKWALLPAPER = 20

# تبدیل داده باینری به تصویر
image_data = ""
image = Image.open(io.BytesIO(base64.b64decode(image_data)))

image_path = r"C:\Windows\Temp\temp.png"
image.save(image_path)
# for python 3.5 and higher

ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)

