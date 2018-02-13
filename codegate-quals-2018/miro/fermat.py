import sys
import multiprocessing as mp
import gmpy
import time

MAX_TASK = mp.cpu_count()
manager = mp.Manager()
queue = manager.Queue()
lock = manager.Lock()
finish = manager.Value('i',0)
n = 0
p = manager.Value('i',0)
q = manager.Value('i',0)
def slaves():
    while True:
        b2 = queue.get()
        if b2 is None:
            break
        if gmpy.is_square(gmpy.mpz(b2)):
            with lock:
                finish.value = 1
                a = gmpy.sqrt(n + b2);
                factor1 = a - gmpy.sqrt(b2)
                factor2 = a + gmpy.sqrt(b2)
                p.value = long(factor1.digits())
                q.value = long(factor2.digits())

def master(base, a):
    top = (n+1)/2
    while finish.value==0 and a<top:
        queue.put(base)
        base = base + 2*a + 1
        a = a + 1
    for i in range(MAX_TASK-1):
        queue.put(None)
        

def fermat(n):
    stime = time.time()
    pool = mp.Pool()
    a = gmpy.sqrt(n)
    base =  a*a - n
    pool.apply_async(master, args=(base, a,))
    for _ in range(MAX_TASK-1):
        pool.apply_async(slaves)
    pool.close()
    pool.join()
    etime = time.time()
    return (p.value,q.value)

if __name__ == '__main__':
    n = int(sys.argv[1])
    fermat(n)