import socket
import json
import base64
from collections import Counter

HOST = "socket.cryptohack.org"
PORT = 13370

def get_ciphertext():
    s = socket.socket()
    s.connect((HOST, PORT))
    s.recv(1024)  # "No leaks\n"

    s.send(b'{"msg": "request"}\n')
    resp = s.recv(1024).decode()
    s.close()

    data = json.loads(resp)
    if "error" in data:
        return None
    return base64.b64decode(data["ciphertext"])

# Thu thập 2000 ciphertext (càng nhiều càng tốt, 1500+ là đủ)
print("Collecting ciphertexts...")
ciphertexts = []
while len(ciphertexts) < 2000:
    ct = get_ciphertext()
    if ct and len(ct) == 20:
        ciphertexts.append(ct)
    print(f"\rCollected: {len(ciphertexts)}", end="")

print("\n\nCracking flag...")
flag = ""
printable = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_?!@#-$%&"

for pos in range(20):
    count_zero = Counter()
    
    for ct in ciphertexts:
        for c in printable:
            otp_byte = ct[pos] ^ ord(c)
            if otp_byte == 0:
                count_zero[c] += 1

    # Tìm ký tự mà số lần otp_byte == 0 là ÍT NHẤT (gần bằng 0)
    best_char = min(printable, key=lambda c: count_zero[c])
    best_count = count_zero[best_char]
    
    flag += best_char
    print(f"Position {pos}: '{best_char}' (zero count: {best_count})")

print("\nFlag:", flag)


"""
OUTPUT:
Collecting ciphertexts...
Collected: 2000

Cracking flag...
Position 0: 'c' (zero count: 0)
Position 1: 'r' (zero count: 0)
Position 2: 'y' (zero count: 0)
Position 3: 'p' (zero count: 0)
Position 4: 't' (zero count: 0)
Position 5: 'o' (zero count: 0)
Position 6: '{' (zero count: 0)
Position 7: 'u' (zero count: 0)
Position 8: 'n' (zero count: 0)
Position 9: 'r' (zero count: 0)
Position 10: '4' (zero count: 0)
Position 11: 'n' (zero count: 0)
Position 12: 'd' (zero count: 0)
Position 13: '0' (zero count: 0)
Position 14: 'm' (zero count: 0)
Position 15: '_' (zero count: 0)
Position 16: '0' (zero count: 0)
Position 17: '7' (zero count: 0)
Position 18: 'p' (zero count: 0)
Position 19: '}' (zero count: 0)

Flag: crypto{unr4nd0m_07p}
"""