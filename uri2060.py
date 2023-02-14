n = int(input())
multiple2 = 0
multiple3 = 0
multiple4 = 0
multiple5 = 0

value = input().split()
values = value[:n]
for i in range(n):
    values[i] = int(values[i])
    if(values[i] % 2 == 0):
        multiple2 += 1
    if(values[i] % 3 == 0):
        multiple3 += 1
    if(values[i] % 4 == 0):
        multiple4 += 1
    if(values[i] % 5 == 0):
        multiple5 += 1

print('{0} Multiplo(s) de 2'.format(multiple2))
print('{0} Multiplo(s) de 3'.format(multiple3))
print('{0} Multiplo(s) de 4'.format(multiple4))
print('{0} Multiplo(s) de 5'.format(multiple5))
