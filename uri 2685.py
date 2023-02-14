while True:
    try:
        m = int(input())
        if m==360 or (m>=0 and m<90):
            print('Bom Dia!!')
        elif m>=90 and (m<180):
            print('Boa Tarde!!')
        elif m>=180 and m<270:
            print('Boa Noite!!')
        elif m>=270 and m<360:
            print('De Madrugada!!')


    except EOFError:
        break