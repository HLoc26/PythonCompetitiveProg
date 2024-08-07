'''https://hnoj.edu.vn/problem/hnoi2122c2_tbg'''
import sys
sys.stdin = open('TBG.INP','r')
sys.stdout = open('TBG.OUT','w')

X, Y, Z = map(int, input().split())

# Tổng dung lượng video
tongDL = X * Z

# Độ chênh lệch trong 1s
cl = X - Y

# Tổng độ chênh lệch sau Z giây
tong_cl = cl * Z


# Thời gian chờ T0
t0 = tong_cl // Y # 15.6...
if tong_cl % Y != 0:
    t0 += 1
    
print(t0)


'''
Để giải quyết bài toán này, chúng ta cần tính toán thời gian tối
thiểu T0 mà An cần đợi để có thể xem video liên tục. Hãy phân tích bài toán từng bước:

Đầu tiên, chúng ta cần tính toán tổng dung lượng của video:
Tổng dung lượng = X * Z (MB)
Sau đó, chúng ta cần tính toán sự chênh lệch giữa tốc độ tải xuống và tốc độ phát video:
Chênh lệch mỗi giây = X - Y (MB)
Tổng chênh lệch sau Z giây:
Tổng chênh lệch = (X - Y) * Z (MB)
Đây chính là lượng dữ liệu mà An cần tải trước để có thể xem video liên tục.
Thời gian cần thiết để tải lượng dữ liệu này với tốc độ Y MB/giây:
T0 = Tổng chênh lệch / Y = ((X - Y) * Z) / Y
'''
