from Crypto.Cipher import AES
import hashlib
import requests

# 1. Lấy ciphertext từ CryptoHack
url = 'http://aes.cryptohack.org/passwords_as_keys/'
try:
    r = requests.get(f'{url}encrypt_flag/')
    first_request = r.json()
    ciphertext_hex = first_request['ciphertext']
    ciphertext = bytes.fromhex(ciphertext_hex)
except Exception as e:
    print(f"Lỗi khi kết nối API: {e}")
    exit()

# 2. Tải danh sách từ khóa từ GitHub Gist
print("Đang tải wordlist...")
link = "https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words"
wordlist_response = requests.get(link)
words = wordlist_response.text.splitlines() # Tách các dòng thành mảng
print(f"Đã tải xong {len(words)} từ. Đang giải mã...")

# 3. Bruteforce tìm key
for w in words:
    # Key là mã MD5 hash của từ (dạng bytes)
    key = hashlib.md5(w.encode()).digest()
    
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    
    # Kiểm tra nếu flag bắt đầu bằng 'crypto{'
    if b'crypto{' in decrypted:
        print(f"--- THÀNH CÔNG ---")
        print(f"Password tìm thấy: {w}")
        print(f"Flag: {decrypted.decode()}")
        break



"""
D:\Vscode>python -u "d:\Vscode\Python_\Symmetric Cryptography.py\nhap.py"
Đang tải wordlist...
Đã tải xong 99171 từ. Đang giải mã...
--- THÀNH CÔNG ---
Password tìm thấy: bluebell
Flag: crypto{k3y5__r__n07__p455w0rdz?}
"""

