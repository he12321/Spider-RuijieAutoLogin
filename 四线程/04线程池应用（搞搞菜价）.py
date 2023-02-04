# 利用线程池的功能获取北京新发地网站的蔬菜所有的菜价

import requests
import re
import json
import csv
from concurrent.futures import ThreadPoolExecutor

url = "http://www.xinfadi.com.cn/getPriceData.html"

# page = 1  # 页面
# prodPcatid = 1186  # 一级分类：蔬菜86 水果87 肉禽蛋89 水产90 粮油88 豆制品1203 调料1204
# prodCatid = 0  # 二级分类：99/00      01/02 5-6-7-8  9-10-11-12
# data = {
#     "limit": 20,
#     "current": page,
#     "pubDateStartTime": "",
#     "pubDateEndTime": "",
#     "prodPcatid": prodPcatid,
#     "prodCatid": prodCatid,
#     "prodName": ""
# }
# resp = requests.post(url, data=data)


def get_onepage_data(data):
    url = "http://www.xinfadi.com.cn/getPriceData.html"
    resp = requests.post(url, data=data)
    text = resp.text.replace("\\", "/").strip()
    # 通过把json转换成dic（字典获取其中数据）
    dic = json.loads(text)
    list = dic["list"]

    # 取出列表中的每一个字典的值,并写入csv文件
    with open("新发地菜价.csv", mode="a", encoding="utf-8") as f:
        csvwriter = csv.writer(f)
        for item in list:
            # 将字典数据写入csv文件
            csvwriter.writerow(item.values())

            # 取出字典key的对应的value
            name = item['prodName']
            lowprice = item['lowPrice']
            highprice = item['highPrice']
            avgprice = item['avgPrice']
            unitinfo = item['unitInfo']
            print(name, lowprice, highprice, avgprice, "元/"+unitinfo)

    print("页面提取完毕！")


def print_price(url, data):
    resp = requests.post(url, data=data)
    text = resp.text
    obj = re.compile(r'"prodName":"(?P<name>.*?)".*?'
                     r'"lowPrice":"(?P<low>.*?)","highPrice":"(?P<high>.*?)","avgPrice":"(?P<avg>.*?)"'
                     r'.*?"unitInfo":"(?P<Info>.*?)"', re.S)
    result = obj.finditer(text)
    for it in result:
        name = it.group("name")
        lowprice = it.group("low")
        highprice = it.group("high")
        avgprice = it.group("avg")
        unitInfo = it.group("Info")
        print(name, "最低价"+lowprice, "最高价"+highprice, "平均"+avgprice, "元/"+unitInfo)


# 利用线程池进行多个页面（21135）的提取
if __name__ == '__main__':
    # for i in range(1, 21136):  # 效率及其低下
    #     get_onepage_data(url, data)

    # 开启50个线程下载数据
    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):  # 这里设置爬取页面数50
            page = i
            data = {
                "limit": 20,
                "current": page
            }
            t.submit(get_onepage_data, data=(data,))

    print("over")
