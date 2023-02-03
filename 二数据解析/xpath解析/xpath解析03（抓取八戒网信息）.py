# 抓取猪八戒信息

import requests
from lxml import etree

url = 'https://nanchang.zbj.com/search/service?kw=saas&r=2&lp=0&hp=8888'
resp = requests.get(url)
# print(resp.text)

html = etree.HTML(resp.text)

# //*[@id="__layout"]/div/div[3]/div/div[4]/div[4]/div[1]/div[12]/div/div[2]/div[1]/span
# //*[@id="__layout"]/div/div[3]/div/div[4]/div[4]/div[1]/div[12]/div/div[2]/div[2]/a/text()
# //*[@id="__layout"]/div/div[3]/div/div[4]/div[4]/div[1]/div[7]/div/div[3]/div[2]/a

divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div[4]/div[1]/div')
for i in range(1, 100):
    str1 = ']/div/div[2]/div[2]/a/text()'
    str2 = ']/div/div[3]/div[1]/span/text()'
    name = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div[4]/div[1]/div['+str(i)+str1)
    price = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div[4]/div[1]/div['+str(i)+str2)
    print(name, price)

