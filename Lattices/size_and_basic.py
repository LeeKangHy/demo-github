
import math 
v = (4,6,2,5)
res_1 = 0
for i in range (0,4):
    res_1 += pow(v[i],2)

res = math.sqrt(res_1)
print(int(res))

