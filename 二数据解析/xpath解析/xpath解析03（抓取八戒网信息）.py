# 抓取猪八戒信息

import requests
from lxml import etree

# url = 'https://nanchang.zbj.com/search/service?kw=saas&r=2&lp=0&hp=8888'


def get_info(url):
    with requests.get(url) as resp:
        # print(resp.text)

        html = etree.HTML(resp.text)

        # //*[@id="__layout"]/div/div[3]/div/div[4]/div[4]/div[1]/div[8]
        # 获取的数据是含类似数据的div列表，将div[8]改div
        # //*[@id="__layout"]/div/div[3]/div/div[4]/div[4]/div[1]/div[7]/div/div[2]/div[1]/span
        # //*[@id="__layout"]/div/div[3]/div/div[4]/div[4]/div[1]/div[7]/div/div[2]/div[2]/a
        # //*[@id="__layout"]/div/div[3]/div/div[4]/div[4]/div[1]/div[7]/div/div[2]/div[4]/div[2]/div/span[2]
        # //*[@id="__layout"]/div/div[3]/div/div[4]/div[4]/div[1]/div[7]/div/div[2]/div[4]/div[3]/div/span[2]

        divs = html.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div[4]/div[1]/div')  # 这里注意div
        for div in divs:
            price = div.xpath("./div/div[2]/div[1]/span/text()")
            if price:  # 通过价格排除空数据
                price = price[0].strip("￥")  # 处理价格数据

                title = div.xpath("./div/div[2]/div[2]/a/text()")  # 处理title
                title = "sass".join(title)  # join拼接

                num = div.xpath("./div/div[2]/div[4]/div[2]/div/span[2]/text()")[0]  # 销量数据

                good_num = div.xpath("./div/div[2]/div[4]/div[3]/div/span[2]/text()")[0]  # 处理好评

                print(title, f"价格：{price}", f"销量：{num}", f"好评{good_num}")


if __name__ == '__main__':
    url = 'https://nanchang.zbj.com/search/service?kw=saas&r=2&lp=0&hp=8888'
    get_info(url)
