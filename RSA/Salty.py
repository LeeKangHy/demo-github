# /usr/bin/env python3

from Crypto.Util.number import long_to_bytes

# Tham số đề bài cung cấp
# N (modulus) - không cần thiết cho việc giải mã này
# n = 110581795715958566206600392161360212579669637391437097703685154237017351570464767725324182051199901920318211290404777259728923614917211291562555864753005179326101890427669819834642007924406862482343614488768256951616086287044725034412802176312273081322195866046098595306261781788276570920467840172004530873767

# e (public exponent) = 1 (Lỗ hổng: C = P^1 mod N => C = P)
# e = 1

# ct (ciphertext)
ct = 44981230718212183604274785925793145442655465025264554046028251311164494127485

# --- Giải quyết vấn đề ---
# Vì e=1, nên Plaintext (pt) = Ciphertext (ct)
pt = ct

# Chuyển đổi số nguyên pt trở lại thành chuỗi bytes (flag)
decrypted_flag = long_to_bytes(pt)


print(f"Giá trị Plaintext (số nguyên): {pt}")
print(f"Flag đã giải mã: {decrypted_flag.decode('utf-8')}")