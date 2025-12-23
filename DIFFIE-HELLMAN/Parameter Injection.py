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

r = remote("socket.cryptohack.org", 13371)
r.recvuntil("Send to Bob:")
r.sendline(b'{"p":"0x01", "g":"0x02", "A":"0x03"}')
r.recvuntil("Intercepted from Bob: ")
r.sendline(b'{"B":"0x01"}')
r.recvuntil(b"Intercepted from Alice: ")
recv = r.readline().strip()
recv= json.loads(recv)
iv = recv["iv"]
ciphertext = recv["encrypted_flag"]
shared_secret = 1
print(decrypt_flag(shared_secret, iv, ciphertext))


