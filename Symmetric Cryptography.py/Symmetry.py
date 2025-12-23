cipher = "7f4de2c70ae2823cc416a5ca06da0c418f73b51048ea0e8dac396291f6e25781446c1ce4a6e77537f0c3e4912823ecb284"
iv = cipher[:32]
ct = cipher[32:]
print(f"{iv = }{ct = }")

pt = '63727970746f7b3066625f31355f35796d6d3337723163346c5f2121213131217d'

FLAG = bytes.fromhex(pt).decode()
print(FLAG)

#crypto{0fb_15_5ymm37r1c4l_!!!11!}
