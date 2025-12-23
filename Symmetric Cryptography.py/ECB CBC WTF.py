from Crypto.Cipher import AES
from Crypto.Util.Padding import*
from pwn import xor
import requests
url = 'https://aes.cryptohack.org/ecbcbcwtf/'
def encrypt_flag():
	r = requests.get(f"{url}/encrypt_flag")
	js = r.json()
	return (js["ciphertext"])

def decrypt(ciphertext):
	r = requests.get(f"{url}/decrypt/{ciphertext}")
	js = r.json()
	return (js["plaintext"])

cipher = encrypt_flag()
plaintext = decrypt(cipher)

iv1 = bytes.fromhex(cipher[:32])
ciphertext = cipher[32:]

iv2 = bytes.fromhex(ciphertext[:32])

plaintext1 =  bytes.fromhex(plaintext[32:64])
plaintext2 = bytes.fromhex(plaintext[64:])

print(xor(plaintext1, iv1) + xor(plaintext2, iv2))


#b'crypto{3cb_5uck5_4v01d_17_!!!!!}'
