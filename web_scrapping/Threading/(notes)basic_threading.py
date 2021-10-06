import threading
import time
from queue import Queue
import copy

# def thread_job():
#     #打印线程的名称
#     print("this is an added Thread, nunber is %s"%threading.current_thread())
#
# def main():
#     #添加线程并给他一个任务
#     added_thread = threading.Thread(target=thread_job)
#     #运行线程
#     added_thread.start()
#     #查看线程数量
#     print(threading.active_count())
#     #查看线程详细信息
#     print(threading.enumerate())
#     #查看现在正在运行的线程是什么
#     print(threading.currentThread())
#
#
# if __name__ == '__main__':
#     main()
"""
运行结果：
    this is an added Thread, nunber is <Thread(Thread-1, started 2148)>
    1
    [<_MainThread(MainThread, started 18640)>]
    <_MainThread(MainThread, started 18640)>
thread_job中的内容先被打印是因为added_thread.start 在其他print内容的前面
"""



# def thread_job():
#     print("T1 start\n")
#     for i in range(10):
#         time.sleep(1)
#     print('T1 finish\n')
#
# def main():
#     # 通过name添加线程名字
#     added_thread = threading.Thread(target=thread_job,name = 'Ti')
#     added_thread.start()
#     print('all done\n')
# if __name__ == '__main__':
#     main()

"""
发现all done居然在T1 finish前面执行，，这是因为主函数不需要等待，
然而thread_job需要等待10秒，为了让主函数等待其他函数，需要用到join函数

T1 start

all done

T1 finish
"""


# def thread_job():
#     print("T1 start\n")
#     for i in range(10):
#         time.sleep(0.1)
#     print('T1 finish\n')
#
# def T2_job():
#     print("T2 start \n")
#     print('T2 finish\n')
#
# def main():
#     # 通过name添加线程名字
#     thread1 = threading.Thread(target=thread_job,name = 'T1')
#     thread2 = threading.Thread(target=T2_job(),name='T2')
#     thread1.start()
#     thread2.start()
#     #让主函数等待其他函数执行完
#     thread1.join()
#     thread2.join()
#
#     print('all done\n')
# if __name__ == '__main__':
#     main()

"""
使用join让所有子线程执行完再执行主线程
"""

# def job(l,q):
#     for i in range(len(l)):
#         l[i] = l[i]**2
#     #多线程不能用return，要用q.put(),将返回的L输出
#     #return l
#     q.put(l)
#
#
# def multithreading(data):
#     q = Queue()
#     threads = []
#     for i in range(4):
#         #args表示要传的参数
#         #注意，如果args里面只有一个值，则要这么写：arges = (q,)后面要加逗号
#         t = threading.Thread(target=job,args=(data[i],q))
#         t.start()
#         threads.append(t)
#     for thread in threads:
#         thread.join()
#     result = []
#     for _ in range(4):
#         result.append(q.get())
#     print (result)
#
# if __name__ == "__main__":
#     data = [[1, 2, 3], [4, 4, 4], [5, 5, 5], [3, 3, 3]]
#     multithreading(data)

"""
返回值：
    [[1, 4, 9], [16, 16, 16], [25, 25, 25], [9, 9, 9]]
print(threading.current_thread())
    <Thread(Thread-1, started 11564)>
    <Thread(Thread-2, started 5644)>
    <Thread(Thread-3, started 5584)>
    <Thread(Thread-4, started 12780)>
"""


# def job(l,q):
#     res = sum(l)
#     q.put(res)
#
# def multithreading(l):
#     q = Queue()
#     threads = []
#     for i in range(4):
#         t = threading.Thread(target=job, args = (copy.copy(l),q),name = "T%i"%i)
#         t.start()
#         threads.append(t)
#     #if循环的缩写模式
#     [t.join()for t in threads]
#     total = 0
#     for _ in range (4):
#         total += q.get()
#     print(total)
#
# def normal(l):
#     total = sum(l)
#     print(total)
#
# if __name__ == "__main__":
#     l = list(range(1000000))
#     s_t = time.time()
#     normal(l*4)
#     print('normal:',time.time()-s_t)
#     s_t = time.time()
#     multithreading(l)
#     print('multithreading:',time.time()-s_t)

"""
返回值：
    1999998000000
    normal: 0.11369538307189941
    1999998000000
    multithreading: 0.11971712112426758 
    
python多线程运算并不是真正的多线程，因为有GIL（global interpret lock）限制每次只能一个线程进行运算

打印从0开始的10个数字
l = list(range(10))
print(l)
"""

# def job1():
#     #定义一个全局变量 A
#     global A,lock
#     #开始lock这个线程
#     lock.acquire()
#     for i in range(10):
#         A += 1
#         print('job1',A)
#     #解锁lock，解锁前，job2会等待job1运行完
#     lock.release()
# def job2():
#     global A,lock
#     lock.acquire()
#     for i in range(10):
#         A += 10
#         print('job2',A)
#     lock.release()
#
# if __name__=="__main__":
#     lock = threading.Lock()
#     A = 0
#     t1 = threading.Thread(target=job1)
#     t2 = threading.Thread(target=job2)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()


#继承父类：在MyThread里面写要继承哪一个父类，这里集成的是threading.Thread
class MyThread(threading.Thread):
    #集成父类后，要重写run方法
    def run(self):
        for i in range(5):
            #打印线程名字
            print(self.name + str(i))

if __name__=="__main__":
    t = MyThread()
    t.start()


    pass
