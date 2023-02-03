# 线程池与进程池

# 线程池：一次性开辟一些线程，我们用户直接给线程池提交任务。线程任务的调度全部交给线程池
# from concurrent.futures import ThreadPoolExcutor, ProcessExcuter

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def fun(name):
    for i in range(1000):
        print(name, i)


if __name__ == '__main__':
    # 创建一个有50个任务的线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):  # 任务设置为100个
            t.submit(fun, name=(f"执行任务{i}",))
    # 等待线程池里面的任务全部执行完毕，才能继续执行（守护）
    print("123")





