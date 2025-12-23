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

r = remote("socket.cryptohack.org", 13379)
r.recvuntil("Send to Bob:")
r.sendline(b'{"supported": ["DH64"]}')
r.recvuntil("Send to Alice:")
r.sendline(b'{"chosen": "DH64"}')
r.recvuntil(b"Intercepted from Alice: ")
recv = r.readline().strip()
recv= json.loads(recv)
p= int(recv["p"], 16)
g= int(recv["g"], 16)
A= int(recv["A"], 16)
r.recvuntil(b"Intercepted from Bob: ")
recv = r.readline().strip()
recv= json.loads(recv)
B= int(recv["B"], 16)
r.recvuntil(b"Intercepted from Alice: ")
recv = r.readline().strip()
recv= json.loads(recv)
iv= recv["iv"]
ciphertext= recv["encrypted_flag"]
# for a in range(1000):
#     x= pow(g, a)% p
#     if x== A:
#         print(a)
#         break
from sympy.ntheory.residue_ntheory import *
a = discrete_log(p, A, g) 
shared_secret = pow(B, a, p)
print(decrypt_flag(shared_secret, iv, ciphertext))


#crypto{d0wn6r4d35_4r3_d4n63r0u5}
