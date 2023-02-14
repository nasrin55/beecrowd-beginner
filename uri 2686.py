while True:
    try:
        m = float(input())
        if m == 360 or (m >= 0 and m < 90):
            print('Bom Dia!!')
        elif m >= 90 and (m < 180):
            print('Boa Tarde!!')
        elif m >= 180 and m < 270:
            print('Boa Noite!!')
        elif m >= 270 and m < 360:
            print('Boa Madrugada!!')

        if m >= 270:
            hours = ((m - 270)*4) / 60
        else:
            hours = ((m * 4) / 60) + 6

        minutes = (hours * 60) % 60
        seconds = (minutes * 60) % 60

        if seconds > 59:
            seconds = 0
            minutes += 1

        hours =  int(hours)
        minutes = int(minutes)
        seconds = int(seconds)

        hours = str(hours).zfill(2)
        minutes = str(minutes).zfill(2)
        seconds = str(seconds).zfill(2)

        print(hours, ':', minutes, ':', seconds)
    except EOFError:
        break