from pwn import *
from gmpy2 import *
from Crypto.Util.number import *
import mt19937predictor
import time 
predictor = mt19937predictor.MT19937Predictor()
#r = remote("localhost",30002)
r = remote("problem.harekaze.com",30002)
print("start")
def get_nc():
    n = [0,0,0]
    c = [0,0,0]
    for i in range(3):
        r.readuntil(str(i+1)+". (")
        n[i] = int(r.readuntil(',')[:-1],16)
        r.readuntil(",")
        c[i] = int(r.readuntil(")")[:-1],16)
    return n,c

def get_d():
    d = [0,0,0]
    for i in range(3):
        r.readuntil(b'\xf0\x9f\x94\x91')
        r.readuntil(". ")
        d[i] = int(r.readuntil("\n"))
    return d

for _ in range(5):
    n,c = get_nc()
    r.sendline("1")
    d = get_d()
    for i in range(3):
        for j in range(3):
            m = long_to_bytes(pow(c[j],d[i],n[j]))
            if ("WIN".encode() in m) or ("LOSE".encode() in m):
                print(i)
                temp = bytes_to_long(m[-200:])
                predictor.setrandbits(temp, 200 * 8)
                break
            
e = 65537
while True:
    answer = None
    n,c = get_nc()
    for _ in range(3):
        padding = predictor.getrandbits(200 * 8).to_bytes(200, 'big')
        m = bytes_to_long(b'WIN \xf0\x9f\x92\x8e' + padding) 
        for i in range(3):
            if (c[i]-pow(m, e, n[i]))==0:
                answer = i
    assert answer is not None
    r.readuntil(">>>")
    r.sendline(str(answer+1))
    r.readline()
    print(r.readline())
    r.readline()
    for _ in range(3):
        r.readline()
    print(r.readline())
