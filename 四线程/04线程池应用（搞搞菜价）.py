# 利用线程池的功能获取北京新发地网站的菜价

import requests
import re
import json

from concurrent.futures import ThreadPoolExecutor
url = "http://www.xinfadi.com.cn/getPriceData.html"

page = 1  # 页面
prodPcatid = 1186  # 一级分类：蔬菜86 水果87 肉禽蛋89 水产90 粮油88 豆制品1203 调料1204
prodCatid = 0  # 二级分类：99/00      01/02 5-6-7-8  9-10-11-12
data = {
    "limit": 20,
    "current": page,
    "pubDateStartTime": "",
    "pubDateEndTime": "",
    "prodPcatid": prodPcatid,
    "prodCatid": prodCatid,
    "prodName": ""
}

resp = requests.post(url, data=data)
html = resp.text
dic = json.loads(html)
print(html["list"])


def print_price(text):
    obj = re.compile(r'"prodName":"(?P<name>.*?)".*?'
                     r'"lowPrice":"(?P<low>.*?)","highPrice":"(?P<high>.*?)","avgPrice":"(?P<avg>.*?)"'
                     r'.*?"unitInfo":"(?P<Info>.*?)"', re.S)
    result = obj.finditer(html)
    for it in result:
        name = it.group("name")
        lowprice = it.group("low")
        highprice = it.group("high")
        avgprice = it.group("avg")
        unitInfo = it.group("Info")
        print(name, "最低价"+lowprice, "最高价"+highprice, "平均"+avgprice, "元/"+unitInfo)


print_price(html)

