# 关闭请求，防止被堵

import requests
url = "https://movie.douban.com/j/chart/top_list"
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",  # 这个参数在显示网页内容时会刷新
    "limit": "20",
}
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"
}
response = requests.get(url=url, params=param, headers=header)
print(response.text)

response.close()  # 关闭response
