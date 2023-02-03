# 多进程：开进程太费资源了
# bilibili：进程是资源单位，多开一个进程就多占用一个资源

from multiprocessing import Process


def func():
    for i in range(12):
        print("子进程", i)


if __name__ == '__main__':
    p = Process(target=fun)
    p.start()

    for i in range(8):
        print("主进程_", i)



