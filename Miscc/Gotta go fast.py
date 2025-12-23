#/usr/bin/env python3
import json
import socket
import threading
import time
from Crypto.Util.Padding import pad

HOST = "socket.cryptohack.org"
PORT = 13372

# Chuỗi mình sẽ gửi để lấy key (có thể là bất kỳ cái gì, miễn biết trước)
MY_DATA = b"0" * 32  # 32 byte để lấy full key


def send_get_flag(result):
    s = socket.socket()
    s.connect((HOST, PORT))
    s.recv(4096)  # "Gotta go fast!\n"

    req = json.dumps({"option": "get_flag"}).encode() + b"\n"
    s.send(req)
    resp = s.recv(4096).decode()
    s.close()
    result["flag"] = json.loads(resp)


def send_encrypt_data(result):
    s = socket.socket()
    s.connect((HOST, PORT))
    s.recv(4096)

    req = json.dumps({
        "option": "encrypt_data",
        "input_data": MY_DATA.hex()
    }).encode() + b"\n"
    s.send(req)
    resp = s.recv(4096).decode()
    s.close()
    result["mine"] = json.loads(resp)


result = {}
t1 = threading.Thread(target=send_get_flag, args=(result,))
t2 = threading.Thread(target=send_encrypt_data, args=(result,))

print("[*] Sending 2 requests at the same time...")
t1.start()
t2.start()
t1.join()
t2.join()

enc_flag = bytes.fromhex(result["flag"]["encrypted_flag"])
enc_mine = bytes.fromhex(result["mine"]["encrypted_data"])

# Key = MY_DATA XOR enc_mine
key = bytes(a ^ b for a, b in zip(MY_DATA, enc_mine))

# Flag = enc_flag XOR key
flag = bytes(a ^ b for a, b in zip(enc_flag, key))
print("[+] Flag:", flag.decode())


"""
OUTPUT:
[*] Sending 2 requests at the same time...
[+] Flag: crypto{t00_f4st_t00_furi0u5}
"""