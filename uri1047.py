
a1,b1,a2,b2 = list(map(int, input().split()))
dif = ((a2*60)+b2) - ((a1*60)+b1)
if(dif <= 0):
    dif = dif+24*60
h = dif//60
m = dif%60
print(f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')

