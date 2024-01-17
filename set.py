import ctypes
import os
from PIL import Image
import io
import base64

SPI_SETDESKWALLPAPER = 20

# تبدیل داده باینری به تصویر
image_data = "داده باینری که قبلاً ذخیره کردید"
image = Image.open(io.BytesIO(base64.b64decode(image_data)))
image.save("temp.png")
image_path = os.path.join(os.getcwd(), "temp.png")

# برای پایتون 3.5 و بالاتر
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)


# حذف تصویر موقت
# os.remove("temp.png")
