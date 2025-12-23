"""
# cách của chatgpt
key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
encode2 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
encode3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
encode4 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

# key2 = key1 ^ encode2
key2 = bytes([key1[i] ^ encode2[i] for i in range(len(encode2))])

# key3 = key2 ^ encode3
key3 = bytes([key2[i] ^ encode3[i] for i in range(len(encode3))])

# flag = encode4 ^ key1 ^ key2 ^ key3
flag = bytes([encode4[i] ^ key1[i] ^ key2[i] ^ key3[i] for i in range(len(encode4))])

print(flag.decode())
"""

# cách theo vốn hiểu biết của tôi
key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
encode2 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
encode3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
encode4 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

key2 = []
for i in range(len(encode2)) :
       key2.append(key1[i]^encode2[i])

key3 = []
for i in range(len(encode3)):
       key3.append(key2[i]^encode3[i])
flag = []
for i in range(len(encode4)):
       flag.append(encode4[i]^key1[i]^key2[i]^key3[i])
for i in range(len(flag)):
       print(chr(flag[i]),end="")