import ctypes
from PIL import Image
import io
import base64
from time import sleep
import datetime

SPI_SETDESKWALLPAPER = 20

# تبدیل داده باینری به تصویر
image_data = ""
image = Image.open(io.BytesIO(base64.b64decode(image_data)))

image_path = r"C:\Windows\Temp\temp.png"
image.save(image_path)

def set_wallpaper():
   ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)


def check_date():
   date = datetime.date.today()
   if date > datetime.date(2023, 2, 21): # 22 Bahman 1401 in Gregorian date
       set_wallpaper()

# Run the function to check the date and set the wallpaper if necessary
check_date()