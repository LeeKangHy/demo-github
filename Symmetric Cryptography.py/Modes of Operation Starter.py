import requests 
BASE_URL = "http://aes.cryptohack.org/block_cipher_starter"

r = requests.get(f"{BASE_URL}/encrypt_flag")
data = r.json()
#print(data)
 #{'ciphertext': 'c11949a4a2ecf929dfce48b39daedd9e6d90c67d2f550b79259bdda835348a48'}
ciphertext = data["ciphertext"]

r = requests.get(f"{BASE_URL}/decrypt/{ciphertext}")
data = r.json()
#print(data)
 #{'plaintext': '63727970746f7b626c30636b5f633170683372355f3472335f663435375f217d'}
plaintext = data["plaintext"]

flag = bytes.fromhex(plaintext)

print(flag)




"""SOURCE CODE FROM URL"""
# from Crypto.Cipher import AES


# KEY = ?
# FLAG = ?


# @chal.route('/block_cipher_starter/decrypt/<ciphertext>/')
# def decrypt(ciphertext):
#     ciphertext = bytes.fromhex(ciphertext)

#     cipher = AES.new(KEY, AES.MODE_ECB)
#     try:
#         decrypted = cipher.decrypt(ciphertext)
#     except ValueError as e:
#         return {"error": str(e)}

#     return {"plaintext": decrypted.hex()}


# @chal.route('/block_cipher_starter/encrypt_flag/')
# def encrypt_flag():
#     cipher = AES.new(KEY, AES.MODE_ECB)
#     encrypted = cipher.encrypt(FLAG.encode())

#     return {"ciphertext": encrypted.hex()}

"""
Bài này dạy ta cách giao tiếp qua url bằng Python
Từ source code thấy được rằng chỉ cần gọi cú pháp để lấy dữ liệu từ server sau đó giải mã hex string 
"""



""" HỌC CÚ PHÁP  """

# 1️⃣ f" " là gì?

# 👉 f" " gọi là f-string (formatted string literal).

# 📌 Nói đơn giản:

# f-string = chuỗi cho phép nhét biến vào bên trong

# 2️⃣ Ví dụ cơ bản nhất
# name = "Huy"
# age = 20

# print(f"Tôi tên là {name}, {age} tuổi")


# 📤 Kết quả:

# Tôi tên là Huy, 20 tuổi


# 📌 {name} và {age} được thay bằng giá trị biến.






# Lý thuyết:

# Client ----GET----> Server
# Client <---JSON---- Server







# 1️⃣ Toàn bộ dòng lệnh
# ciphertext = data["ciphertext"]


# 👉 Dòng này gồm 3 phần:

# [ciphertext] = [data]["ciphertext"]

# 2️⃣ data là cái gì?

# Trước đó bạn có dòng:

# data = r.json()


# Server trả về JSON như sau:

# {
#   "ciphertext": "a1b2c3d4..."
# }


# 👉 Khi vào Python, nó trở thành dictionary (dict):

# data = {
#   "ciphertext": "a1b2c3d4..."
# }

# 3️⃣ Dictionary (dict) là gì?

# 👉 dict = bảng ánh xạ key → value

# Ví dụ:

# person = {
#   "name": "Huy",
#   "age": 20
# }

# Key	Value
# "name"	"Huy"
# "age"	20
# 4️⃣ data["ciphertext"] nghĩa là gì?

# 👉 Lấy giá trị tương ứng với key "ciphertext"

# data["ciphertext"]


# = "a1b2c3d4..."

# 📌 Đây gọi là truy cập phần tử trong dictionary

# 5️⃣ Gán vào biến ciphertext
# ciphertext = data["ciphertext"]


# 👉 Nghĩa là:

# Lấy giá trị "a1b2c3d4..."
# Gán nó vào biến ciphertext

# 6️⃣ Viết lại bằng lời người thường

# “Từ dữ liệu server gửi về (data),
# lấy phần có tên là "ciphertext",
# rồi lưu nó vào biến ciphertext.”

# 7️⃣ Ví dụ đơn giản hơn (ngoài CTF)
# data = {
#   "food": "pho",
#   "price": 30000
# }

# x = data["food"]
# print(x)


# 📤 Kết quả:

# pho

# 8️⃣ Nếu key không tồn tại thì sao?
# data["abc"]


# ❌ Python báo lỗi:

# KeyError: 'abc'


# 👉 Vì vậy phải đúng tên key server trả