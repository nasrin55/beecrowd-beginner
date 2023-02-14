n = int(input())
list = [int(x) for x in input().split()]
total = 1
for i in range(2, n):
    if list[i] - list[i-1] != list[i-1] - list[i-2]:
        total += 1
print(total)