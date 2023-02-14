def getInput():
    a,b,c,d = map(int, input().split())
    return a,b,c,d


def testtri(a,b,c):
    if((a+b) > c):
        if((a+c) > b):
            if((b+c) > a):
                return True
    else:
        return False
def main():
    a,b,c,d = getInput()
    if testtri(a,b,c) or testtri(a,b,d) or testtri(a,c,d) or testtri(b,c,d):
        print('S')
    else:
        print('N')
main()