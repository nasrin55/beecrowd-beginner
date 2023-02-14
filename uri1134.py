a = 0
g = 0
d = 0
while(True):
    n = int(input())
    if(n == 1):
        a = a + 1
    if(n == 2):
        g = g + 1
    if(n == 3):
        d = d + 1
    if(n == 4):
        break

print('MUITO OBRIGADO')
print('Alcool: {}'.format(a))
print('Gasolina: {}'.format(g))
print('Diesel: {}'.format(d))