a,b,c = map(int, input().split())

nums = [a,b,c]
x = max(nums)
y = min(nums)
z = a + b + c - x - y
if x >= y + z:
    print('Invalido')
else:
    if a != b and b != c and c != a:
        print('Valido-Escaleno')
        if a * a == b * b + c * c:
            print('Retangulo: S')
        else:
            print('Retangulo: N')
    elif a == b and b == c and c == a:
       print('Valido-Equilatero')
       if a * a == b * b + c * c:
           print('Retangulo: S')
       else:
           print('Retangulo: N')
    elif (a == b and b != c) or (b == c and c != a) or (c == a and a != b):
       print( 'Valido-Isoceles')
       if a * a == b * b + c * c:
           print('Retangulo: S')
       else:
           print('Retangulo: N')


