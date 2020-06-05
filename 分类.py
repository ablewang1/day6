from matplotlib import pyplot as plt
import numpy as np
import random

_x = [i/100 for i in range(1,100)]
_y = []
# _y1 = []
# _y2 = []
for i in _x:
    if i*100%2 > 0:
        _y.append(400*i+50+40*random.random())

        # _y1.append(400*i+50+40*random.random())
    else:
        _y.append(400*i-(50+40*random.random()))
        # _y2.append(400*i-(50+40*random.random()))
# _y.extend(_y1)
# _y.extend(_y2)
random.seed(5)
w = random.random()
b = random.random()

for i in range(50):
    for x,y in zip(_x,_y):
        z = w*x+b
        o = z-y
        loss = o ** 2

        dw = -2*o*x
        db = -2*o

        w = w + 0.02*dw
        b = b + 0.02*db
        print(w,b,loss)
print()
# plt.scatter(_x[:len(_y1)],_y1)
# plt.scatter(_x[len(_y1):],_y2)
plt.scatter(_x,_y)
v = [w*e+b for e in _x]
plt.plot(_x,v,'g')
plt.show()