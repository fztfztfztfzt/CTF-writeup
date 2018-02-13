import socket
import re
#from Crypto.Util.number import *
#from gmpy2 import *
pattern = re.compile(r'\d\.\s\(.*\)') 
pattern2 = re.compile(r'\d\.\s\d+') 
HOST = 'problem.harekaze.com'
PORT = 30214

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

win = 6289644257982517902
print "start"
#n = [0 for i in range(3)]
#c = [0 for i in range(3)]
while True:
    data = s.recv(10240)
    print data
    data2 = pattern2.findall(data)
    data = pattern.findall(data)
    #n1 = [n[i] for i in range(3)]
    #c1 = [c[i] for i in range(3)]
    n = [0 for i in range(3)]
    c = [0 for i in range(3)]
    for i in range(3):
        data[i] = data[i][4:-1]
        data[i] = data[i].split(",")
        n[i] = int(data[i][0],16)
        c[i] = int(data[i][2],16)
    #print n
    #print c
    """
    if len(data2)==3:
        for i in range(3):
            data2[i] = int(data2[i][3:])
        print data2
        s = data2
        for d in [[s[0],s[1],s[2]],[s[0],s[2],s[1]],[s[1],s[0],s[2]],[s[1],s[2],s[0]],[s[2],s[0],s[1]],[s[2],s[1],s[0]]]:
            print "==================="
            haha = [ pow(c1[i], d[i], n1[i]) for i in range(3) ]
            for i in range(3):
                print haha[i]
    """
    for i in range(3):
        print i,
        print pow(win,65537,n[i])-c[i]==0
        if pow(win,65537,n[i])-c[i]==0:
            s.send(str(i+1)+'\n')
