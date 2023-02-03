# 拿到页面源代码
# 通过re（正则）来提取我们要的信息
import requests
import re
import csv  # 导入csv包，csv文件是数据以逗号间隔

for i in range(0, 250, 25):
    url = 'https://movie.douban.com/top250?start='+str(i)+'&filter='
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"
    }

    # 请求页面内容
    resp = requests.get(url, headers=header)
    page = resp.text

    # 解析数据
    obj = re.compile(r'<li>.*?<em class="">(?P<id>.*?)</em>'
                     r'.*?<span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&nbsp;'
                     r'.*? <span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                     r'.*?<span>(?P<num>.*?)人评价</span>', re.S)
    # 开始匹配
    result = obj.finditer(page)
    f = open("豆瓣电影Top250.csv", mode="a")
    csvwriter = csv.writer(f)
    for it in result:
        idstr = it.group("id")
        namestr = it.group("name")
        timestr = '时间:'+it.group("year").strip()  # 清除字符串中空白
        s = '评分:'+it.group("score")
        numstr = it.group("num")+'人评价'
        print(idstr, namestr, timestr, s, numstr)

        dic = it.groupdict()
        dic['year'] = dic['year'].strip()
        csvwriter.writerow(dic.values())
    # def strip(self, *args, **kwargs):leading and trailing whitespace removed


f.close()  # 关闭文件
resp.close()  # 关闭resp
print("over")

