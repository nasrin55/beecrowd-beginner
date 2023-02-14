n = int(input())
while n:
    n -= 1
    pattern = input().split('-')
    if (len(pattern) == 2) and (len(pattern[0]) == 3) and (len(pattern[1]) == 4) and (pattern[0] == pattern[0].upper()):
        try:
            check = int(pattern[1])
            r = int(pattern[1][3])
            if r == 9  or r == 0:
                print('FRIDAY')
            elif r == 7  or r == 8:
                print('THURSDAY')
            elif r == 5  or r == 6:
                print('WEDNESDAY')
            elif r == 3  or r == 4:
                print('TUESDAY')
            elif r == 1  or r == 2:
                print('MONDAY')
        except:
            print('FAILURE')
    else:
        print('FAILURE')