'''https://oj.vnoi.info/problem/hp_thpt_23_b'''
s = input().strip()
count = 0

for i in range(len(s)):
    if s[i].isdigit():
        count+=1
print(count)