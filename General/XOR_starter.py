s = "label"
key = 13
for i in range(len(s)):
    print(chr(ord(s[i])^ key),end="")
#output : aloha 
