from decimal import Decimal
n = input()
if Decimal(n) >= 0 and n[0] != '-':
    print('+', end='')
print('%.4E' %Decimal(n))