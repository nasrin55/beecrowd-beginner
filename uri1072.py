n = int(input())
count1 = 0
count2 = 0
for i in range(n):
    n = int(input())
    if(n>=10 and n<=20):
        count1 = count1 + 1
    else:
        count2 = count2 + 1

print(f'{count1} in')
print(f'{count2} out')