hex_string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
bytes_string = bytes.fromhex(hex_string)
"""
key = 16
flag = ""
for c in range(0,len(bytes_string)): 
    flag += chr(key^bytes_string[c])

print(flag)

"""

"""
for key in range(0,256) : 
   flag = ""
   for c in range(0, len(bytes_string)) :
      flag += chr(key ^ bytes_string[c])
  
   print(key,flag)    
"""

for key in range(0,256):
    flag = bytes(c ^ key for c in bytes_string)
    print(key,flag)

#OUTPUT: 16 b'crypto{0x10_15_my_f4v0ur173_by7e}'