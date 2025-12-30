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

print(r.readline())
  # b'Intercepted from Alice: {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", 
  # "g": "0x02",
  # "A": "0xdac983255bcad01db828648b29af7ca3d4fa9d59712217af7a8785d66dc4e0579e01b3d91ec6f791496373abdb6ec9fe70f3f02b0f3d9b7479dced1409202c63dbda9e0e6417acd5a4e39fa937203f0c9c30abccf44ddb65e19e718e61c99d7b70ae49a6fb21c0c04769999e25d138cb70b9302e5413f43c379f9c2afb94012eef7213116716b28aa95df86b748fbbb931b4ddf66e1a466bbdc00aa1c421b3485cc36392824cc2ff5c2ba2ec4cd33d4812abcd264e873e4e9ace3454c614ba9f"}\n'

r.sendline(b'{"p": "0x01324","g" : "0x02345", "A" :"0x02343"}')      #gửi gì cũng được, không quan trọng bài này chỉ muốn mô tả kịch bản MITM trong DH thôi
                                                                     #nếu gửi p = 1 thì dễ tính luôn được B = 0 (Do B = g^b mod p = g^b mod 1 = 0)
print(r.readline())
 #b'Send to Bob: Intercepted from Bob: {"B": "0x0"}\n'

r.sendline(b'{"B" : "0x01"}')          #Gửi B = 1 để dễ tính luôn khóa bí mật giữa Max và Alice = 1

#print(r.readline())  
 #b'Send to Alice: Intercepted from Alice: {"iv": "a4c5cbd86949b979573eb88171641803", "encrypted_flag": "9241592a3bdee4fbd02e09d856dc5fc84ba5116c09bb27a983aae80a856f50d2"}\n'
print(r.recvuntil(b"Intercepted from Alice: "))  # in ra đến hết "Intercepted from Alice: " thì dừng
recv = r.readline().strip()     #hàm strip() là hàm xử lý chuỗi (string / bytes) dùng để xóa các ký tự “thừa” ở đầu và cuối, thường gặp nhất là newline, space khi đọc dữ liệu từ socket / file. 
                                # cụ thể ở đây hàm strip() giúp gọt bớt phần "\n"      
 # lúc này recv = {"iv": "...", "encrypted_flag": "..."}
recv= json.loads(recv)       # chuyển string json -> dict Python

"""tiến hành bắt dữ liệu"""

iv = recv["iv"]
ciphertext = recv["encrypted_flag"]
shared_secret = 1               #do Max đã tiêm B = 1 cho Alice
print(decrypt_flag(shared_secret, iv, ciphertext))





"""Mô tả"""
# Kịch bản MITM trong DH 

# Bước 1: Alice gửi A = g^a mod p
# Max chặn lại, không chuyển cho Bob
# Bước 2: Max gửi A' = g^m1 cho Bob
# Bob tưởng đó là của Alice
# Bước 3: Bob gửi B = g^b
# Max chặn lại
# Bước 4: Max gửi B' = g^m2 cho Alice
# Từ đó Max và Alice có chung khóa bí mật là k1, Max và Bob có chung khóa bí mật là k2
# Nghĩa là Max có thể giao tiếp giữa Alice và Bob  




#Lưu ý thực hiện chat với server bằng câu lệnh r.printline() để hiểu server nói gì
# iv và encrypted_flag là động (nghĩa là giá trị thay đổi sau mỗi lần chạy server) 
#vì vậy cần viết code trực tiếp để bắt thông tin (chứ không phải là copy-paste giá trị đọc được ở 1 lần chat với server)





























