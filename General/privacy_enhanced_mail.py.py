# extract_d_windows.py
from Crypto.PublicKey import RSA
from pathlib import Path
# Đảm bảo đường dẫn này trỏ đến một file Private Key RSA
pem_path = Path(r"D:\Crypto\Privacy-Enhanced Mail\privacy_enhanced_mail.pem")
f = open(pem_path,'r')
key = RSA.importKey(f.read())

print(key.d)





"""
#FLAG :
156827002880563313647871710458199736549911499491979599298608612281800217073168519244562055436655658
1089267419005983133023143697091447477456271494562051914438978515890899418195134884601743250646416356
4960993784254153395406799101314760033445065193429592512349952020982932218524462341002102063435489318
8133164645116217369439384407104706949123362376802197462045951289591618005952163662375382964473353758188
7195252002699310214832889708354718428649324119150595360166885894112979096690923694112785137020242113589709
1086763569884760099112291072056970636380417349019579768748054760104838790424708988260443926906673795975104689
"""









""" 
# cách của chatgpt : đầy đủ nhưng tôi chưa hiểu hết được
import sys
from pathlib import Path
from Crypto.PublicKey import RSA
import getpass

def main():
    # <- chỉnh đường dẫn file PEM ở đây nếu cần
    pem_path = Path(r"D:\Crypto\Privacy-Enhanced Mail\privacy_enhanced_mail.pem")

    if not pem_path.exists():
        print(f"File not found: {pem_path}", file=sys.stderr)
        sys.exit(2)

    data = pem_path.read_bytes()

    # Thử import không passphrase trước
    try:
        key = RSA.import_key(data)
    except ValueError as e:
        # Có thể PEM được mã hóa — hỏi passphrase
        try:
            pw = getpass.getpass("PEM appears encrypted. Enter passphrase (will be hidden): ")
        except Exception:
            pw = None
        if not pw:
            print("Failed to import key and no passphrase provided.", file=sys.stderr)
            sys.exit(3)
        try:
            key = RSA.import_key(data, passphrase=pw)
        except Exception as e2:
            print("Failed to import key with provided passphrase:", e2, file=sys.stderr)
            sys.exit(4)

    # Kiểm tra có d không
    d = getattr(key, "d", None)
    if d is None:
        print("This PEM does not contain a private exponent 'd' (may be a public key or certificate).", file=sys.stderr)
        sys.exit(5)

    # In CHỈ giá trị d (decimal) — phù hợp cho challenge
    print(d)

if __name__ == "__main__":
    main()
"""