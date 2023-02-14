t = int(input())
s1 = '010'
s2 = '101'
for i in range(t):
    s = input()
    if s1 in s or s2 in s:
        print('Good')
    else:
        print('Bad')


