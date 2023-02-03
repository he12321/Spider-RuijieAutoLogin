# 登录小说网
# 登录 -> 得到cookies
# 带着cookies去请求书架url -> 书架上的内容

# session：会话
# 必须把上面的操作连起来
# 可以用session进行请求 -> session是一连串的请求，在这个过程中cookies不会丢失

import requests
from lxml import etree

url = 'https://passport.zhihuishu.com/login'

# 1.登录

session = requests.session()  # session：会话
data = {
    "pwd": "89b62336528945a28733ecd3ffb2e1c7"
}
session.get(url, data=data)
# print(resp.text)
# print(resp.cookies)  # 查看cookies

# 2.带着cookies拿到课程数据
resp = session.get('https://onlineweb.zhihuishu.com/onlinestuh5')
resp.encoding = 'utf-8'
print(resp.text)
html = etree.HTML(resp.text)
div = html.xpath('//*[@id="sharingClassed"]/div[2]/ul[1]/div/dl/dt/div[1]/div[1]/text()')
print(div)
