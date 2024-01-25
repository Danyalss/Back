import base64
import pyperclip
import os

os.system("dir")

file_name = input("File Name : ")

# باز کردن تصویر و تبدیل آن به داده باینری
with open(file_name, "rb") as image_file:
    binary_data = base64.b64encode(image_file.read()).decode()


# print(binary_data)

# کپی کردن داده باینری به کلیپ بورد
pyperclip.copy(binary_data)
