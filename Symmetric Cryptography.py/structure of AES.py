text = b'crypto{inmatrix}'       #text này được giải ra từ trước

def bytes2matrix(text):
    return[list(text[i:i+4]) for i in range(0,len(text),4)]

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
 ]                                  #thực chất matrix = bytes2matrix(text) 


def matrix2bytes(matrix):
    return bytes(sum(matrix,[]))

print(matrix2bytes(matrix))   #OUTPUT :  b'crypto{inmatrix}'







""" HỌC CÚ PHÁP """
""" trong hàm bytes2matrix"""
# Bạn có đoạn:

# text = b'crypto{inmatrix}'
# list(text[i:i+4]) for i in range(0, len(text), 4)

# 1️⃣ text = b'crypto{inmatrix}'

# b'...' tạo byte string trong Python.

# Thay vì chuỗi bình thường (str) dùng các ký tự Unicode, byte string lưu trực tiếp giá trị byte của các ký tự ASCII.

# Ví dụ:

# text = b'crypto'
# print(text[0])  # 99


# Ở đây c có ASCII là 99, nên text[0] trả về số 99 (chứ không phải 'c').

# 2️⃣ text[i:i+4]

# Đây là cắt lát (slice) của bytes.

# i chạy từ 0 đến len(text) với bước 4 (xem phần range bên dưới).

# text[i:i+4] nghĩa là lấy 4 byte liên tiếp bắt đầu từ vị trí i.

# Ví dụ với text = b'crypto{inmatrix}':

# i=0 → text[0:4] = b'cryp'
# i=4 → text[4:8] = b'to{'
# i=8 → text[8:12] = b'inma'
# i=12 → text[12:16] = b'trix'

# 3️⃣ range(0, len(text), 4)

# range(start, stop, step) tạo một dãy số: từ start đến stop-1 với bước step.

# Ở đây: range(0, len(text), 4) tạo ra các giá trị [0, 4, 8, 12] (vì len(text)=16)

# Tức là i sẽ chạy lần lượt 0, 4, 8, 12 → tương ứng với từng khối 4 byte.

# 4️⃣ list(text[i:i+4])

# text[i:i+4] là một bytes object (ví dụ b'cryp').

# list(bytes_object) sẽ biến mỗi byte thành số nguyên (ASCII) trong danh sách.

# Ví dụ:

# list(b'cryp')  # → [99, 114, 121, 112]

# 5️⃣ Kết hợp lại

# Nếu viết đầy đủ thành list comprehension:

# [text[i:i+4] for i in range(0, len(text), 4)]


# Nó trả về các khối bytes 4 phần tử:

# [b'cryp', b'to{', b'inma', b'trix']


# Nếu thêm list(...) xung quanh mỗi khối như bạn viết:

# [list(text[i:i+4]) for i in range(0, len(text), 4)]


# Nó trả về danh sách các danh sách các giá trị byte:

# [[99, 114, 121, 112], [116, 111, 123], [105, 110, 109, 97], [116, 114, 105, 120]]


# ✅ Tóm tắt ý nghĩa:

# Code này chia chuỗi bytes text thành các khối 4 byte và chuyển từng byte thành giá trị số ASCII, tạo ra một danh sách các danh sách các số.



"""trong hàm matrix2bytes"""

# 1️⃣ sum(matrix, [])

# sum() trong Python thông thường dùng để tính tổng số.

# Nhưng nếu đối số là list, bạn có thể dùng nó để nối các list:

# sum(list_of_lists, start=[])


# list_of_lists là list chứa các list con.

# start=[] là list khởi tạo (bắt buộc để sum hoạt động với list).

# sum() sẽ nối tất cả các list con thành một list duy nhất.

# Ví dụ:

# matrix = [[1,2],[3,4],[5,6]]
# sum(matrix, [])
# # Output: [1, 2, 3, 4, 5, 6]


# Ở đoạn của bạn:

# sum(matrix, [])


# → Kết quả:

# [99, 114, 121, 112, 116, 111, 123, 105, 110, 109, 97, 116, 114, 105, 120, 125]

# 2️⃣ bytes(...)

# bytes() tạo bytes object từ iterable các số nguyên 0–255.

# Mỗi số nguyên sẽ trở thành 1 byte trong đối tượng bytes.

# Ví dụ:

# bytes([65,66,67])
# # Output: b'ABC'


# Vì 65 = 'A', 66 = 'B', 67 = 'C' theo ASCII.

# Ở đoạn của bạn:

# bytes(sum(matrix, []))


# → Nối tất cả các list con trong matrix thành 1 list duy nhất, rồi chuyển từng số ASCII thành byte.

# Kết quả là:

# b'crypto{inmatrix}'

# 3️⃣ Tổng hợp ý nghĩa

# Đoạn code:

# bytes(sum(matrix, []))


# ý nghĩa:

# matrix là ma trận 4x4 số ASCII.

# sum(matrix, []) → “dẹp” ma trận thành một danh sách dài các số ASCII.

# bytes(...) → chuyển danh sách số ASCII thành chuỗi bytes (tương đương với text ban đầu).

# Nói cách khác, đây là cách chuyển ma trận số về lại dạng bytes/chuỗi.