from math import prod

# Các giá trị trong hệ đồng dư
a = [2, 3, 5]
n = [5, 11, 17]

# Bước 1: Tính N = n1 * n2 * n3
N = prod(n)

# Bước 2: Tính từng phần Ni = N / ni và tìm nghịch đảo của Ni mod ni
def modinv(a, m):
    """Tìm nghịch đảo của a mod m (a^{-1} mod m)"""
    a %= m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("Không có nghịch đảo modular")

# Bước 3: Áp dụng công thức CRT
x = 0
for ai, ni in zip(a, n):
    Ni = N // ni
    Mi = modinv(Ni, ni)
    x += ai * Ni * Mi

x %= N

print(f"Nghiệm duy nhất: x ≡ {x} (mod {N})")


"""
#FLAG : 872
"""