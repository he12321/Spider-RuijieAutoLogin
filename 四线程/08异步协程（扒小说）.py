# 利用异步协程扒小说

import requests
import asyncio
import aiohttp
import json
import aiofiles  # 异步的文件读写
import os
import time


# 目标百度——小说——西游记
# https://dushu.baidu.com/pc/detail?gid=4355370985

# 章节内容：（get就获得所有的章节，同步）
# https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224355370985%22}  # %22book_id% <=> "book_id"
# https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":"4355370985"} # 所有章节的id
# 章节里面的内容：（每个内容不一样，异步）
# https://dushu.baidu.com/api/pc/getChapterContent?data={"book_id":"4355370985","cid":"4355370985|1566856033","need_bookinfo":1}

'''
1.同步操作：访问getCatalog,拿到章节的book_id、cid
2.异步操作：getChapterContent下载所有的文章内容
'''


async def aiodownload(title, cid, book_id):
    data = {  # json
        "book_id": book_id,
        "cid": f"{book_id}|{cid}",
        "need_bookinfo": 1
    }
    data = json.dumps(data)  # json转换成字符串
    url = f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            dic = await resp.json()
            # coroutine 'ClientResponse.json' was never awaited，这意味着在json部分前面必须有一个await。这是因为您使用的是异步函数。

            os.listdir("西游记")
            async with aiofiles.open('西游记/'+title+".txt", mode="w", encoding="utf-8") as f:
                await f.write(dic['data']['novel']['content'])  # 把小说内容写出


async def getCatalog(url):  # 获取章节的cid
    resp = requests.get(url)
    dic = resp.json()
    tasks = []
    for item in dic['data']['novel']['items']:  # item对应每一个章节
        title = item['title']
        cid = item['cid']
        # 准备异步任务,每一个cid对应一个异步任务：
        task = asyncio.create_task(aiodownload(title, cid, book_id))
        tasks.append(task)
    await asyncio.wait(tasks)


if __name__ == '__main__':
    book_id = "4355370985"  # 西游记的id
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id":'+book_id+'}'
    asyncio.run(getCatalog(url))




