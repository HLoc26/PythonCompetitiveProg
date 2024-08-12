'''https://hnoj.edu.vn/problem/pa020'''
import math

def solve_quadratic_equation(a, b, c):
    # Tính delta
    delta = b**2 - 4*a*c
    
    if delta > 0:
        # Hai nghiệm phân biệt
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return sorted([x1, x2], reverse=True)
    elif delta == 0:
        # Nghiệm kép
        x = -b / (2*a)
        return [x]
    else:
        # Vô nghiệm
        return []

# Đọc input
a = float(input())
b = float(input())
c = float(input())

# Giải phương trình
solutions = solve_quadratic_equation(a, b, c)

# In kết quả
if len(solutions) == 0:
    print("VO NGHIEM")
else:
    for x in solutions:
        print(f"{x:.3f}")
