def int_hex(n):
    n = hex(n)
    n = n[2:] #count number after 2 digit
    return n

def main(n):
    n = n.upper() #return uppercase character
    print(n)
main(int_hex(int(input())))