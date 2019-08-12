import torch


if __name__ == '__main__':
    a = torch.FloatTensor(2, 3)
    print(a)
    b = torch.FloatTensor([2, 3, 4, 5])
    print(b)
    c = torch.IntTensor(2, 3)
    print(c)
    d = torch.IntTensor([2, 3, 4, 5])
    print(d)
    e = torch.rand(2, 4)
    print(e)
    print(type(e))
    f = torch.randn(2, 3)
    print(f)
    g = torch.range(2, 8, 1)
    print(g)

    h = torch.zeros(2, 3)
    print(h)
    i = torch.abs(f)
    print(i)

