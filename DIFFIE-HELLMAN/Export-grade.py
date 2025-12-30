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

print(r.readline())
 #b'Intercepted from Alice: {"supported": ["DH1536", "DH1024", "DH512", "DH256", "DH128", "DH64"]}\n'

r.sendline(b'{"supported": ["DH64"]}') 
print(r.readline())
 #b'Send to Bob: Intercepted from Bob: {"chosen": "DH64"}\n'

r.sendline(b'{"chosen": "DH64"}')
#print(r.readline())
 #b'Send to Alice: Intercepted from Alice: {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0xb37e57b96c63f55e"}\n'

"""bắt dữ liệu"""
print(r.recvuntil(b"Intercepted from Alice: "))
recv = r.readline().strip()
recv= json.loads(recv)              # chuyển string json -> dict Python      
p= int(recv["p"], 16)
g= int(recv["g"], 16)
A= int(recv["A"], 16)

"""tiếp tục đọc server"""
#print(r.readline())
 #b'Intercepted from Bob: {"B": "..."}\n'
"""bắt dữ liệu"""
print(r.recvuntil(b"Intercepted from Bob: "))
recv = r.readline().strip()
recv = json.loads(recv)
B = int(recv["B"],16)

#print(r.readline()) 
 #b'Intercepted from Alice: {"iv": "...", "encrypted_flag": "..."}\n'

"""bắt dữ liệu"""
print(r.recvuntil(b"Intercepted from Alice: "))
recv = r.readline().strip()
recv = json.loads(recv) 
iv = recv["iv"]
ciphertext = recv["encrypted_flag"]


"""Có p,g,A,B rồi , tiến hành tìm ra secret_key giữa Bob và Alice"""

#Brute force (đpt : O(p)) để tìm a với p <10^6 
#thư viện dùng thuật toán Baby-Step Giant-Step (BSGS) , độ phức tạp O(sqrt(p))
from sympy.ntheory.residue_ntheory import discrete_log
a = discrete_log(p, A, g) 
#print(a)
shared_secret = pow(B,a,p)
flag = decrypt_flag(shared_secret,iv,ciphertext)
print(flag)



#crypto{d0wn6r4d35_4r3_d4n63r0u5}


"""MÔ TẢ KỊCH BẢN"""
# Bước 1: Alice → Bob (bị Max chặn)
# Alice gửi:
# {"supported": ["DH1536", "DH1024", "DH512", "DH256", "DH128", "DH64"]}
# Max sửa:
# {"supported": ["DH64"]}


# Bước 2: Bob chọn tham số
# Bob nghĩ:“Alice chỉ hỗ trợ DH64”
# Bob trả lời:{"chosen": "DH64"}
# Max chuyển nguyên vẹn cho Alice.


# Bước 3: Alice & Bob trao đổi Diffie–Hellman
# p chỉ 64-bit
# Không còn an toàn
# Max nghe lén toàn bộ:
# p, g
# A = gᵃ mod p
# B = gᵇ mod p

# Bước 4: Max phá Diffie–Hellman
# Vì p = 64-bit:
# Giải discrete log trong vài giây
# Tìm được:a hoặc b
# Tính được:shared_secret = g^(ab) mod p


# Bước 5: Giải mã toàn bộ dữ liệu
# Alice và Bob dùng:SHA1(shared_secret) ; AES-CBC
# Max có:key,iv,ciphertext
# -->Giải mã flag / message 