# 获取豆瓣电影的网页内容

import requests
url = "https://movie.douban.com/j/chart/top_list?"
# ?type=24&interval_id=100:90&action=&start=0&limit=20"
open
# 重新封装参数
param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "20",
}
resp = requests.get(url, params=param)
print('请求的url：'+resp.request.url)  # 跟get的url一样
# 发现没有内容，应该是反扒机制
# 查看一下headers
print("查看headers：", resp.request.headers)
# 发现是Python的headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"
}
resp = requests.get(url, params=param, headers=headers)
print(resp.json())
resp.close()  # 关闭resp
