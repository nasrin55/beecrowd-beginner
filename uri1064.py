count = 0
total = 0

for i in range(1,7):
    n = float(input())
    if n > 0:
        count = count + 1
        total = total + n


print("{} valores positivos".format(count))
print("%0.1f"%(total/count))