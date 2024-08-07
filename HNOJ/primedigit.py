n = int(input())

s = str(n)
count = 0
for char in s:
    if int(char) in [2, 3, 5, 7]:
        count+=1

print(count)