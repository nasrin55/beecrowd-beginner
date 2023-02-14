#from sympy import *

while True:
    try:

        m = int(input())
        v = []
        for i in range(m):
            x = int(input())
            v.append(x)

        n = int(input())
        sum = 0
        for i in range(1, len(v) + 1, n):
            sum += i
        # print(sum)
        if sum > 1:
            for i in range(2, sum//2):
                if sum % i == 0:
                    print('Bad boy! I’ll hit you.')
                    break
            else:
                print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
        else:
            print('Bad boy! I’ll hit you.')


    except EOFError:
        break