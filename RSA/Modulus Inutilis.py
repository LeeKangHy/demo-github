#/usr/bin/env python3

from Crypto.Util.number import long_to_bytes

# --- Tham số đầu vào ---
# Modulus N (không cần thiết cho tấn công này, nhưng được cung cấp để tham khảo)
# n = 17258212916191948536348548470938004244269544560039009244721959293554822498047075403658429865201816363311805874117705688359853941515579440852166618074161313773416434156467811969628473425365608002907061241714688204565170146117869742910273064909154666642642308154422770994836108669814632309362483307560217924183202838588431342622551598499747369771295105890359290073146330677383341121242366368309126850094371525078749496850520075015636716490087482193603562501577348571256210991732071282478547626856068209192987351212490642903450263288650415552403935705444809043563866466823492258216747445926536608548665086042098252335883
# e = 3

# Ciphertext C (ct)
ct = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957

# --- Thuật toán tìm căn bậc ba nguyên (Integer Nth Root) ---
def integer_nth_root(n, k):
    """Tính căn bậc k nguyên của n, floor(n^(1/k))"""
    if n < 0:
        raise ValueError("Cannot compute real root of negative number")
    if n == 0:
        return 0
    
    # Sử dụng phương pháp Newton's method (hoặc binary search) để tìm căn
    # Ước tính ban đầu
    x = int(n ** (1/k))
    # Tinh chỉnh bằng thuật toán tìm căn (Binary Search cho căn bậc n)
    low = 1
    high = n
    root = 1

    while low <= high:
        mid = (low + high) // 2
        try:
            # Kiểm tra tránh tràn số (overflow) nếu mid quá lớn, nhưng với Python thì không cần lo lắng
            power = mid ** k
        except OverflowError:
            power = float('inf') 

        if power == n:
            return mid
        elif power < n:
            root = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return root


# --- Tiến hành giải mã ---

e_value = 3
pt_int = integer_nth_root(ct, e_value)

# 1. Kiểm tra xác nhận: (P^3 = C)
if pt_int ** e_value == ct:
    print(f"Xác nhận: {pt_int} ^ {e_value} = {ct} (C = P^e)")
    
    # 2. Chuyển đổi số nguyên pt_int thành bytes (flag)
    decrypted_flag = long_to_bytes(pt_int)

    print("-" * 50)
    print(f"Giá trị Plaintext (số nguyên): {pt_int}")
    print(f"Flag đã giải mã: {decrypted_flag.decode('utf-8', errors='ignore')}")
else:
    print("Lỗi: Không thể tính căn bậc 3 chính xác. Điều kiện C = P^e có lẽ không được thỏa mãn.")


"""
OUTPUT : 
Xác nhận: 624239975241694158443315202759206900318542905782320965248893 ^ 3 = 243251053617903760309941844835411292373350655973075480264001352919865180151222189820473358411037759381328642957324889519192337152355302808400638052620580409813222660643570085177957 (C = P^e)
--------------------------------------------------
Giá trị Plaintext (số nguyên): 624239975241694158443315202759206900318542905782320965248893
Flag đã giải mã: crypto{N33d_m04R_p4dd1ng}

"""