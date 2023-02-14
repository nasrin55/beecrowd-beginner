count1 = 0
count2 = 0
count3 = 0
count4 = 0
for i in range(1,6):
    n = int(input())
    if (n%2 == 0):
        count1 = count1 + 1

    if(n%2 != 0):
        count2 = count2 + 1

    if(n > 0):
        count3 = count3 + 1

    if(n < 0):
        count4 = count4 + 1


print(f'{count1} valor(es) par(es)')
print(f'{count2} valor(es) impar(es)')
print(f'{count3} valor(es) positivo(s)')
print(f'{count4} valor(es) negativo(s)')