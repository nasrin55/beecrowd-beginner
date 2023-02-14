i = 0
j = 1
while(i<=2):
    for i in range(0, 3):
        if (i == 0):
            print("I=%.0f J=%.0f" % (i, j))
        else:
            # j = i+1
            print("I=%.1f J=%.1f" % (i, i + 1))
            # j = i+2
            print("I=%.1f J=%.1f" % (i, i + 2))
            # j = i+3
            print("I=%.1f J=%.1f" % (i, i + 3))
            j = j+1
    i = i + 0.2
    j = 1+i





