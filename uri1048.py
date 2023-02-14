s = float(input())
if(s>=0 and s<=400.00):
    es = s * (15/100)
    ns = s + es
    print('Novo salario: %.2lf' % ns)
    print('Reajuste ganho: %.2lf' % es)
    print('Em percentual: 15 %')
elif(s>=400.01 and s<=800.00):
    es = s * (12 / 100)
    ns = s + es
    print('Novo salario: %.2lf' % ns)
    print('Reajuste ganho: %.2lf' % es)
    print('Em percentual: 12 %')
elif(s>=800.01 and s<=1200.00):
    es = s * (10 / 100)
    ns = s + es
    print('Novo salario: %.2lf' % ns)
    print('Reajuste ganho: %.2lf' % es)
    print('Em percentual: 10 %')
elif(s>=1200.01 and s<=2000.00):
    es = s * (7 / 100)
    ns = s + es
    print('Novo salario: %.2lf' % ns)
    print('Reajuste ganho: %.2lf' % es)
    print('Em percentual: 7 %')
else:
    es = s * (4 / 100)
    ns = s + es
    print('Novo salario: %.2lf' % ns)
    print('Reajuste ganho: %.2lf' % es)
    print('Em percentual: 4 %')