# -*- coding: utf-8 -*-

import threadpool


def hello(a):
    return 'hello: %s' % a


def world(a, b):
    return 'world: %s, %s' % (a, b)


def foobar(a, b, c):
    return 'foobar: %s, %s, %s' % (a, b, c)


def print_result(req, result):
    print('The result is %s %s' % (req.requestID, result))


if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]

    lst1 = (6, 6)
    lst2 = (7, 7)
    lst3 = (8, 8)
    data2 = [(lst1, None), (lst2, None), (lst3, None)]

    dct1 = {'a': 8, 'b': 9, 'c': 10}
    dct2 = {'a': 11, 'b': 12, 'c': 13}
    data3 = [(None, dct1), (None, dct2)]

    pool = threadpool.ThreadPool(5)
    requests1 = threadpool.makeRequests(hello, data1, print_result)
    requests2 = threadpool.makeRequests(world, data2, print_result)
    requests3 = threadpool.makeRequests(foobar, data3, print_result)

    [pool.putRequest(req) for req in requests1]
    [pool.putRequest(req) for req in requests2]
    [pool.putRequest(req) for req in requests3]

    pool.wait()
