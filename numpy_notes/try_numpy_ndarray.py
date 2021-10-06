# ##use numpy compute a^2+b^3
import numpy as np
#
# def npSum():
#     a = np.array([0,1,2,3,4])
#     b = np.array([9,8,7,6,5])
#     c = a**2 + b**3
#     return c
# print(npSum())


##获得数组维度
# import numpy as np
#
# a = np.array([[0,1,2,3,4],
#              [9,8,7,6,5]])
# # print (a.ndim)
# # ##返回值2，即，有两组数据，维度为2
# # print (a.shape)
# # ##返回（2.5）表示两行五列
# # print (a.size)
# # ##返回10， 表示一共10个元素
# # print (a.dtype)
# # #返回int32表示32位的整数类型
# ##创建数组的方法x=np.array(数组，数据类型）
# x = np.array(a,dtype=int)
# print (x)
# ##将a数组引入x数组，数据类型定义为整数

# x = np.arange(4)
# print (x)
#返回值：[0 1 2 3]
# x = np.ones((3,6))
# print (x)
# # 返回：
# # # [[1. 1. 1. 1. 1. 1.]
# # #  [1. 1. 1. 1. 1. 1.]
# # #  [1. 1. 1. 1. 1. 1.]]

# x = np.zeros((2,3))
# print(x)
# ##返回：
# ##[[0. 0. 0.]
# ## [0. 0. 0.]]

# x = np.eye(3)
# print (x)
# ##
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]