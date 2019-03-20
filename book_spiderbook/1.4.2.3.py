#coding:utf-8
# 线程同步

import threading

mylock = threading.RLock()
num = 0


class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global num
        while True:
            mylock.acquire()
            print '%s locked, Number: %d' % (threading.current_thread().name, num)
            if num >= 4:
                mylock.release()
                print '%s released, Number: %d' % (threading.current_thread().name, num)
                break
            num += 1
            print '%s released, Number: %d' % (threading.current_thread().name, num)
            mylock.release()


if __name__ == '__main__':
    thread1 = myThread('Thread_1')
    thread2 = myThread('Thread_2')
    thread1.start()
    thread2.start()

'''
Thread_1 locked, Number: 0
Thread_1 released, Number: 1
Thread_1 locked, Number: 1
Thread_1 released, Number: 2

Thread_2 locked, Number: 2
Thread_2 released, Number: 3
Thread_2 locked, Number: 3
Thread_2 released, Number: 4
Thread_1 locked, Number: 4
Thread_1 released, Number: 4
Thread_2 locked, Number: 4
Thread_2 released, Number: 4

Process finished with exit code 0
'''