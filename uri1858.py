n = int(input())
d = input().split()

for i in range(n):
    d[i] = int(d[i])
minimum = min(d)
r = d.index(minimum) + 1
print(r)