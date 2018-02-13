from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import gmpy 

def fermat(N):
    a = gmpy.sqrt(N)
    b2 = a*a - N
    while not gmpy.is_square(gmpy.mpz(b2)):
        b2 += 2*a + 1
        a += 1
    factor1 = a - gmpy.sqrt(b2)
    factor2 = a + gmpy.sqrt(b2)
    return (long(factor1.digits()), long(factor2.digits()))

pem = open("public.pem").read()
key = RSA.importKey(pem)
n = key.n
e = key.e
print "n:",n
print "e:",e
p,q=fermat(n)
print "p:",p
print "q:",q
phi=(p-1)*(q-1)
d=inverse(e,phi)

g=open('privkey.key','wb')
priv = RSA.construct((n,e,d))
g.write(priv.exportKey('PEM'))
g.close()