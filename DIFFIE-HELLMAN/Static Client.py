from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib
from pwn import *
import json
def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))
def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

r = remote("socket.cryptohack.org", 13373)
r.recvuntil(b"Intercepted from Alice: ")
recv = r.readline().strip()
recv= json.loads(recv)
p= recv["p"]
g= int(recv["g"], 16)
A= recv["A"]
r.recvuntil(b"Intercepted from Bob: ")
recv = r.readline().strip()
recv= json.loads(recv)
B= int(recv["B"], 16)
r.recvuntil(b"Intercepted from Alice: ")
recv = r.readline().strip()
recv= json.loads(recv)
iv= recv["iv"]
ciphertext= recv["encrypted"]
r.recvuntil("Bob connects to you, send him some parameters: ")
r.sendline(json.dumps({"p": p, "g": A, "A": "0x01"}))
r.recvuntil("Bob says to you: ")
recv = r.readline().strip()
recv= json.loads(recv)
shared_secret= int(recv["B"], 16)
print(decrypt_flag(shared_secret, iv, ciphertext))


#crypto{n07_3ph3m3r4l_3n0u6h}