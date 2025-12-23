import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"  

decode_into_bytes = bytes.fromhex(hex_string)

encode_into_base64 = base64.b64encode(decode_into_bytes)

print(encode_into_base64.decode())

#OUTPUT : crypto/Base+64+Encoding+is+Web+Safe/