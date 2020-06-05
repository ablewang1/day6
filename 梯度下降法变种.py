import numpy as np
from matplotlib import pyplot as plt
import random
from sklearn import datasets
import torch

def tanh1(x):
    return np.tanh(x)

x,y = datasets.samples_generator.make_blobs(n_samples=10,centers=2,cluster_std=1,random_state=20)
# print(x)
# print(y)
# d1 = []
# d2 = []
a = random.random()
b = random.random()
c = random.random()

# d1 = random.random()
# d2 = random.random()
for i in range(30):
    plt.ion()
    for _x,_y in zip(x,y):
        if _y == 0:
            # d1.append([_x,_y])
            o = _x[0] * a + _x[1]*b +c# - d1

        elif _y == 1:
            # d2.append([_x,_y])
            o = _x[0] * a + _x[1]*b +c# - d2  #< 0

        loss = (o ** 2)/(a**2+b**2)
        da = -(2*o*(a**2+b**2)*_x[0] - (o**2)*2*a)/(a**2+b**2)
        db = -(2*o*(a**2+b**2)*_x[1] - (o**2)*2*b)/(a**2+b**2)
        dc = -2*o
        # dd1 = -2*o/(a**2+b**2)
        # dd2 = -
        a = a + 0.01 * da
        b = b + 0.01 * db
        c = c + 0.01 * dc
    print(loss)


    plt.cla()
    x1 = [0,-c/b]
    y1 = [-c/a,0]
    plt.plot(x1,y1)
    plt.scatter(x[:, 0], x[:, 1], c=y)
    plt.pause(0.1)
#
# d1 = list(np.array(d1))
# d2 = list(np.array(d2))

# plt.plot(d2[0],d2[1],'.')
plt.ioff()
plt.show()
#
#
# print(d1)
# print(d2)


# #根据线随机生成数据 失败原因：直线所有值构成一个真空
# x1 = []
# y1 = []
# x = np.arange(0,45)
# y = 10*x+5
# while True:
#     num = random.randint(0, 20)
#     if num > ((y+x)-1).any():
#         x1.append(num)
#     if len(x1) == 45:
#         break
# print("x1",x1)
# plt.plot(x,x1,'.')
# plt.plot(x,y)

# while True:
#     num = random.randint(0, 20)
#     if num < y.any():
#         y1.append(num)
#     if len(y1) == 45:
#         break
# print("y1",y1)
# plt.plot(x[::-1],y1,'.')



#
# x1 = np.random.randint(0,15+3*np.random.random(),50)
# y1 = np.random.randint(10,15+3*np.random.random(),50)
# x2 = np.random.randint(15,35+2*np.random.random(),50)
# y2 = np.random.randint(5,10+2*np.random.random(),50)
#
# x = np.hstack([x1, x2])
# y = np.hstack([y1, y2])
#
#
# # for i in range(500):
# #     if -3 < y[i] - x[i] < 3:
# #         x[i] -= 1
# #         y[i] += 1
# #
# w = random.random()
# b = random.random()
# plt.ion()
# for i in range(3):
#     for _x,_y in zip(x,y):
#         if (w * _x[0] + b )*_y != 0:
#             # o = (w * _x[0] + b - _x[1])/2
#             o = 1
#         else:
#             # o = (w * _x[1] + b - _x[0])/2
#             o = 0
#
#
#         loss = o ** 2
#
#         dw = -2*o*_x[0]
#         db = -2*o
#
#         w = w + 0.01 * dw
#         b = b + 0.01 * db
#     print(loss)
# # print("*"*20)
# # print("w",w)
#     plt.cla()
#     v = [e*w+b for e in x[:,0]]
#     plt.plot(x[:,0],v)
#     # y = 2*y-1
#     plt.scatter(x[:, 0], x[:, 1], s=100, c=y)
#     plt.pause(0.1)
# plt.ioff()
#
# # # plt.plot(x,y,".")
# # #
# # # plt.plot(x1,y1,'.')
# # # plt.plot(x2,y2,'.')
# # plt.plot(x,y,'.')
#
# plt.show()

