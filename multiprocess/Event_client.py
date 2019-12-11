from multiprocessing import Event, Process
import time


def wait_for_event(e: Event):
    print("wait for envert: start")
    e.wait()
    print("wait for event: e.is_set() ->" + str(e.is_set()))


def wait_for_event_timeout(e: Event, t: float):
    print("wait for event timeout: starting")
    e.wait(t)
    print("wait for event timeout: e.is_set()->" + str(e.is_set()))


if __name__ == '__main__':
    e = Event()
    w1 = Process(name="block", target=wait_for_event, args=(e,))
    w1.start()

    w2 = Process(name="non-block", target=wait_for_event_timeout, args=(e, 2))
    w2.start()

    time.sleep(3)
    e.set()
    print("main: event is set")
