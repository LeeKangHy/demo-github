#include <iostream>
#include <vector>
#include <iomanip> // Thư viện cần thiết

using namespace std;

void print_aligned_vectors(const vector<vector<double>>& vectors) {
    int i = 1;
    
    cout << "--- Cac Vector Truc Giao (Thang hang) ---\n";
    
    // 1. Thiết lập hiển thị số thập phân cố định và độ chính xác
    cout << fixed << setprecision(5); 

    // Vòng lặp in ra nội dung mảng 2 chiều
    for (const auto& u : vectors) {
        cout << "u" << i << ": ";
        
        // 2. Vòng lặp in ra từng phần tử (cột)
        for (const auto& component : u) {
            // Sử dụng setw(15) de dat do rong cot la 15 ky tu
            cout << setw(15) << component; 
        }
        
        cout << endl; // Xuống dòng
        i++;
    }
}

int main() {
    // Dữ liệu ma trận
    vector<vector<double>> orthogonal_vectors = {
        {4.0, 1.0, 3.0, -1.0},       
        {2.59259, 1.14815, -2.55556, 3.85185}, 
        {0.21739, 0.21739, -0.08696, -0.26087},
        {0.05882, 0.0, 0.41176, 0.0}      
    };

    print_aligned_vectors(orthogonal_vectors);

    return 0;
}