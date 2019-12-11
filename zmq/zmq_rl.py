import time

import zmq


def sent():
    context = zmq.Context()
    print('connect to hello world server')
    socket = context.socket(zmq.REQ)
    socket.connect('tcp://localhost:5555')

    for request in range(1, 10):
        print('send ', request, '...')
        socket.send_string('hello')
        message = socket.recv()
        print('received reply', request, '[', message, ']')


def pub():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://127.0.0.1:5555")
    while True:
        topic = input("input topic:")
        msg = input('input data:')
        # socket.send(msg)
        socket.send_pyobj([topic, msg])
        time.sleep(0.1)


if __name__ == '__main__':
    pub()
