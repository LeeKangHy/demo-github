import requests
import string

BASE_URL = "http://aes.cryptohack.org/ecb_oracle"
FLAG = ''
BLOCKSIZE = 32
KEYSPACE = string.ascii_letters + "!@#$%^&*()_+-=[]\;',./{}|:\"<>?~01234567890"

def encrypt(plaintext):
    url = f"{BASE_URL}/encrypt/{plaintext}/"
    encrypt_request = requests.get(url)
    return encrypt_request.json()["ciphertext"]

def split_blocks(ctxt):
    if len(ctxt) % BLOCKSIZE != 0:
        raise Exception("!")
    else:
        number_of_blocks = len(ctxt) // BLOCKSIZE
        return [ctxt[i*BLOCKSIZE:(i+1)*BLOCKSIZE] for i in range (number_of_blocks)]

def string_to_hex(txt):
    return txt.encode("utf-8").hex()

while True:
    ref_payload = 'A' * ((BLOCKSIZE-1) - len(FLAG))
    expected = encrypt(string_to_hex(ref_payload))
    expected_block = split_blocks(expected)[1]

    for char in KEYSPACE:
        cur_payload = ref_payload + FLAG + char
        current = encrypt(string_to_hex(cur_payload))
        current_block = split_blocks(current)[1]    
        if expected_block == current_block:
            FLAG += char
            print(f"FLAG: {FLAG}")
            break

    if FLAG.endswith('}'):
        break

print(FLAG)

#crypto{p3n6u1n5_h473_3cb}
