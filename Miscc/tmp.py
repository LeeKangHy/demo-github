import hashlib
import time
import socket
from Crypto.Util.number import long_to_bytes

'''
A dirty but working solution
'''


def decrypt(enc,time):
    key = hashlib.sha256(long_to_bytes(time)).digest()
    plain=b''
    for i in range(len(enc)):
        plain += bytes([enc[i] ^ key[i]])
    return plain



s = socket.socket()
s.connect(("socket.cryptohack.org",13372))

s.recv(2048) # print( "Gotta go fast!\n" )

start=int(time.time())
s.send('{"option":"get_flag"}\n'.encode())

x=s.recv(2048).decode()
encrypted=bytes.fromhex(x.split(': "')[1].split('"')[0])

for i in range(start-100000,start+100000): #Just bruteforce timestamp
    o=decrypt(encrypted,i)
    if o[:6]==b"crypto": # All flags start with "crypto"
        print(o.decode())