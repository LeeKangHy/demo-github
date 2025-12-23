"""
from pwn import * 
mission = xor("label", 13)
print(mission)
"""
string = "label"
key = 13 

result = ""

for c in string: 
    result += chr(ord(c)^key)

print(result)

