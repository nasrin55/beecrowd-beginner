n = input()
c = [int(x) for x in input().split()]
m = [int(x) for x in input().split()]
count = 0
for i in c:
    if not i in m:
        count += 1
print(count)