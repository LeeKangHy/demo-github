state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def matrix2bytes(matrix):
    return bytes(sum(matrix,[]))

bytes_from_state = matrix2bytes(state)
bytes_from_round_key = matrix2bytes(round_key)



def add_round_key(s, k):
    return bytes(s[i]^k[i] for i in range (0,len(bytes_from_state)))


print(add_round_key(bytes_from_state,bytes_from_round_key))




#OUTPUT : b'crypto{r0undk3y}'



