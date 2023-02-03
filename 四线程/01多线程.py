# 线程：是一个执行单位，cpu运行找的是线程
# 进程：是一个资源单位，每一个进程至少要有一个线程

from threading import Thread  # 线程类


def func():
    for i in range(10):
        print("函数里面打印的i:", i)


# if __name__ == '__main__':
#     func()
#     print("hello")
#     print("执行main函数。至少会有一个主线程")
#     for i in range(6):
#         print("主函数打印i:", i)
# # 查看执行结果就知道该程序是一个单线程的

# 要执行多线程就要导入多线程的类 from Threading import Thread
'''  线程状态
1.新建状态（New）：创建一个新的线程对象。
2.就绪状态（Runnable）:线程创建对象后，其他线程调用start()方法，该线程处于就绪状态，资源已经准备就绪，等待CPU资源。
3.运行状态（Running）：处于就绪状态的线程获取到CPU资源后进入运行状态。
4.阻塞状态（Blocked）：阻塞状态是线程由于某些原因放弃CPU使用，暂时停止运行。
（1）等待阻塞：线程调用start（）方法，JVM会把这个线程放入等待池中，该线程需要其他线程调用notify()或notifyAll()方法才能被唤醒。
（2）同步阻塞：运行的线程在获取对象的同步锁时，若该同步锁被其他线程占用，则JVM会把该线程放入锁池中。
（3）其他阻塞：运行的线程执行sleep()或join()方法，或者发出了I/O请求时，JVM会把该线程置为阻塞状态。当sleep()状态超时、join()等待线程终止或者超时、或者I/O处理完毕时，线程重新转入就绪状态。
5.终止状态（Terminated）：线程run（）方法运行完毕，该线程结束。
'''

# if __name__ == '__main__':
#     t1 = Thread(target=func)  # 创建线程对象，线程处于准备状态I告诉线程要执行func函数
#     t1.start()  # 线程处于就绪状态，资源就绪，具体执行看CPU
#
#     for i in range(6):
#         print("主线程：", i)



# class myThread(Thread):  # myThread继承Thread
#     def run(self):  # 重写run方法，当线程被执行的时候，被执行的就是run()里面的函数
#         for i in range(5):
#             print("Class_run_", i)
#
#
# if __name__ == '__main__':
#     t = myThread()  # 创建对象
#     # t.run() # 这样就成方法的调用了
#     t.start()  # 线程就绪，待cpu启动
#
#     for i in range(8):
#         print("主线程" + str(i))


def func(name):
    for i in range(6):
        print(name, i)


if __name__ == '__main__':
    t1 = Thread(target=func, args=("线程一：",))  # args:传参数。必须是一个元组顾加逗号避免成为字符串
    t2 = Thread(target=func, args=("线程二：",))  # 传参必须是元组
    t1.start()
    t2.start()
