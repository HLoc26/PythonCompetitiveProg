'''https://hnoj.edu.vn/problem/exam'''
def min_twos(N, k):
    total = 5 * N
    diff = total - k
    
    if diff < 0 or diff > 3 * N:
        return -1  # Không thể đạt được k điểm
    
    count_2 = max(0, diff - 2 * N)
    
    return count_2

# Đọc input
N, k = map(int, input().split())

# Tính và in kết quả
result = min_twos(N, k)
print(result)
'''
Phân tích lại bài toán:

Có N bài thi
Mỗi bài có điểm từ 2 đến 5
Mục tiêu: đạt chính xác k điểm
Cần tối thiểu hóa số bài điểm 2

Chiến lược đúng:
- Bắt đầu bằng cách cho tất cả bài điểm tối đa (5 điểm)
- Tính số điểm cần giảm: diff = 5N - k
- Giảm điểm từng bài, bắt đầu từ 5 xuống 4, 4 xuống 3, 3 xuống 2
- Đếm số bài điểm 2 cần thiết

Giải thích:

- Nếu diff < 0, nghĩa là không thể đạt được k điểm vì ngay cả
khi tất cả bài đều đạt điểm tối đa vẫn chưa đủ.
- Nếu diff > 3 * N, nghĩa là không thể đạt được k điểm vì ngay
cả khi tất cả bài đều đạt điểm tối thiểu (2) vẫn cao hơn k.
- Chúng ta có thể giảm tối đa 3 điểm cho mỗi bài (từ 5 xuống 2).
- Nếu diff <= 2 * N, chúng ta có thể giảm điểm mà không cần bài nào có điểm 2.
- Nếu diff > 2 * N, số bài điểm 2 cần thiết là diff - 2 * N.


Độ phức tạp: O(1) vì chúng ta chỉ thực hiện một số phép tính đơn giản.

Thuật toán này đảm bảo rằng TDZ sẽ có số lượng bài điểm 2 ít nhất có thể trong
khi vẫn đạt được chính xác k điểm. Nó xem xét tất cả các trường hợp có thể và tính toán
chính xác số bài điểm 2 cần thiết.
'''