import ctypes
import os
from PIL import Image
import io
import base64
from time import sleep
import datetime
import jdatetime


SPI_SETDESKWALLPAPER = 20

# تبدیل داده باینری به تصویر
image_data = ""
image = Image.open(io.BytesIO(base64.b64decode(image_data)))

image_path = r"C:\Windows\Temp\temp.png"
image.save(image_path)


#   ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)


# تاریخ فعلی را به فرمت شمسی تبدیل می‌کنیم
now = datetime.datetime.now()
jalali_date = jdatetime.date.fromgregorian(day=now.day, month=now.month, year=now.year)

# اگر تاریخ فعلی از 22 بهمن گذشته بود یا همان روز بود
change_wallpaper = (jalali_date.month > 11) or (jalali_date.month == 11 and jalali_date.day >= 22)

# اگر شرط برقرار بود، تصویر پس‌زمینه تغییر می‌کند
if change_wallpaper:
    image_path = "مسیر تصویر خود را اینجا قرار دهید"
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)
