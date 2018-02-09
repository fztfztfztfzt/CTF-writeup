from hashlib import md5

def foo(h, m):
    return md5(h.encode('utf-8') + m.encode('utf-8')).hexdigest()[:4]

def solve(hl,hr):
    for i in xrange(2**16):
        for j in xrange(2**16):
            l = '{:04x}'.format(i)
            m = '{:04x}'.format(j)
            if foo(l, m)==hl:
                for k in xrange(2**16):
                    r = '{:04x}'.format(k)
                    if foo(r, m) == hr:
                        return m,l,r

left = '260c'
right = '01da'
message = ""
for _ in range(4):
    m,left,right = solve(left,right)
    message = m+message
                    
print('message: {}, hl: {}, hr: {}'.format(message, left, right))
