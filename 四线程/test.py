import requests
import json

dic = {
    "你好": "hello",
    "嗨": "hi",
    "英语": "English"
}
h = [1, 2, 3, 4]
l = list(dic.keys())
list = list(dic.values())

date = {
    "date": "12345"
}
url = "http://www.xinfadi.com.cn/getPriceData.html"
data = {
    "limit": 20,
    "current": 2
}
resp = requests.post(url, data=data)
html = resp.text
html = json.loads(html)
list = html["list"]
i = 10086
page = i
data = {
    "limit": 20,
    "current": page
}
print(data)
