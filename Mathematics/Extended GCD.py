def egcd(a,b):
    if b == 0 : return a,1,0
    g,x,y = egcd(b,a%b)
    return g,y,x-a//b *y 

p=26513
q=32321
print(egcd(p,q))
"""
egcd(a,b) : tìm x,y sao cho a*x + b*y = GCD(a,b)

a*x + b*y = GCD(a,b) 
          = GCD(b,a%b)
          = b*x + (a%b)*y
          = b*x + (a - a//b*b)*y
          = a*y + b*(x - a//b*y)


==> giá trị x,y của hàm egcd(a,b) = giá trị y,(x-a//b*y) của hàm egcd(b,a%b)          
"""

    