'''https://hnoj.edu.vn/problem/pa095'''
import sys
sys.stdin = open('SUMX.INP','r')
sys.stdout = open('SUMX.OUT','w')
def count_pairs(A, x):
    seen = set()
    count = 0
    for a in A:
        if x - a in seen:
            count += 1
        seen.add(a)
    return count

# Đọc input
n, x = map(int, input().split())
A = list(map(int, input().split()))

# Tính kết quả
result = count_pairs(A, x)

# In kết quả
print(result)

'''
Hàm count_pairs(A, x) nhận vào dãy A và số x.
seen là một tập hợp để lưu các số đã xét qua.
Với mỗi số a trong A:

Chúng ta kiểm tra xem x - a có trong seen không.
Nếu có, điều này có nghĩa là chúng ta đã tìm thấy một cặp số có tổng bằng x.
Sau đó, chúng ta thêm a vào seen để sử dụng cho các phép kiểm tra tiếp theo.


Cuối cùng, chúng ta trả về số cặp đã đếm được.
'''