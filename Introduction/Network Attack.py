

from pwn import * # pip install pwntools
import json

HOST = "socket.cryptohack.org"
PORT = 11112

r = remote(HOST, PORT)


def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


print(r.readline().decode())
print(r.readline().decode())
print(r.readline().decode())
print(r.readline().decode())


request = {
    "buy": "flag"
}
json_send(request)

response = json_recv()

print(response)


""" HỌC CÚ PHÁP """

# Mình giải thích rất rõ và ngắn gọn, đúng theo ý nghĩa Python:

# ✔ json.loads(line.decode()) là gì?
# 1️⃣ line.decode()

# line là bytes (ví dụ: b'{"msg":"hello"}\n').

# .decode() biến bytes → string theo UTF-8.

# Ví dụ:

# b'{"msg":"hello"}'.decode()


# kết quả:

# '{"msg":"hello"}'   # dạng string

# 2️⃣ json.loads(...)

# json.loads() đọc chuỗi JSON và biến thành dict Python.

# Ví dụ:

# json.loads('{"msg":"hello"}')


# →

# {"msg": "hello"}   # dict Python

# 👉 Gộp lại
# json.loads(line.decode())


# Nghĩa là:

# bytes JSON → string → dict Python

# ✔ json.dumps(hsh).encode() là gì?
# 1️⃣ json.dumps(hsh)

# Chuyển dict Python → chuỗi JSON.

# Ví dụ:

# json.dumps({"option": "hello"})


# →

# '{"option": "hello"}'   # string

# 2️⃣ .encode()

# Chuyển chuỗi JSON string → bytes, để gửi qua socket.

# Ví dụ:

# '{"option":"hello"}'.encode()


# →

# b'{"option":"hello"}'

# 👉 Gộp lại
# json.dumps(hsh).encode()


# Nghĩa là:

# dict Python → JSON string → bytes (để gửi qua mạng)

# 🎯 Tóm tắt cực ngắn
# Code	Ý nghĩa
# json.loads(line.decode())	bytes → string → dict
# json.dumps(hsh).encode()	dict → string JSON → bytes


