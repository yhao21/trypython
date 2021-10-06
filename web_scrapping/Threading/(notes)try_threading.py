#使用线程库
import threading
#使用队列
import queue
#解析库
from lxml import etree

import requests
#json处理
import json

#采集的退出信号
CRAWL_EXIT = False
#解析的退出信号
PARSE_EXIT = False


#父类线程
#继承父类：在MyThread里面写要继承哪一个父类，这里集成的是threading.Thread
class ThreadCrawl(threading.Thread):
    #父类初始化，线程名，两个队列
    def __init__(self,ThreadName,pageQueue,dataQueue):
        #如何调用线程初始化，下面两种都可以，super的好处：如果有代码重做，要多个父类，只需改上面父类ThreadCrawl括号里的内容即可，无需修改super的内容。
        # threading.Thread.__init__(self)
        super(ThreadCrawl, self).__init__()
        #线程名
        self.threadname = ThreadName
        #页面队列
        self.pagequeue = pageQueue
        self.dataqueue = dataQueue
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}


    def run(self):
        ##每个线程要一直执行，结束条件为队列为空
        while not CRAWL_EXIT:
            #从页面队列中取出一个页码，先进先出规则
            #get里有一个可选参数block，默认为True：
            #如果队列为空，block为true，则进入堵塞状态，直到队列有新的数据
            #另一种情况：如果队列为空，block为false，则弹出一个queue.empty()异常，并结束
            #通常我们会用第二个，因为第一个不会结束，只会进入阻塞，
            try:

                page = self.pagequeue.get(False)
                url = "https://www.bilibili.com/video/av78270678?p=" + str(page)
                content = requests.get(url,headers = self.headers)
                #把内容放入data队列
                self.dataqueue.put(content)
            except:
                pass


def main():
    #野马队列，表示一次执行10页
    pageQueue = queue.Queue(10)
    for i in range(1,11):
        #把页码放入队列，注意是先进先出
        pageQueue.put(i)
    #采集结果（每页的html源码）的数据队列，参数为空表示不限制数量
    dataQueue = queue.Queue()

    #三个采集线程的名字
    crawlList = ["采集线程1号","采集线程2号","采集线程3号"]
    #保存线程
    threadcrawl = []
    #存储三个采集线程
    for ThreadName in crawlList:
        #创建一个采集类ThreadCrawl，把name，page和dataqueue传进这个类里
        thread = ThreadCrawl(ThreadName, pageQueue,dataQueue)
        #线程执行
        thread.start()
        # 存储三个采集线程
        threadcrawl.append(thread)


    #解析线程

    #若队列不为空则等待之前的操作执行完毕
    while not pageQueue.empty():
        pass
    #如果pagequeue为空，采集线程退出循环
    ##通过global把CRAWL_EXIT变成可以全局修改的全局变量，
    ##因为，如果不声明为全局变量，在run()函数里的crawl_exit无法被修改，而我们想要修改的恰恰就是run中的
    global CRAWL_EXIT
    CRAWL_EXIT = True

    print("pagequeue is empty")

    #添加阻塞
    for thread in threadcrawl:
        thread.join()
        print ("1")





if __name__ == "__main__":
    main()