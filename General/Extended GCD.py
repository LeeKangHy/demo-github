"""
def gcd(a,b):
 if b == 0 : 
  return a
 g = gcd(b,a%b)
 return g

"""

def egcd(a,b):
  if b == 0 :
    return a,1,0
  g,x,y = egcd(b,a%b)
  return g,y, x - a//b *y

 


print (egcd(26513,32321))