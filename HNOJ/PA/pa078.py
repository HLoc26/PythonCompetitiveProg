'''https://hnoj.edu.vn/problem/pa078'''
temperatures = list(map(float, input().split()))

cold_days = [temp for temp in temperatures if temp < 10]
if cold_days:
    print(*cold_days)
else:
    print()

coldest = min(temperatures)
print(f"{coldest}")

hottest = max(temperatures)
print(f"{hottest}")