import torch
from torch import optim
from matplotlib import pyplot as plt

# 直线数据
# x = torch.arange(0,10,0.1)
# y = 3 * x + 6 + 3*torch.rand(100)

# 曲线数据
x = torch.arange(0, 1, 0.01)
# y = x ** 3 + x - 3 * x ** 2 + 6 + torch.rand(100) / 10
y = x ** 3 + 6 + torch.rand(100) / 10



# plt.plot(x,y,'.')
# plt.show()
# exit()
# print(y)
# def active(x):
#     return x ** 2


class Line(torch.nn.Module):
    def __init__(self):
        super().__init__()

        self.w1 = torch.nn.Parameter(torch.rand(1))
        self.b = torch.nn.Parameter(torch.rand(1))

    def forward(self, x):
        # print("***************", self.w.grad, self.b.grad)
        # return self.w1 * x + self.w2 * x ** 2 + self.w3 * x ** 3 + self.b
        return self.w1*x**3 + self.b

if __name__ == '__main__':
    line = Line()

    # opt = optim.SGD(line.parameters(),lr=0.0002,momentum=0.0005)
    opt = optim.Adam(line.parameters(), lr=0.002)

    loss = torch.nn.MSELoss()
    plt.ion()
    for i in range(200):
        for _x, _y in zip(x, y):
            # z = line()

            output = line.forward(_x)
            ls = loss(output, _y)
            opt.zero_grad()
            ls.backward()
            opt.step()
        # for _x,_y in zip(x,y):
        #     z = line(_x)
        #     # z = line.forward(_x)
        #     loss = (z-_y)**2
        #     # loss(_y,z)
        #     opt.zero_grad()
        #     loss.backward()
        #     opt.step()
        #     print(loss)
        # v = [line.w1 * e + line.w2 * e ** 2 + line.w3 * e ** 3 + line.b for e in x]
        v = [line.w1 * i ** 3 + line.b for i in x]

        plt.cla()
        plt.plot(x, v)
        plt.plot(x, y, '.')
        plt.title(ls.item())
        plt.pause(0.01)
    plt.ioff()
    plt.show()
