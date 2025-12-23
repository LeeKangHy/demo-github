from math import gcd

a = [588,665,216,113,642,4,836,114,851,492,819,237]

# Tính GCD của (a[i+1]^2 - a[i]*a[i+2])
vals = [a[i+1]**2 - a[i]*a[i+2] for i in range(len(a)-2)]
g = abs(vals[0])
for v in vals[1:]:
    g = gcd(g, abs(v))

print("GCD =", g)

# Hàm tìm số nguyên tố 3 chữ số chia hết cho g
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

candidates = [p for p in range(100, 1000) if is_prime(p) and g % p == 0]
print("Prime candidates:", candidates)

# Hàm nghịch đảo modulo (dùng thuật toán Euclid mở rộng)
def modinv(a, p):
    a %= p
    if a == 0:
        raise ValueError("no inverse")
    t, new_t = 0, 1
    r, new_r = p, a
    while new_r != 0:
        q = r // new_r
        t, new_t = new_t, t - q * new_t
        r, new_r = new_r, r - q * new_r
    if r > 1:
        raise ValueError("not invertible")
    if t < 0:
        t += p
    return t

# Thử từng p để tìm x hợp lệ
for p in candidates:
    try:
        x = (a[1] * modinv(a[0], p)) % p
    except ValueError:
        continue
    ok = all((a[i] * x) % p == a[i+1] % p for i in range(len(a)-1))
    if ok:
        print(f"✅ Found p = {p}, x = {x}")


"""
#FLAG : crypto{919,209}

nghiệm lại : 
for i in range(25,25+12):
    print(pow(209,i,919),end=" ")  #in ra tập hợp a

"""
