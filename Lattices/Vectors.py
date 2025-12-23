# # cách 1  ( tư duy c++ nguyên thủy)
# v = [2,6,3]
# w = [1,0,0]
# u = [7,7,2]
# n = int(input("Nhap vao so phan tu cua mang res: "))
# res_1 = [0]*n
# ans = 0 
# for i in range (0,3): 
#    res_1[i] = 3*(2*v[i] - w[i])*2     
#    ans += res_1[i]*u[i]


# print(ans)



#cách 2 (dùng thư viện numpy )
import numpy as np 
v = np.array([2,6,3])
w = np.array([1,0,0])
u = np.array([7,7,2])

ans = np.dot(3*(2*v - w),2*u)
print(ans)

   