x = int(input())
count = 1
j = 0
while(j != 1):
    z = int(input())
    if(z > x):
        j = 1
sum = 0
for i in range(x, z):
    sum = sum + i
    if(sum > z):
        break
    count = count + 1
print(count)