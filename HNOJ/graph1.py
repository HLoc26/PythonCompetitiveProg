a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

# Song song
if a1 == a2 and b1 != b2:
    print("Parallel")
# Trùng nhau
elif a1 == a2 and b1 == b2:
    print("Coincident")
# Cắt nhau
elif a1 != a2:
    if b1 == b2:
        x = 0
        y = b1
        print(f"Intersect {x:.6f} {y:.6f}")
    else:
        x = (b2-b1)/(a1-a2)
        y = a1*x + b1
        print(f"Intersect {x:.6f} {y:.6f}")