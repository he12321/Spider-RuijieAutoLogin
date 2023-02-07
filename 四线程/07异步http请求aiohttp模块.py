# aiohttp模块作为爬虫应对各种请求运行效率极高

# requests.get()是一个同步的代码 -> 异步操作aiohttp
# pip install aiohttp -i 这里添加百度搜的python国内源

import aiohttp
import asyncio
import os

# 实战优美图库
urls = [
    "http://kr.shanghai-jiuxin.com/file/2020/0627/5a3c6e07bdef0b5aaf50662cecec4f82.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/0627/7344e144a8fc5118f2609b5df10d1bb1.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/0609/01990e1408314b341bb26b70670f7108.jpg",
    "http://kr.shanghai-jiuxin.com/file/2020/0609/817ccc274d3526b3fe57375f485da873.jpg"
]


async def aiodownload(url):
    name = url.rsplit("/", 1)[1]  # 从右边第一个切取第0个
    # -发送请求
    # requests.get(url)  .post(url)
    # session.get()  .post()
    # --得到图片内容
    # ---保存到文件

    # with open("data.csv",) as f:
    #     f.write()
    # with操作相当于文件的操作，到时候会自动关闭，不用关链接
    async with aiohttp.ClientSession() as session:  # 异步的<==> requests模块
        async with session.get(url) as resp:    # 异步的resp
            # 请求回来，写入文件：
            data = resp.content.read()  # .text=>text() .json()=>.json()
            os.listdir("图片")
            # 保存到图片文件夹下

            # 文件读写也是io操作，也可以异步操作=> aiofiles模块

            with open("图片/"+name, mode="wb") as f:
                f.write(await data)  # 读取内容是异步的，需要一个await挂起，什时候有东西在往里面写

    print(name, "下载成功")


async def main():
    tasks = []
    for url in urls:
        ta = asyncio.create_task(aiodownload(url))  # 创建任务对象，把协程对象aiodownload(url)转换成任务对象
        tasks.append(ta)

    await asyncio.wait(tasks)  # 运行任务列表


if __name__ == '__main__':
    asyncio.run(main())



