# python写协程的程序

import asyncio
import time


# 定义一个简单的函数
# async def func():
#     print("我叫小贺")


# if __name__ == '__main__':
#     g = func()  # 此时的函数是异步协程函数，此时函数执行得到的是一个协程对象
#     print(g)  # <coroutine object func at 0x0000022657435600>
# # sys:1: RuntimeWarning: coroutine 'func' was never awaited  <coroutine object func at 0x000002A8CBA65000>
# # sys：1：运行时警告：协程“func”从未等待过<协程对象 func at 0x000002A8CBA65000>
#     asyncio.run(g)  # 协程程序运行需要asynico模块支持


# async def func1():  # 串行运行所有函数至少需要9秒
#     print("1.你好，我叫阿尼亚")
#     # time.sleep(3)  # 当程序出现同步操作时，异步就中断了
#     await asyncio.sleep(3)  # 异步操作的代码，把当前的睡眠挂起切换到其他任务上面（await）
#     print("1.你好，我叫黄昏")
#
#
# async def func2():
#     print("你好，我叫2-2")
#     # time.sleep(2)
#     await asyncio.sleep(2)
#     print("你好，我叫黄昏2-2")
#
#
# async def func3():
#     print("你好，我叫3-4")
#     # time.sleep(4)
#     await asyncio.sleep(4)
#     print("你好，我叫3-4")
#
#
# async def main():  # 定义一个协程主函数
#     # 第一种写法：await不放在主函数，放在协程函数里面
#     # f1 = func1()
#     # await f1  # 相当于调用了f1,一般await挂起操作放在协程对象前面
#     # f2 = func2()
#     # await f2
#
#     # 第二种写法：
#
#     # tasks = {  # python3.11这样写会报错，从3.8开始，计划3.11删除
#     #            # 3.11.1亲测报错，3.8及以下应该可以照下面写
#     #     func1(), func2(), func3()
#     # }
#     # 应该改为：
#
#     tasks = [
#         asyncio.create_task(func1()),  # python3.8以后应把协程对象包装成task对象asyncio.create_task()
#         asyncio.create_task(func2()),
#         asyncio.create_task(func3())
#     ]
#
#     await asyncio.wait(tasks)
# # 在python3.8之后不能把协程对象直接丢给wait（）处理，
# # Coroutines will be wrapped in Tasks.而在之前的版本（python3.8以下）会自动包装成task对象
# # python3.8以后应把协程对象包装成task对象asyncio.create_task()
#
# if __name__ == '__main__':
#     print("正常如果同步执行需要3+2+4 = 9秒以上")
#     start = time.time()
#     asyncio.run(main())  # main（）返回的应该是一个协程对象
#     print(time.time()-start)


# 在爬虫领域的应用（模拟）：

async def download(url):
    print("准备开始下载")
    await asyncio.sleep(2)  # 这里处理异步程序异步程序
    print("下载成功")


async def main():
    urls = [
        "http://www.baidu.com",
        "http://www.bilibili.com",
        "http://sougou.com"
    ]
    tasks = []
    for url in urls:
        d = asyncio.create_task(download(url))  # 返回一个协程对象
        tasks.append(d)
    await asyncio.wait(tasks)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time()-start)
