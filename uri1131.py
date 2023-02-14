total_gre = 0
victory_of_inter = 0
victory_of_gremio = 0
number_of_draws = 0
j = 0
while(True):
    x,y = list(map(int, input().split()))
    if(x>y):
        victory_of_inter = victory_of_inter + 1
    if(x<y):
        victory_of_gremio = victory_of_gremio + 1
    if(x == y):
        number_of_draws = number_of_draws + 1
    total_gre = total_gre + 1
    print('Novo grenal (1-sim 2-nao)')
    n = int(input())
    if(n == 1):
        continue
    if(n==2):
        break

print('{} grenais'.format(total_gre))
print('Inter:{}'.format(victory_of_inter))
print('Gremio:{}'.format(victory_of_gremio))
print('Empates:{}'.format(number_of_draws))

if(victory_of_inter > victory_of_gremio):
    print('Inter venceu mais')
if(victory_of_inter < victory_of_gremio):
    print('Gremio venceu mais')
if(victory_of_inter == victory_of_gremio):
    print('Não houve vencedor')