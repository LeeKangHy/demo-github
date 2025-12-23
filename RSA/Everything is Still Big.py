#/usr/bin/env python3

from Crypto.Util.number import long_to_bytes, inverse
import math

# --- 1. Tham số đầu vào (Chuyển từ hex sang số nguyên) ---
N = 0xb12746657c720a434861e9a4828b3c89a6b8d4a1bd921054e48d47124dbcc9cfcdcc39261c5e93817c167db818081613f57729e0039875c72a5ae1f0bc5ef7c933880c2ad528adbc9b1430003a491e460917b34c4590977df47772fab1ee0ab251f94065ab3004893fe1b2958008848b0124f22c4e75f60ed3889fb62e5ef4dcc247a3d6e23072641e62566cd96ee8114b227b8f498f9a578fc6f687d07acdbb523b6029c5bbeecd5efaf4c4d35304e5e6b5b95db0e89299529eb953f52ca3247d4cd03a15939e7d638b168fd00a1cb5b0cc5c2cc98175c1ad0b959c2ab2f17f917c0ccee8c3fe589b4cb441e817f75e575fc96a4fe7bfea897f57692b050d2b
e = 0x9d0637faa46281b533e83cc37e1cf5626bd33f712cc1948622f10ec26f766fb37b9cd6c7a6e4b2c03bce0dd70d5a3a28b6b0c941d8792bc6a870568790ebcd30f40277af59e0fd3141e272c48f8e33592965997c7d93006c27bf3a2b8fb71831dfa939c0ba2c7569dd1b660efc6c8966e674fbe6e051811d92a802c789d895f356ceec9722d5a7b617d21b8aa42dd6a45de721953939a5a81b8dffc9490acd4f60b0c0475883ff7e2ab50b39b2deeedaefefffc52ae2e03f72756d9b4f7b6bd85b1a6764b31312bc375a2298b78b0263d492205d2a5aa7a227abaf41ab4ea8ce0e75728a5177fe90ace36fdc5dba53317bbf90e60a6f2311bb333bf55ba3245f
c = 0xa3bce6e2e677d7855a1a7819eb1879779d1e1eefa21a1a6e205c8b46fdc020a2487fdd07dbae99274204fadda2ba69af73627bdddcb2c403118f507bca03cb0bad7a8cd03f70defc31fa904d71230aab98a10e155bf207da1b1cac1503f48cab3758024cc6e62afe99767e9e4c151b75f60d8f7989c152fdf4ff4b95ceed9a7065f38c68dee4dd0da503650d3246d463f504b36e1d6fafabb35d2390ecf0419b2bb67c4c647fb38511b34eb494d9289c872203fa70f4084d2fa2367a63a8881b74cc38730ad7584328de6a7d92e4ca18098a15119baee91237cea24975bdfc19bdbce7c1559899a88125935584cd37c8dd31f3f2b4517eefae84e7e588344fa5

# --- 2. Hàm tính Ước xấp xỉ liên tục (Continued Fractions) ---
def continued_fraction(numerator, denominator):
    """Tính toán và trả về các ước xấp xỉ (k/d) của phân số (numerator/denominator)"""
    # Lấy các hệ số của phân số liên tục [a0; a1, a2, ...]
    a = []
    while denominator:
        a.append(numerator // denominator)
        numerator, denominator = denominator, numerator % denominator
    
    # Tính các ước xấp xỉ (convergents) p_i / q_i
    convergents = []
    p_prev, p_curr = 0, 1
    q_prev, q_curr = 1, 0
    
    for coeff in a:
        p_next = coeff * p_curr + p_prev
        q_next = coeff * q_curr + q_prev
        
        # Chỉ quan tâm đến d nhỏ (q_next)
        if q_next.bit_length() > 512 + 10:  # Giới hạn tìm kiếm ở kích thước d ~ 512 bit
             break
        
        convergents.append((p_next, q_next)) # (k, d_guess)
        p_prev, p_curr = p_curr, p_next
        q_prev, q_curr = q_curr, q_next
        
    return convergents

# --- 3. Hàm kiểm tra khóa bí mật d ---
def check_d(e, N):
    """
    Tìm khóa bí mật d bằng cách kiểm tra các ước xấp xỉ liên tục.
    Wiener/Boneh-Durfee dựa trên việc tìm d nhỏ.
    """
    
    # Tìm kiếm trong các ước xấp xỉ của e/N
    for k_guess, d_guess in continued_fraction(e, N):
        if k_guess == 0 or d_guess == 0: continue
        
        # 1. Tính phi(N) giả định: phi = (e * d - 1) / k
        # Phải đảm bảo (e * d_guess - 1) chia hết cho k_guess
        if (e * d_guess - 1) % k_guess == 0:
            phi_guess = (e * d_guess - 1) // k_guess
            
            # 2. Tính p + q
            # p + q = N - phi(N) + 1
            sum_pq = N - phi_guess + 1
            
            # 3. Tính Delta (biệt thức) của phương trình bậc 2: x^2 - (p+q)x + N = 0
            # Delta = (p + q)^2 - 4 * N
            delta = sum_pq * sum_pq - 4 * N
            
            if delta > 0:
                # 4. Kiểm tra xem Delta có phải là số chính phương không
                try:
                    root_delta = math.isqrt(delta) 
                except AttributeError:
                    # Fallback cho các phiên bản Python cũ hơn
                    root_delta = int(math.sqrt(delta))

                # Nếu delta là số chính phương, chúng ta tìm được p và q nguyên
                if root_delta * root_delta == delta:
                    # p, q phải là số nguyên
                    if (sum_pq + root_delta) % 2 == 0:
                        p = (sum_pq + root_delta) // 2
                        q = (sum_pq - root_delta) // 2
                    else:
                        continue # Bỏ qua nếu p, q không nguyên

                    # 5. Xác nhận p * q = N và p, q là hai số nguyên tố (hoặc ít nhất là nguyên)
                    if p * q == N and p != q and p > 1 and q > 1:
                        # Kiểm tra thêm điều kiện d phải là nghịch đảo của e mod phi
                        if (e * d_guess) % phi_guess == 1:
                            print(f"--- THÀNH CÔNG ---")
                            print(f"Tìm thấy khóa bí mật d: {d_guess}")
                            print(f"d có {d_guess.bit_length()} bit.")
                            print(f"p: {p.bit_length()} bit, q: {q.bit_length()} bit.")
                            return d_guess
                        
    return None

# --- Thực hiện giải mã ---

print("Bắt đầu tìm kiếm khóa bí mật d (dựa trên Wiener/Boneh-Durfee Attack cho d nhỏ)...")

d_found = check_d(e, N) # e/N

if d_found:
    # Bước 2: Giải mã
    d = d_found
    m = pow(c, d, N)
    
    # Bước 3: Chuyển đổi sang Flag
    flag = long_to_bytes(m)
    
    print("-" * 50)
    print(f"Giá trị Plaintext (số nguyên): {m}")
    print(f"Flag đã giải mã: {flag.decode('utf-8')}")
else:
    print("LỖI: Không tìm thấy khóa bí mật d phù hợp bằng phương pháp Continued Fractions.")
    print("Do d có kích thước 512 bit, phương pháp này đôi khi không hiệu quả và cần sử dụng Lattices (Boneh-Durfee Attack).")

"""
OUTPUT :
Bắt đầu tìm kiếm khóa bí mật d (dựa trên Wiener/Boneh-Durfee Attack cho d nhỏ)...
--- THÀNH CÔNG ---
Tìm thấy khóa bí mật d: 4405001203086303853525638270840706181413309101774712363141310824943602913458674670435988275467396881342752245170076677567586495166847569659096584522419007
d có 511 bit.
p: 1024 bit, q: 1024 bit.
--------------------------------------------------
Giá trị Plaintext (số nguyên): 912327745903138315261363718252626615681701561492303083405804674195730203057913811964908292881307584531936637
Flag đã giải mã: crypto{bon3h5_4tt4ck_i5_sr0ng3r_th4n_w13n3r5}

"""