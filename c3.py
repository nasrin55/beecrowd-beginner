def power_of_two(n):
    if n <= 0:
        return False
    else:
        return n & (n-1) == 0

n = int(input())

if power_of_two(n):
    print('YES')
else:
    print('NO')
