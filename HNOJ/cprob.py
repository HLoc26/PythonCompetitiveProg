'''https://hnoj.edu.vn/problem/cprob'''
def count_digits(n):
    total = 0
    for i in range(1, len(str(n)) + 1):
        if 10**(i-1) <= n:
            total += (min(10**i - 1, n) - 10**(i-1) + 1) * i
    return total

def find_nth_digit(n):
    length = 1
    count = 9
    start = 1
    
    while n > length * count:
        n -= length * count
        length += 1
        count *= 10
        start *= 10
    
    start += (n - 1) // length
    return int(str(start)[(n - 1) % length])

def find_pages(n):
    if n <= 0:
        return -1

    total_digits = 0
    pages = 0
    length = 1

    while total_digits < n:
        start = 10 ** (length - 1)
        end = 10 ** length - 1
        count = end - start + 1
        digits_in_range = count * length

        if total_digits + digits_in_range >= n:
            remaining = n - total_digits
            full_numbers = remaining // length
            pages += full_numbers
            
            if remaining % length == 0:
                return pages
            else:
                return -1
        
        total_digits += digits_in_range
        pages += count
        length += 1

    return -1

n = int(input())
print(count_digits(n))
print(find_nth_digit(n))
print(find_pages(n))
