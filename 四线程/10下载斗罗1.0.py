'''
下载斗罗大第一集
流程：
    1.拿到710-1-1.html页面源代码
    2.从代码中提取m3u8的url
    3.下载m3u8
    4.读取m3u8文件，下载视频
    5.合并视频
'''

import requests
import re
import asyncio
import aiohttp
import aiofiles
import os


# 1.拿到710-1-1.html页面源代码
# 2.从代码中提取m3u8的url

# https://v.v1kd.com/20211117/ttxgRz2V/index.m3u8（第一个m3u8）
# https://v.v1kd.com/20211117/ttxgRz2V/1000kb/hls/index.m3u8（第二个m3u8）


def get_m3u8(url):
    resp = requests.get(url)
    text = resp.text
    resp.close()

    # 从JavaScript提取最好使用re
    obj = re.compile(r'<li class="swiper-slide">正在播放(?P<name>.*?)</li>.*?'
                     r'<div class="player-wrapper"><script type="text/javascript">.*?'
                     r'"url":"(?P<url>.*?)"', re.S)
    name = obj.search(text).group("name")
    result2 = obj.search(text).group("url")
    m3u8_url_1 = result2.replace("\\", "")

    # 下载第一个m3u8文件
    resp1 = requests.get(m3u8_url_1)
    string = "first.m3u8"
    with open(string, mode="wb")as f:
        f.write(resp1.content)
    print(string, "下载成功！")

    # 解析第一个m3u8文件
    get_line = ""
    with open(string, mode="r")as f:
        for line in f:
            line = line.strip()  # 去掉空格、空白、换行符
            if line.startswith("#"):  # 如果以#开头我不要
                continue
            get_line = line

    # 第2个m3u8文件(真正的m3u8)
    m3u8_url_2 = "https://v.v1kd.com"+get_line  # 也可以这样写 <=> m3u8_url_1.rsplit("/", 3)[0] +getline

    # 下载第2个m3u8文件(真正的m3u8)
    resp2 = requests.get(m3u8_url_2)
    string2 = name+".m3u8"  # 第二个m3u8文件名字
    with open(string2, mode="wb")as f:
        f.write(resp2.content)
    print(string2, "下载成功！")
    return name


async def down_ts(dir, url, n):  # 异步协程下载ts文件
    name = str(n)+".ts"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.content.read()
            async with aiofiles.open(f"{dir}/{name}", mode="wb")as f:
                await f.write(data)
            print("下载成功")


# 解析第二个m3u8文件
async def get_ts(name, dir):
    string2 = f"{name}.m3u8"
    n = 1
    tasks = []
    with open(string2, mode="r")as f:
        for line in f:
            line = line.strip()  # 去掉空格、空白、换行符
            if line.startswith("#"):  # 如果以#开头我不要
                continue

            # 下载视频片段
            url = "https://v.v1kd.com"+line
            task = asyncio.create_task(down_ts(dir, url, n))
            tasks.append(task)
            n += 1

    await asyncio.wait(tasks)


# 下载ts视频
if __name__ == '__main__':
    url = "https://jinri.live/vodplay/710-1-1.html"
    # name = get_m3u8(url)
    name = "《斗罗大陆》第01集 - 酷播线路"
    dir = "TS/"+name  # 保存ts文件的目录

    # 判断目录是否存在
    if not os.path.exists(dir):
        os.mkdir(f"TS/{name}")

    asyncio.run(get_ts(name, dir))


