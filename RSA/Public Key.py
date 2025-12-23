"""
encrypt f(m) = c = pow(m,e) mod n
 n = p* q,where p, q are the large primes
decrypt 
 Compute: phi(n)=(p−1)(q−1) 
 Then compute d, the modular inverse of e mod phi(n) : d = pow(e,-1) mod phi(n)
 Now d is the trapdoor key
 Once you have d : m = pow(c,d) mod n

explain 
 This works because of Euler's theorem pow(pow(m,e),d) = pow(m,e*d) = m (mod n)  (since ed = 1 mod phi(n))

SUMMARY 
  n,e,c : Public info — can encrypt, but not decrypt
  p,q,d : Trapdoor info — can decrypt (invert) 
"""
p = 17
q = 23
n = p*q
m = 12
e = 65537

print (pow(m,e,n))
