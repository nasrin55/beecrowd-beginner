from numpy.compat import long

n = int(input())
x = [int(i) for i in input().split()]
total = sum(x)
index = [0] * n
i = 0

while i>=0 and i<n:
    star = x[i] % 2
    if x[i] > 0:
        x[i] -= 1
        index[i] = 1
        total -= 1
    if star:
        i = i + 1
    else:
        i = i - 1

index = index.count(1)
print(index, total)