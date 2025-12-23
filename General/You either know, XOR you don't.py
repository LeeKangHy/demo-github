# Dữ liệu mã hoá dạng hex
cipher_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

# Chuyển từ hex sang bytes
cipher = bytes.fromhex(cipher_hex)

# Khóa XOR
key = b"myXORkey"

# # Giải mã XOR (lặp khóa cho đủ độ dài ciphertext)
# flag = bytes([c ^ key[i % len(key)] for i, c in enumerate(cipher)])

# # In kết quả
# print(flag.decode())



flag = [0] * len(cipher_hex)

for i in range (0,len(cipher)):
    flag[i] = cipher[i] ^ key[i%len(key)]
   

result = ""
for i in range(0,len(cipher)):
  result += chr(flag[i])

print(result)




