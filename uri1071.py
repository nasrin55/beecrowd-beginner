a = int(input())
b = int(input())
sum = 0
for n in range((b+1), a):
    if(n%2 != 0):
        sum = sum + n
print(sum)