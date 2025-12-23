#from ascii to character
arr = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

for i in arr :
    print(chr(i),end ="")


#crypto{ASCII_pr1nt4bl3}


"""
#from bytes to ASCII

s = b'crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}'

#s[0] = 99 (ASCII của 'c') 
#s[1] = 114 (ASCII của 'r')

for b in s:      # b sẽ chạy với các s[i] với i = 0,1,2,.... 
    char = chr(b)                # byte → ký tự ASCII
    ascii_value = ord(char)      # ký tự → ASCII (dùng ord)
    print(ascii_value,  end=" ") 

"""

