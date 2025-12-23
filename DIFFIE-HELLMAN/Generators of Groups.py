"""
g là phần tử nguyên thủy của trường hữu hạn Fp nếu:
 mọi phần tử khác 0 của Fp đều có thể viết được dưới dạng pow(g,k,p)  (k là 1 số bất kì)

 
Kiểm tra g có phải là phần tử nguyên thủy của trường hữu hạn Fp :
 1,Phân tích thừa số của (p-1)
  p-1 = ∏pow(q_i,e_i)
 2,Với mỗi q_i: 
  Tính s_i = pow(g, (p-1)/q_i ,p)
 3, Nếu tất cả s_i != 1 ---> g là phần tử nguyên thủy  
"""


def is_primitive_root(g, p):
    from sympy import factorint
    factors = factorint(p-1).keys()  # prime divisors
    for q in factors:
        if pow(g, (p-1)//q, p) == 1:
            return False
    
    return True

p = 28151

for i in range(1,100):
    if is_primitive_root(i,p) :
        print(i)

# min_value = 7

#Flag : 7


    








