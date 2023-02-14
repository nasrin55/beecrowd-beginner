while True:
    try:
        e = str(input()).split()
        d = e[0]
        l = e[1]
        p = e[2]
        g = ''

        if d == l == p or d != l != p != d:
            g = 'tie'
        else:
            if d == l == 'papel':
                if p == 'pedra':
                    g = 'tie'
                elif p == 'tesoura':
                    g = 'pepper'
            elif d == l == 'pedra':
                if p == 'papel':
                    g = 'pepper'
                elif p == 'tesoura':
                    g = 'tie'
            elif d == l == 'tesoura':
                if p == 'pedra':
                    g = 'pepper'
                elif p == 'papel':
                    g = 'tie'

            elif l == p == 'papel':
                if d == 'pedra':
                    g = 'tie'
                elif d == 'tesoura':
                    g = 'dodo'
            elif l == p == 'pedra':
                if d == 'papel':
                    g = 'dodo'
                elif d == 'tesoura':
                    g = 'tie'
            elif l == p == 'tesoura':
                if d == 'pedra':
                    g = 'dodo'
                elif d == 'papel':
                    g = 'tie'

            elif d == p == 'papel':
                if l == 'pedra':
                    g = 'tie'
                elif l == 'tesoura':
                    g = 'leo'
            elif d == p == 'pedra':
                if l == 'papel':
                    g = 'leo'
                elif l == 'tesoura':
                    g = 'tie'
            elif d == p == 'tesoura':
                if l == 'pedra':
                    g = 'leo'
                elif l == 'papel':
                    g = 'tie'

        if g == 'tie':
            print('Putz vei, o Leo ta demorando muito pra jogar...')
        elif g == 'dodo':
            print('Os atributos dos monstros vao ser inteligencia, sabedoria...')
        elif g == 'leo':
            print('Iron Maiden\'s gonna get you, no matter how far!')
        elif g == 'pepper':
            print('Urano perdeu algo muito precioso...')
    except EOFError:
        break