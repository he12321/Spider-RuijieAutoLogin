# 获取2023年必看片的迅雷下载链接
# 1.定位到2023必看热片
# 2.从必看热片中提取子页面链接
# 3.请求子页面链接地址，获取想要的下载地址

import requests
import re
import urllib3
urllib3.disable_warnings()  # 解决警告：InsecureRequestWarning

url = 'https://www.dytt89.com'
resp = requests.get(url, verify=False)  # verify=False 去掉安全验证
resp.encoding = 'gb2312'  # 指定字符集为网站编码，解决乱码，gb2312是中国标准简体中文字符集
# print(resp.text)

ul_obj = re.compile(r'2023必看热片.*?<ul>(?P<ul>.*?)</ul>', re.S)
li_obj = re.compile(r"<a href='(?P<href>.*?)'", re.S)
mov_obj = re.compile(r'◎片　　名(?P<movie>.*?)<br />.*?'
                     r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)

# 找到ul电影区域

childhref_list = []  # 列表保存完整子页面链接
ul_result = ul_obj.finditer(resp.text)  # 获取找的那部分
for it in ul_result:
    ul = it.group("ul")
    # print(ul)

    # 提取子页面超链接
    href_result = li_obj.finditer(ul)
    for it2 in href_result:
        href = it2.group("href")
        # 拼接子页面链接 域名+子页面地址
        final_href = "https://www.dytt89.com"+href
        # print(final_href)  # 子页面链接
        childhref_list.append(final_href)  # 子页面链接保存到列表


# 提取子页面内容（片名，下载链接），并保存到文件
f = open("2023必看热片.txt", mode="a", encoding="utf-8")
for it in childhref_list:
    resp2 = requests.get(it)
    resp2.encoding = "gb2312"
    # print(resp2.text)
    # 获取片名、下载链接
    mov_result = mov_obj.search(resp2.text)
    movie = mov_result.group("movie")
    download = mov_result.group("download")
    f.write(movie+'\n')
    f.write(download+'\n')
    print(movie)
    print(download)

print("over")

