# 代理：通过第三方的机器发送请求

import requests

# 223.82.106.130	80	江西省九江市

proxies = {
   " https": "https://223.82.106.130"
}
url = 'https://baidu.com'
resp = requests.get(url, proxies=proxies)
resp.encoding = 'utf-8'

print(resp.text)

resp.close()  # 关闭resp
