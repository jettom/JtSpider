#第二种方法：使用multiprocessing模块创建多进程
import os
from multiprocessing import Process
# 子进程要执行的代码
def run_proc(name):
    print('Child process %s (%s) Running...' % (name, os.getpid()))
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p_list=[]
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        p_list.append(p)
        print('Process will start.')
        p_list[i].start()
    for p in p_list:
        p.join()
    print('Process end.')

'''
Parent process 3273.
Process will start.
Process will start.
Process will start.
Child process 0 (3274) Running...
Process will start.
Child process 1 (3275) Running...
Process will start.
Child process 2 (3276) Running...
Child process 3 (3277) Running...
Child process 4 (3278) Running...
Process end.
'''
