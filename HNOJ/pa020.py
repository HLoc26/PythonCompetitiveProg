'''https://hnoj.edu.vn/problem/pa020'''
def solve_quadratic(a, b, c):
    if a == 0:
        if b != 0:
            return (-c / b,)
        elif c == 0:
            return "Vô số nghiệm"
        else:
            return "Vô nghiệm"
    
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + (delta)**0.5) / (2 * a)
        x2 = (-b - (delta)**0.5) / (2 * a)
        return (x1, x2)
    elif delta == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        return "Vô nghiệm"

# Ví dụ
a, b, c = 1, -3, 2
print(solve_quadratic(a, b, c))
