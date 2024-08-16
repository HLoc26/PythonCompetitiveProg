'''https://hnoj.edu.vn/problem/pa051'''
n = input().strip()

# print("YES" if n == n[::-1] else "NO")

l = 0
r = len(n) - 1
while l < r:
    if n[l] != n[r]:
        print("NO")
        break
    else:
        l+=1
        r-=1
else:
    print("YES")