#cách chatgpt
# xor_with_pwn.py

import os
import sys
from PIL import Image
from pwn import xor    # cần cài pwntools: pip install pwntools

BASE_DIR = r"D:\Crypto\Lemur XOR"
IMG1 = os.path.join(BASE_DIR, "lemur.png")
IMG2 = os.path.join(BASE_DIR, "flag.png")
OUT  = os.path.join(BASE_DIR, "leak.png")

def load_and_normalize(path):
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    im = Image.open(path).convert("RGB")   # ép về RGB để chắc
    return im

def main():
    a = load_and_normalize(IMG1)
    b = load_and_normalize(IMG2)

    if a.size != b.size:
        raise ValueError(f"Kích thước khác nhau: {a.size} vs {b.size}. Hãy crop/resize hoặc xử lý trước.")

    # Lấy bytes thô (pixel order = RGBRGB...)
    a_bytes = a.tobytes()
    b_bytes = b.tobytes()

    # pwn.xor trả bytes
    out_bytes = xor(a_bytes, b_bytes)

    # Dựng lại ảnh từ bytes: mode và size nên trùng với ảnh đã convert
    out_im = Image.frombytes(a.mode, a.size, out_bytes)
    out_im.save(OUT)
    print("Saved:", OUT)

if __name__ == "__main__":
    main()

""" #cách của youtube
#https://www.youtube.com/watch?v=sQ2M64CtIzE


import cv2

img1 = cv2.imread("D:\Crypto\Lemur XOR/lemur.png")
img2 = cv2.imread("D:\Crypto\Lemur XOR/flag.png")

#AND 
final_AND = cv2.bitwise_and(img2,img1,mask = None)

#OR
final_OR = cv2.bitwise_or(img2,img1,mask = None)

#XOR
final_XOR = cv2.bitwise_xor(img2,img1,mask = None)

#NOT
final_NOT1 = cv2.bitwise_not(img1,mask = None)
final_NOT2 = cv2.bitwise_not(img2,mask = None)


#cv2.imshow("AND Output",final_AND)
#cv2.imshow("OR Output",final_OR)
#cv2.imshow("XOR Output",final_XOR)
#cv2.imshow("NOT Output 1",final_NOT1)
#cv2.imshow("NOT Output 2",final_NOT2) 


cv2.imshow("XOR Output",final_XOR)
cv2.waitKey(0)



"""

# FLAG :
# crypto{X0Rly_n0t!}

