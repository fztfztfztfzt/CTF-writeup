import random
import base64

def xor(msg, key):
    return bytes([ch1^ch2 for ch1, ch2 in zip(msg, key)])

random.seed("765753154007029226621575888896")
enc = base64.b64decode("7XDZk9F4ZI5WpcFOfej3Dbau3yc1kxUgqmRCPMkzgyYFGjsRJF9aMaLHyDU=")
key = bytes([random.randint(0,255) for _ in enc])
flag = xor(enc, key)
print(flag) #HarekazeCTF{3ul3rrrrrrrrr_t0000000t1nt!!!!!}