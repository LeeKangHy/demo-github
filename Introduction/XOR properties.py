KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_xor_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_xor_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_xor_KEY1_xor_KEY3_xor_KEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"



b1 = bytes.fromhex(KEY1)
b2 = bytes.fromhex(KEY2_xor_KEY1)
b3 = bytes.fromhex(KEY2_xor_KEY3)
b4 = bytes.fromhex(FLAG_xor_KEY1_xor_KEY3_xor_KEY2)


KEY2 = [0] * len(b1)
for i in range(0,len(b1)):
    KEY2[i] = b1[i] ^ b2[i] 
    print(KEY2[i],end= "")

print("\n") 
KEY3 = [0] * len(b1)
for i in range(len(b1)): 
    KEY3[i] = b3[i] ^ KEY2[i]
    print(KEY3[i], end= "")

print("\n") 

FLAG = [0] *len(b1)

for i in range(len(b1)):
    FLAG[i] = b4[i]^b1[i]^KEY2[i]^KEY3[i]
    print(FLAG[i],end = "")



print("\n") 
flag = ""
for i in range(len(b1)): 
    flag += chr(FLAG[i]) 

print(flag) 




"""
CÁCH của CHATGPT 
KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_xor_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_xor_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_xor_KEY1_xor_KEY3_xor_KEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

b1 = bytes.fromhex(KEY1)
b2 = bytes.fromhex(KEY2_xor_KEY1)
b3 = bytes.fromhex(KEY2_xor_KEY3)
b4 = bytes.fromhex(FLAG_xor_KEY1_xor_KEY3_xor_KEY2)

# KEY2 = KEY1 XOR (KEY2_xor_KEY1)
KEY2 = bytes([b1[i] ^ b2[i] for i in range(len(b1))])          # chú thích cú pháp bytes(...) bên dưới

# KEY3 = KEY2 XOR (KEY2_xor_KEY3)
KEY3 = bytes([b3[i] ^ KEY2[i] for i in range(len(b1))])

# FLAG = XOR của tất cả
FLAG = bytes([b4[i] ^ b1[i] ^ KEY2[i] ^ KEY3[i] for i in range(len(b1))])

print("KEY2 =", KEY2.hex())
print("KEY3 =", KEY3.hex())
print("FLAG =", FLAG.decode())



# [b1[i] ^ b2[i] for i in range(len(b1))]

# Đây là list comprehension, tạo ra một list các số nguyên byte:

# Ví dụ:

# [12, 244, 81, 3, 99, ...]


# Mỗi phần tử là 1 byte (giá trị 0–255).

#  bytes([...])

# Hàm bytes() nhận một list các số nguyên và biến nó thành 1 chuỗi bytes bất biến.

# Ví dụ:

# bytes([97, 98, 99])  →  b'abc'

"""