from datetime import datetime, timedelta
while True:
    try:
        n1,n2 =input().split()

        if len(n1) == 1:
            n1 = '0' + n1
        if len(n2) == 1:
            n2 = '0' + n2
        date = '2016' + n1 + n2
        natal = '20161225'
        date = datetime.strptime(date, '%Y%m%d')
        natal = datetime.strptime(natal, '%Y%m%d')
        dias = (natal - date).days

        if dias == 0:
            print('E natal!')
        elif dias == 1:
            print('E vespera de natal!')
        elif dias < 0:
            print('Ja passou!')
        else:
            print('Faltam %d dias para o natal!' %dias)

    except EOFError:
        break