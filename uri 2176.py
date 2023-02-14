m = input()
one = 0

for i in m:
    if i == '1':
        one += 1
print(m + str(one % 2))