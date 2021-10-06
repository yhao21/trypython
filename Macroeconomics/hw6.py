#
#
from scipy import optimize
import matplotlib.pyplot as plt


# def f(x):
#  C1,C2 = x.tolist()
#
# #下面的写法是上面代码的完整模式：
#  # C1 = x.tolist()
#  # C2 = x.tolist()
#
#  return [(1/0.98)*(C1/C2)**(-2)-1-0.5*(2-C1)**(-3/4),C2-2*(2-C1)**(1/4)-2+C1]
# result = optimize.fsolve(f,[0.1,1])
# print(result)






# def f(x):
#  C1,C2 = x.tolist()
#
#  return [(1/0.98)*(C1/C2)**(-2)-1-0.3*(2-C1)**(-3/4),
#          C2-1.2*(2-C1)**(1/4)-2+C1]
# result = optimize.fsolve(f,[0.1,1])
# print(result)


# def f(x):
#  C1,C2 = x.tolist()
#
#  return [(1/0.98)*(C1/C2)**(-1/3)-1-0.5*(2-C1)**(-3/4),
#          C2-2*(2-C1)**(1/4)-2+C1]
# result = optimize.fsolve(f,[0.1,1])
# print(result)



def f(x):
 C1,C2 = x.tolist()

 return [(1/0.98)*(C1/C2)**(-1/3)-1-0.3*(2-C1)**(-3/4),
         C2-1.2*(2-C1)**(1/4)-2+C1]
result = optimize.fsolve(f,[0.1,1])
print(result)


# from sympy import *
#
# C1 = symbols('C1')
# C2 = symbols('C2')
#
# result = solve([
#     C2 - 2 * ((2 - C1) ** (1/4)) - 2 + C1,
#     (1/0.98) * ((C1/C2) ** (-2)) - 1 - 0.5 * ((2 - C1) ** (-3/4))
# ],[C1,C2])
#
# print(result)