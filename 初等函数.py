import numpy as np
from matplotlib import pyplot as plt
import torch
plt.style.use('ggplot')

# x = torch.tensor([3.0],requires_grad=True)
# y = x**3
# y.backward()
# print(x.grad)
# # print(torch.autograd.grad(y,x))


# x = np.arange(-20,20,0.5)
# # y = np.ones(x.shape)*3
# y = np.tile(3,x.shape)
# plt.plot(x,y)

# y1 = x ** 3
# plt.plot(x,y1)

# y2 = x ** 2
# plt.plot(x,y2)

# y3 = x
# plt.plot(x,y3)

# try:
#     y4 = 1 / x
#
#     plt.plot(x,y4)
# except:
#     pass

# x1 = np.arange(0.1,40,0.1)
# y1 = x1**0.5
# plt.plot(x1,y1)

# x = np.arange(-2,2,0.1)
# y1 = 0.5**x
# y2 = 2**x
# plt.plot(x,y1)
# plt.plot(x,y2)

# x = np.arange(0.1,5,0.1)
# y = np.log(x)
# y1 = np.log(x)/np.log(0.5)
# print(x)
# print(y)
# plt.plot(x,y)
# plt.plot(x,y1)

# x = np.arange(-2*np.pi,2*np.pi,0.1)
# y = np.sin(x)
# y1 = np.cos(x)
# plt.plot(x,y)
# plt.plot(x,y1)

# x = np.arange(-2*np.pi*8,2*np.pi*8,0.1)
# y = np.sinc(x)
# plt.plot(x,y)

# x = np.arange(-np.pi,np.pi,0.01)
# y = np.tanh(x)
# plt.plot(x,y)

# #对数函数压缩数据
# x = np.arange(0.01,5,0.01)
# y = (x-2)**2+1
# plt.plot(x,y)
# plt.plot(x,np.log(y))

# #正态分布
# x = np.arange(-20,20,0.1)
# y = (1/((2*np.pi)**0.5*3))*np.exp(-(x-4)**2/(2*9))
# plt.plot(x,y)

# #Sigmoid
# x = np.arange(-20,20,0.1)
# y = 1/(1+np.exp(-x))
# plt.plot(x,y)




plt.ion()
for i in np.arange(-15,15):
    x = np.arange(-5,15,0.1)
    y = [4*e+i for e in x]
    y = [1/(1+np.e**(-e)) for e in y]
    y1 = [(np.e**(j)-np.e**(-j))/(np.e**(j) + np.e**(-j)) for j in y]
    plt.cla()
    plt.plot(x,y)
    plt.plot(x,y1)
    plt.pause(0.1)

for i in np.arange(-15,15):
    x = np.arange(-5,15,0.1)
    y = [i*e+5 for e in x]
    y = [1/(1+np.e**(-e)) for e in y]
    y1 = [(np.e**(j)-np.e**(-j))/(np.e**(j) + np.e**(-j)) for j in y]

    plt.cla()
    plt.plot(x,y)
    plt.plot(x,y1)
    plt.pause(0.001)
    plt.ioff()
plt.show()