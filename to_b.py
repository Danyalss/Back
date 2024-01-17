import base64
import pyperclip

# باز کردن تصویر و تبدیل آن به داده باینری
with open("back.png", "rb") as image_file:
    binary_data = base64.b64encode(image_file.read()).decode()

# کپی کردن داده باینری به کلیپ بورد
pyperclip.copy(binary_data)
