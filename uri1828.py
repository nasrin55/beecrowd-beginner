t = int(input())
for i in range(1,t+1):
    a,b = input().split()
    a = str(a)
    b = str(b)
    if(a == b):
        print('Caso #%d: De novo!' %i)

    elif(a=='tesoura' and (b=='papel' or b=='lagarto')):
        print('Caso #%d: Bazinga!' %i)
    elif (a == 'tesoura' and (b == 'Spock' or b == 'pedra')):
        print('Caso #%d: Raj trapaceou!' %i)

    elif (a == 'papel' and (b == 'Spock' or b == 'pedra')):
        print('Caso #%d: Bazinga!' %i)
    elif (a == 'papel' and (b == 'tesoura' or b == 'lagarto')):
        print('Caso #%d: Raj trapaceou!' %i)

    elif (a == 'pedra' and (b == 'lagarto' or b == 'tesoura')):
        print('Caso #%d: Bazinga!' %i)
    elif (a == 'pedra' and (b == 'papel' or b == 'Spock')):
        print('Caso #%d: Raj trapaceou!' %i)


    elif (a == 'lagarto' and (b == 'Spock' or b == 'papel')):
        print('Caso #%d: Bazinga!' %i)
    elif (a == 'lagarto' and (b == 'pedra' or b == 'tesoura')):
        print('Caso #%d: Raj trapaceou!' %i)

    elif (a == 'Spock' and (b == 'tesoura' or b == 'pedra')):
        print('Caso #%d: Bazinga!' %i)
    elif (a == 'Spock' and (b == 'lagarto' or b == 'papel')):
        print('Caso #%d: Raj trapaceou!' %i)