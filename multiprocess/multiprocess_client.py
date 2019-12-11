
import sys
from multiprocessing import Lock, Process


def worker_with(lock: Lock, f: str):
    with lock:
        with open(f, mode="a+") as fs:
            fs.write("Lock acquired via with.\n")


def worker_no_with(lock: Lock, f: str):
    lock.acquire()
    try:
        with open(f, "a+") as fs:
            fs.write("Lock acquired directly.\n")
    finally:
        lock.release()


if __name__ == '__main__':
    f = "t.txt"
    lock = Lock()
    w = Process(target=worker_with, args=(lock, f))
    nw = Process(target=worker_no_with, args=(lock, f))
    w.start()
    nw.start()
    w.join()
    nw.join()
    