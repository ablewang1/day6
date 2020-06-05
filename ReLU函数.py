from matplotlib import pyplot as plt

x = [i for i in range(-20,50)]
y = []
for i in x:
    if i > 0:
        y.append(i)
    else:
        y.append(0)
print(x)
print(y)
plt.plot(x,y,"-")
plt.show()