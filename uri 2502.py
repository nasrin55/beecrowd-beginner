while True:
    try:
        c,n = map(int, input().split())
        str1 = input().lower()
        str2 = input().lower()
        str1_aux = str1.upper()
        str2_aux = str2.upper()
        result = ''

        for i in range(n):
            text = input()
            text = list(text)

            for j in range(len(text)):
                for k in range(c):
                    if text[j] == str1[k]:
                        text[j] = str2[k]
                    elif text[j] == str2[k]:
                        text[j] = str1[k]
                    elif text[j] == str1_aux[k]:
                        text[j] = str2_aux[k]
                    elif text[j] == str2_aux[k]:
                        text[j] = str1_aux[k]
                result += text[j]
            print(result)
            result = ''
        print()

    except:
        break