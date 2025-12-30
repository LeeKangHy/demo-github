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

HOST = "socket.cryptohack.org"
port = 13371
r = remote(HOST, port)
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

print(recv["iv"])
print(recv["encrypted_flag"])
print(decrypt_flag(shared_secret, iv, ciphertext))




"""Mô tả"""
# Kịch bản MITM trong DH 
# Bước 1: Alice gửi A = g^a mod p

# Mallory chặn lại, không chuyển cho Bob

# Bước 2: Mallory gửi A' = g^m1 cho Bob

# Bob tưởng đó là của Alice

# Bước 3: Bob gửi B = g^b

# Mallory chặn lại

# Bước 4: Mallory gửi B' = g^m2 cho Alice


#Lưu ý thực hiện chat với server bằng câu lệnh r.printline() để hiểu server nói gì
# iv và encrypted_flag là động (nghĩa là giá trị thay đổi sau mỗi lần chạy server) 
#vì vậy cần viết code trực tiếp để bắt thông tin (chứ không phải là copy-paste giá trị đọc được ở 1 lần chat với server)

