# 抓取优美图库图片:唯美壁纸-手机壁纸
# 拿到页面源代码，提取子页面的链接地址-href
# 找到子页面图片的下载地址：<img alt="" src=的值
# 下载图片

import requests
import re
from bs4 import BeautifulSoup
import os
import  time

for i in range(1, 2):  # 爬3个网页的图片试着看
    if i == 1:
        index = 'index.htm'
    else:
        index = 'index_'+str(i)+'.htm'
    url = 'https://www.umei.cc/bizhitupian/shoujibizhi/'+index
    print(url)
    resp = requests.get(url)
    resp.encoding = "utf-8"
    # print(resp.text)

    # 解析数据,把源代码交给BeautifulSoup,
    main_page = BeautifulSoup(resp.text, "html.parser")
    div1 = main_page.find("div", class_="listlbc_cont_l")
    # print(div1)
    divs = div1.find_all("div", class_="img")
    # 拿到子页面的链接
    '''  通过正则或直接拿
    # 1.通过着正则
    obj = re.compile(r'href="(?P<href>.*?)">', re.S)
    for div in divs:
        # print(div)
        div2 = div.find("a", class_="img_album_btn")
        # print(div2)
        href = obj.search(str(div2))  # 这里要注意转换成字符串
        html = 'https://www.umei.cc'+href.group("href")
        print(html)
        
    '''
    # 2.直接调用方法拿
    # print(divs)
    for div in divs:
        # 获取a标签的href数据,拼接好子页面链接
        a = div.find("div", class_="btns").find("a")
        href = a.get("href")  # 通过get拿到a属性的值
        html = 'https://www.umei.cc/'+href  # 子页面的链接
        # print(html)

        # 拿到子页面的源代码
        child_resp = requests.get(html)  # get方法获取标签属性值
        child_resp.encoding = "utf-8"
        # print(child_resp.text)
        # 拿到图片链接
        child_page = BeautifulSoup(child_resp.text, "html.parser")
        img_div = child_page.find("div", class_="big-pic")

        # 获取图片的名字
        name_div = child_page.find("div", class_="wrapper clearfix imgtitle sut6552").find("h1")
        total_name = name_div.text.strip()  # 获取标签的名字值
        # 转化str，replace清除空格
        # str[start,end]切片获取字符串前几位，start/end为负表示从尾部计数
        img_name = str(total_name.replace(" ", ""))[:4]

        # 图片源链接
        img_src = img_div.find("img").get("src")  # get方法拿img标签的src值

        print(img_name)
        print(img_src)

        # 下载图片
        img_resp = requests.get(img_src)
        img_resp.content  # 这里拿到的是字节 wb:二进制写入

        # 保存到指定的目录
        os.listdir("手机壁纸")
        with open("手机壁纸/"+img_name+".jpg", mode="wb") as f:
            f.write(img_resp.content)

        print(img_name+'.jpg下载成功！')
        time.sleep(1)  # 暂停1秒，防止网站把你的请求禁止
        # break  # test

print('allover!')
