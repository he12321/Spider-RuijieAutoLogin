# 获取 北京新发地市场网站 菜价
# http://www.xinfadi.com.cn/index.html

import requests
import re

url = 'http://www.xinfadi.com.cn/index.html'
resp = requests.get(url)
# print(resp.text)  # 发现前端网页没有想要的菜价数据等，应该是js加载

# 在浏览器的检查中发现数据隐藏在一个getCat.html的post请求中，可以利用requests02学习的内容来解决
url = 'http://www.xinfadi.com.cn/getCat.html'
from_data = {
    "prodCatid": 1186
}
resp = requests.post(url, from_data)
# print(resp.text)

# 使用正则获取数据
html = resp.text

obj = re.compile(r'"prodName":"(?P<cainame>.*?)".*?'
                 r'"lowPrice":"(?P<lowprice>.*?)","highPrice":"(?P<highprice>.*?)",'
                 r'"avgPrice":"(?P<avgprice>.*?)".*?'
                 r'"unitInfo":"(?P<every>.*?)"', re.S)

result = obj.finditer(html)
for it in result:
    name = it.group("cainame")
    lowPrice = it.group("lowprice")
    highPrice = it.group("highprice")
    avgPrice = it.group("avgprice")
    every = it.group("every")
    print(name, '最低价'+lowPrice, '最高价'+highPrice, '平均价'+avgPrice, '/'+every)



