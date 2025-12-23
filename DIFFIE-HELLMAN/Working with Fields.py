# ax+by = g || function egcd(a,b) return g, x ,y 
# if a and b is coprime, that function give : ax = 1 (mod b)
def egcd(a,b):
    if(b==0): return a,1,0
    g,x,y = egcd(b,a%b) 
    return g,y,x-(a//b)*y 

print(egcd(209,991))  # output thoa man : 209*(-422) + 991*89 = 1 , lay mod 991 hai ve, ta duoc 209*(-422) = 1 (mod 991) 
                    # nghich dao modulor 991 cua 209 la (991-422) = 569
#FLAG : 569 



"""
#cách 2 
from Crypto.Util.number import inverse

d = inverse(209,991)
print(d)
"""