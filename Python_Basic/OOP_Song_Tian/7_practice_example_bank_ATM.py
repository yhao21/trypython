import time
import numpy as np

"""
问题假设：
ATM机器服务时间：在1到maxtime间随机(对每一个客户，atm工作的最大时间是多少）
客户流:n个客户到达时间在1到arrivetime间随机（一个客户到达的时间与下一个客户到达时间的差额）
所有时间以整数为单位
进一步扩展可以采用随机分布函数


面向对象程序思路：
思考封装对象，以及对象间如何交互
    本案例中对象：    
                ATM机：   ATM类（假设只有1个机器）
                客户流：  Customers类
需要解决的问题是：
    每个客户的等待时间是多少                
"""
class ATM():
    def __init__(self,maxtime = 5):
        self.t_max = maxtime
    def getServComleteTime(self, start = 0):
        #从1到5，模拟完成一次业务的时间
        return start + np.random.randint(1,self.t_max)

class Customers():
    def __init__(self, n):
        self.count = n
        self.left = n
    def getNextArrvTime(self,start = 0, arrvtime = 10):
        if self.left != 0:
            self.left =self.left - 1
            return start + np.random.randint(1,arrvtime)
        else:
            return 0
    def isOver(self):
        return True if self.left == 0 else False