#/usr/bin/env python3

from Crypto.Util.number import long_to_bytes
import math

# --- Tham số đề bài cung cấp (đã chuyển sang số nguyên) ---
N = 0xb8af3d3afb893a602de4afe2a29d7615075d1e570f8bad8ebbe9b5b9076594cf06b6e7b30905b6420e950043380ea746f0a14dae34469aa723e946e484a58bcd92d1039105871ffd63ffe64534b7d7f8d84b4a569723f7a833e6daf5e182d658655f739a4e37bd9f4a44aff6ca0255cda5313c3048f56eed5b21dc8d88bf5a8f8379eac83d8523e484fa6ae8dbcb239e65d3777829a6903d779cd2498b255fcf275e5f49471f35992435ee7cade98c8e82a8beb5ce1749349caa16759afc4e799edb12d299374d748a9e3c82e1cc983cdf9daec0a2739dadcc0982c1e7e492139cbff18c5d44529407edfd8e75743d2f51ce2b58573fea6fbd4fe25154b9964d
e = 0x9ab58dbc8049b574c361573955f08ea69f97ecf37400f9626d8f5ac55ca087165ce5e1f459ef6fa5f158cc8e75cb400a7473e89dd38922ead221b33bc33d6d716fb0e4e127b0fc18a197daf856a7062b49fba7a86e3a138956af04f481b7a7d481994aeebc2672e500f3f6d8c581268c2cfad4845158f79c2ef28f242f4fa8f6e573b8723a752d96169c9d885ada59cdeb6dbe932de86a019a7e8fc8aeb07748cfb272bd36d94fe83351252187c2e0bc58bb7a0a0af154b63397e6c68af4314601e29b07caed301b6831cf34caa579eb42a8c8bf69898d04b495174b5d7de0f20cf2b8fc55ed35c6ad157d3e7009f16d6b61786ee40583850e67af13e9d25be3
c = 0x3f984ff5244f1836ed69361f29905ca1ae6b3dcf249133c398d7762f5e277919174694293989144c9d25e940d2f66058b2289c75d1b8d0729f9a7c4564404a5fd4313675f85f31b47156068878e236c5635156b0fa21e24346c2041ae42423078577a1413f41375a4d49296ab17910ae214b45155c4570f95ca874ccae9fa80433a1ab453cbb28d780c2f1f4dc7071c93aff3924d76c5b4068a0371dff82531313f281a8acadaa2bd5078d3ddcefcb981f37ff9b8b14c7d9bf1accffe7857160982a2c7d9ee01d3e82265eec9c7401ecc7f02581fd0d912684f42d1b71df87a1ca51515aab4e58fab4da96e154ea6cdfb573a71d81b2ea4a080a1066e1bc3474

# --- 1. Hàm tính Ước xấp xỉ liên tục (Continued Fractions) ---
def continued_fraction(numerator, denominator):
    """Tính toán và trả về các ước xấp xỉ (k/d) của phân số (numerator/denominator)"""
    # Ứng dụng Euclidean Algorithm để tính các hệ số của phân số liên tục [a0; a1, a2, ...]
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
        convergents.append((p_next, q_next)) # (k, d_guess)
        p_prev, p_curr = p_curr, p_next
        q_prev, q_curr = q_curr, q_next
        
    return convergents

# --- 2. Hàm kiểm tra khóa bí mật d ---
def check_d(d_guess, e, N):
    """
    Kiểm tra xem d_guess có phải là d chính xác không.
    Dựa trên việc tìm p và q từ N và giả định phi(N).
    """
    
    # K là một số nguyên nhỏ, thường là 1 (vì e * d = 1 + k * phi)
    # Vì k là tử số của ước xấp xỉ, ta cần lặp qua các ước xấp xỉ.
    
    # Thử k = 1 (thường là trường hợp phổ biến nhất cho k/d)
    k = 1 
    
    # Giả định: e * d_guess = 1 + k * phi
    # => phi_guess = (e * d_guess - 1) / k
    
    # Kiểm tra điều kiện chính xác của d (mối quan hệ với phi)
    if (e * d_guess) % N != 1:
        # Nếu d * e không đồng dư 1 mod N, thử với k=2, k=3, ...
        # Tuy nhiên, trong tấn công Wiener, k thường là 1.
        # Chúng ta sẽ sử dụng k_guess từ ước xấp xỉ liên tục.
        pass
    
    # Mối quan hệ giữa N và phi(N) là:
    # N - phi(N) + 1 = p + q
    # Phương trình bậc hai để tìm p và q là:
    # x^2 - (p + q)x + N = 0
    
    for k_guess, d_guess in continued_fraction(e, N):
        if k_guess == 0: continue # Bỏ qua 0/1
        
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
                root_delta = math.isqrt(delta) 
                
                # Nếu delta là số chính phương, chúng ta tìm được p và q nguyên
                if root_delta * root_delta == delta:
                    p = (sum_pq + root_delta) // 2
                    q = (sum_pq - root_delta) // 2
                    
                    # 5. Xác nhận p * q = N và p, q là hai số khác nhau
                    if p * q == N and p != q and p > 1 and q > 1:
                        print(f"--- THÀNH CÔNG ---")
                        print(f"Tìm thấy khóa bí mật d: {d_guess}")
                        print(f"p: {p.bit_length()} bit, q: {q.bit_length()} bit.")
                        print(f"d: {d_guess.bit_length()} bit.")
                        return d_guess
                        
    return None

# --- Thực hiện giải mã ---

# Bước 1: Tìm khóa bí mật d
d_found = check_d(e, e, N) # e/N

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
    print("Không tìm thấy khóa bí mật d phù hợp bằng Wiener's Attack.")

"""
OUTPUT : 
--- THÀNH CÔNG ---
Tìm thấy khóa bí mật d: 79434351637397000170240219617391501050474168352481334243649813782018808904459
p: 1024 bit, q: 1024 bit.
d: 256 bit.
--------------------------------------------------
Giá trị Plaintext (số nguyên): 11515195063862319002386785506490949575337279649825636153248053928580408574830461
Flag đã giải mã: crypto{s0m3th1ng5_c4n_b3_t00_b1g}

"""
