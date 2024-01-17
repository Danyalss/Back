import ctypes
import os
from PIL import Image
import io
import base64
import pyperclip

SPI_SETDESKWALLPAPER = 20

# تصویر را به صورت داده باینری ذخیره کنید

with open("back.png", "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode()

pyperclip.copy(image_data)

# تبدیل داده باینری به تصویر
image_data = io.BytesIO(base64.b64decode(image_data))
image = Image.open(image_data)


image.save("temp.png")
image_path = os.path.join(os.getcwd(), "temp.png")


# برای پایتون 3.5 و بالاتر
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)

# حذف تصویر موقت
os.remove("temp.png")
