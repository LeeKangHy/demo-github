import numpy as np

def gram_schmidt(vectors):
    """
    Áp dụng thuật toán Gram-Schmidt để tìm cơ sở trực giao cho một tập hợp vector.
    
    Args:
        vectors (list of numpy arrays): Danh sách các vector đầu vào (v1, v2, v3, v4).
        
    Returns:
        list of numpy arrays: Cơ sở trực giao (u1, u2, u3, u4).
    """
    
    # Khởi tạo danh sách chứa các vector trực giao
    orthogonal_basis = []
    
    for v in vectors:
        # Vector mới (u_k) ban đầu bằng vector đầu vào (v_k)
        u_k = v
        
        # Trừ đi phép chiếu (projection) của v_k lên tất cả các vector trực giao u_j đã tìm được
        for u_j in orthogonal_basis:
            # Tính tích vô hướng (dot product): <v_k, u_j>
            dot_product = np.dot(v, u_j)
            
            # Tính bình phương độ dài (norm squared): <u_j, u_j>
            norm_sq = np.dot(u_j, u_j)
            
            # Tính hệ số chiếu: ( <v_k, u_j> / <u_j, u_j> )
            projection_factor = dot_product / norm_sq
            
            # Phép trừ: u_k = u_k - proj_{u_j} v_k
            u_k = u_k - projection_factor * u_j
            
        # Thêm vector trực giao u_k mới tìm được vào danh sách
        # NumPy tự động xử lý các phép tính phân số/thập phân.
        orthogonal_basis.append(u_k)
        
    return orthogonal_basis

# --- Dữ liệu đầu vào ---
# Các vector của bạn: v1, v2, v3, v4
v1 = np.array([4, 1, 3, -1], dtype=float)
v2 = np.array([2, 1, -3, 4], dtype=float)
v3 = np.array([1, 0, -2, 7], dtype=float)
v4 = np.array([6, 2, 9, -5], dtype=float)

input_vectors = [v1, v2, v3, v4]

# --- Thực thi thuật toán Gram-Schmidt ---
orthogonal_vectors = gram_schmidt(input_vectors)

# --- In kết quả ---
print("--- Cơ sở Trực giao (Orthogonal Basis) ---")

for i, u in enumerate(orthogonal_vectors):
    print(f"u{i+1} (Trực giao): {u}")

print("\n(Lưu ý: Các giá trị là số thực do tính toán chiếu, nhưng vẫn trực giao)")