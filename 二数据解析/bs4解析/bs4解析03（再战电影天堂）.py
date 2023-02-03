# 利用bs4解析获取-国内电影-资源页面信息并保存到文件

import requests
import re
from bs4 import BeautifulSoup
import csv

url = 'https://www.dy2018.com/html/gndy/index.html'
resp = requests.get(url)
resp.encoding = 'gb2312'
# print(resp.text)

# 解析数据
# 1.把页面源代码交给BeautifulSoup进行处理，生成bs（page）对象
page = BeautifulSoup(resp.text, "html.parser")  # 指定html解释器

# 2.从bs对象中查找数据
# 方法：find(标签，属性=值) 找到一个数据就终止 find_all(div, class="hello") 查找所有数据
# table = page.find("div", class_="content2")  # class是Python的关键字，
# 属性后面加下划线_就可以避免报错,也可以换成字典来代替<div class="co_content2">
dic = {
    "class": "co_content8"
}
div = page.find("div", attrs=dic)
# print(div)
table = div.find("table")
# print(table)

# 从table里面找数据、或使用正则寻找
obj = re.compile(r'</a>]<a href="(?P<url>.*?)" title="(?P<name>.*?)"', re.S)
tds = table.find_all("td", class_="inddline")
# print(tds)

# 写入csv文件

f = open("国内电影(再战电影天堂).csv", mode="w", encoding="utf=8")  # 设置文件编码为utf-8
csvwriter = csv.writer(f)
for td in tds:
    result = obj.search(str(td))  # 注意参数，要装转换成字符串
    if result:
        href = 'https://www.dytt89.com'+result.group("url")
        name = result.group("name")
        print(name)
        print(href)
        csvwriter.writerow([name, href])


print("over")
