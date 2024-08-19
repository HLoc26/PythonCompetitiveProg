'''https://hnoj.edu.vn/problem/loop12'''
def sum_of_digits(N):
    return sum(int(digit) for digit in N)

N = input()

result = sum_of_digits(N)
print(f"{result}")