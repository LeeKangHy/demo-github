from Crypto.Util.number import inverse

# d = inverse(3,13)
# print(d) #output : 9 

def egcd(a,b):
    if (b==0): return a,1,0
    g,x,y = egcd(b,a%b)
    return g,y,x-a//b*y 

g,d,y = egcd(3,13)

print(g,d,y)