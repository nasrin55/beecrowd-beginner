n = 0
count = 0
sum = 0
while(1):
    n = int(input())
    if(n >= 0):
        sum = sum + n
        count = count + 1
    else:
        break

avg = sum / float(count)
print("%.2f" %avg)
