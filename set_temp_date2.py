import ctypes
from PIL import Image
import io
import base64
import jdatetime

SPI_SETDESKWALLPAPER = 20

# تبدیل داده باینری به تصویر
image_data = ""
image = Image.open(io.BytesIO(base64.b64decode(image_data)))

image_path = r"C:\Windows\Temp\temp.png"
image.save(image_path)

def set_wallpaper():
   ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)


target_date = jdatetime.date(1402, 11, 22)  # 22 بهمن 1402

now = jdatetime.date.today()

if now > target_date:
    set_wallpaper()
else:
    print("NOT now")
