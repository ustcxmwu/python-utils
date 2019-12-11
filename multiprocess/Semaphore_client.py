from multiprocessing import current_process, Semaphore, Process
import time


def worker(s: Semaphore, i: int):
    s.acquire()
    print(current_process().name + "acquire")
    time.sleep(i)
    print(current_process().name + "release")
    s.release()


if __name__ == '__main__':
    s = Semaphore(2)
    for i in range(5):
        p = Process(target=worker, args=(s, i))
        p.start()
