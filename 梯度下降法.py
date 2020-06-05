import numpy as np
from matplotlib import pyplot as plt
import random
_x = [i/100 for i in range(100)]
_y = [3*e+9+random.random() for e in _x]

w = random.random()
b = random.random()
plt.ion()
for i in range(60):
    for x,y in zip(_x,_y):
        z = w*x+b
        o = z - y
        loss = o ** 3

        dw = 2*o*x
        db = 2*o

        w = w - 0.01*dw
        b = b - 0.01*db

        print(w,b,o)
    v = [w * e + b for e in _x]
    plt.cla()
    plt.plot(_x,v)
    plt.plot(_x,_y,".")
    plt.title(loss)
    plt.pause(0.01)
plt.ioff()
# v = [e*w+b for e in _x]
# plt.plot(_x,v,"-")
plt.show()