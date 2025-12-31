from Crypto.Cipher import AES
import hashlib
import requests

# 1. Lấy ciphertext từ CryptoHack
url = 'http://aes.cryptohack.org/passwords_as_keys/'
r = requests.get(f'{url}encrypt_flag/')
data = r.json()
#print(data)
 #{'ciphertext': 'c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66'
ciphertext_hex = data['ciphertext']
ciphertext = bytes.fromhex(ciphertext_hex)


# 2. Tải danh sách từ khóa từ GitHub Gist
link = "https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words"
wordlist_response = requests.get(link) 
#print(wordlist_response)  
 #<Response [200]>  # đây chỉ là đoạn output để xác định việc tải về thành công thôi
 #(not relevant)  #print(wordlist_response.text[:50]) # xem 50 ký tự (char) đầu tiên trong file đã tải về
words = wordlist_response.text.splitlines() # Tách các dòng thành mảng


#3.Brute force tìm key


for w in words:
    # Key là mã MD5 hash của từ (dạng bytes)
    key = hashlib.md5(w.encode()).digest()              #sau khi băm, cần hàm digest() để lấy dữ liệu đã băm ra 
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    
    # Kiểm tra nếu flag bắt đầu bằng 'crypto{'
    if b'crypto{' in decrypted:
        print(w)
        print(f"Flag: {decrypted.decode()}")
        break


# bluebell
# Flag: crypto{k3y5__r__n07__p455w0rdz?}



























"""10 vạn câu hỏi vì sao"""


"""Tại sao lúc thì mã code sử dụng lệnh get() thì là truy cập đến server, lúc thì lệnh get() sẽ tải nội dung file về vậy ?"""
#Thực chất, về phía Python và thư viện requests, lệnh requests.get("...") luôn làm đúng một việc duy nhất: Gửi một yêu cầu (request) đến một địa chỉ URL và nhận về một phản hồi (response).
#Sự khác biệt mà bạn thấy (lúc thì là "truy cập server", lúc thì là "tải file") không nằm ở câu lệnh, mà nằm ở loại dữ liệu mà URL đó cung cấp.

"""Có cách nào để xem file mình tải về nó nằm ở đâu trên máy tính không"""
# File đó hiện tại không nằm ở bất kỳ đâu trên ổ cứng máy tính của bạn cả.

# Khi bạn dùng lệnh requests.get(), nội dung của file được tải về và lưu tạm thời vào RAM (Bộ nhớ đệm) dưới dạng một biến trong chương trình Python. Nếu bạn tắt chương trình đi, dữ liệu đó sẽ biến mất.

# Để "thấy" được nó hoặc lưu nó xuống máy tính, bạn có 2 cách sau:

# Cách 1: Lưu file xuống ổ cứng (Để mở bằng Notepad/Text Editor)
# Nếu bạn muốn file đó xuất hiện trong thư mục máy tính (ví dụ đặt tên là tudien.txt), bạn phải dùng thêm lệnh ghi file của Python:

# Python

# import requests

# link = "https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words"
# wordlist_response = requests.get(link)

# # Lưu nội dung vào một file tên là tudien.txt
# with open("tudien.txt", "w", encoding="utf-8") as f:
#     f.write(wordlist_response.text)

# print("Đã lưu file thành công! Bạn hãy kiểm tra thư mục chứa file code này.")
# Cách 2: Xem trực tiếp nội dung khi đang chạy code
# Nếu bạn chỉ muốn "ngó" qua xem nội dung bên trong có gì mà không cần lưu, bạn có thể in nó ra màn hình:

# Xem toàn bộ: print(wordlist_response.text) (Cẩn thận vì file này rất dài, có thể làm treo màn hình console).

# Xem 50 ký tự đầu tiên: ```python print(wordlist_response.text[:50])