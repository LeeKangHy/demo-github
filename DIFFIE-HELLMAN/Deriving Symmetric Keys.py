from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message :bytes):   
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()                                 #tạo một đối tượng sha1 mới đang ở trạng thái rỗng
    sha1.update(str(shared_secret).encode('ascii'))       # shared_secret định dạng int -> string -> byte
    key = sha1.digest()[:16]                              #lấy 16 byte đầu làm khóa AES
    # Decrypt flag  
    ciphertext = bytes.fromhex(ciphertext)                #ciphertext của hàm encrypt ở định dạng hex -> byte
    iv = bytes.fromhex(iv)                                #iv của hàm encrypt ở định dạng hex -> byte
    cipher = AES.new(key, AES.MODE_CBC, iv)               #Tạo đối tượng mã hóa AES chế độ CBC
    plaintext = cipher.decrypt(ciphertext)                #giải mã ciphertext

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')       #unpad(plaintext, 16) : hàm bỏ padding (đệm) đã được thêm trước khi mã hóa, cụ thể là bỏ "PKCS#7 padding" để lấy lại plaintext gốc.
    else:
        return plaintext.decode('ascii')                                     


A= 112218739139542908880564359534373424013016249772931962692237907571990334483528877513809272625610512061159061737608547288558662879685086684299624481742865016924065000555267977830144740364467977206555914781236397216033805882207640219686011643468275165718132888489024688846101943642459655423609111976363316080620471928236879737944217503462265615774774318986375878440978819238346077908864116156831874695817477772477121232820827728424890845769152726027520772901423784
b= 197395083814907028991785772714920885908249341925650951555219049411298436217190605190824934787336279228785809783531814507661385111220639329358048196339626065676869119737979175531770768861808581110311903548567424039264485661330995221907803300824165469977099494284722831845653985392791480264712091293580274947132480402319812110462641143884577706335859190668240694680261160210609506891842793868297672619625924001403035676872189455767944077542198064499486164431451944
p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919

shared_secret = pow(A,b,p)

iv = '737561146ff8194f45290f5766ed6aba'
ciphertext = '39c99bf2f0c14678d6a5416faef954b5893c316fc3c48622ba1fd6a9fe85f3dc72a29c394cf4bc8aff6a7b21cae8e12c'

print(decrypt_flag(shared_secret, iv, ciphertext))




"""HỌC LÝ THUYẾT VỀ PADDING, cụ thể là hiểu hàm is_pkcs7_padded()"""

# Mục đích của hàm
# 👉 Kiểm tra xem message (bytes) có padding PKCS#7 hợp lệ hay không.
# 1️⃣ Tham số message: bytes
# def is_pkcs7_padded(message: bytes):


# message là bytes

# Thường là:

# plaintext sau khi decrypt

# chưa unpad

# Ví dụ:

# b"HELLO\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b"

# 2️⃣ Dòng quan trọng nhất: lấy padding
# padding = message[-message[-1]:]


# Phân tích từ trong ra ngoài 👇

# 🔹 message[-1]

# Lấy byte cuối cùng của message

# Vì message là bytes → kết quả là số nguyên (0–255)

# Ví dụ:

# message[-1] = 11


# Theo PKCS#7:

# Byte cuối cùng = số byte padding

# 🔹 message[-message[-1]:]

# Nghĩa là:

# message[-11:]


# Lấy 11 byte cuối của message

# Ví dụ:

# padding = b'\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b'


# 👉 Dòng này tách riêng phần padding ở cuối message

# 3️⃣ Kiểm tra padding có hợp lệ không
# return all(padding[i] == len(padding) for i in range(0, len(padding)))


# Chia nhỏ ra:

# 🔹 len(padding)

# Số byte padding

# Ví dụ: len(padding) = 11

# 🔹 padding[i] == len(padding)

# Kiểm tra:

# Mỗi byte padding có giá trị đúng bằng độ dài padding không?

# Ví dụ đúng:

# [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11]


# Ví dụ sai:

# [11, 11, 11, 10, 11]

# 🔹 for i in range(0, len(padding))

# Duyệt từng byte trong padding

# 🔹 all(...)

# Trả về:

# True → tất cả byte đúng

# False → chỉ cần 1 byte sai

# 4️⃣ Hàm này KHẲNG ĐỊNH điều gì?

# Hàm trả về True nếu và chỉ nếu:

# Byte cuối cùng là k

# Có đúng k byte padding ở cuối

# Mỗi byte padding đều có giá trị k

# ➡️ Đúng chuẩn PKCS#7

# 5️⃣ Ví dụ chạy thật
# ✅ Padding hợp lệ
# msg = b"ABC\x03\x03\x03"
# is_pkcs7_padded(msg)
# # True

# ❌ Padding không hợp lệ
# msg = b"ABC\x03\x03\x02"
# is_pkcs7_padded(msg)
# # False

# 6️⃣ ⚠️ Lưu ý quan trọng (rất hay ra CTF)

# Hàm này CHƯA đủ an toàn, vì nó không kiểm tra:

# message[-1] == 0

# message[-1] > block_size

# message rỗng

# 👉 Chính kiểu kiểm tra đơn giản này thường tạo ra padding oracle attack.

# 7️⃣ Tóm tắt 1 câu (đúng bản chất)

# is_pkcs7_padded()
# → đọc byte cuối
# → coi đó là độ dài padding
# → kiểm tra tất cả byte padding có đúng giá trị đó hay không.




"""Cách python đánh chỉ số"""
# Trong Python, index âm đếm từ cuối về đầu.
# Ví dụ đơn giản:

# a = [10, 20, 30, 40]
# a[-1]   # 40
# a[-2]   # 30