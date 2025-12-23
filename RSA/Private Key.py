#function to find inverse modulor of a mod b 

"""
Explain : we know extended euclid algorithm  
(*): a*x + b*y = gcd (a,b)
 if a and b are coprime -> gcd(a,b) = 1
(*) -> a*x + b*y = 1
take mod b on both side 
   (a*x+b*y) mod b = 1 mod b
-> a*x = 1 mod b

Conclusion : x is the inverse modulor of a mod b 
"""
def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)  # g = gcd(a,b) | x1 = a | y1 = b
    return g, y1, x1 - (a // b) * y1

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
phi = (p-1)*(q-1)
e=65537 

a, b,c = egcd(e,phi)
print(b)


"""
#FLAG :
121832886702415731577073962957377780195510499965398469843281
"""



    