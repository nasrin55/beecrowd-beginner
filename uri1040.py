n1, n2, n3, n4 = map(float, input().split())

avg = ((n1*2) + (n2*3) + (n3*4) + (n4*1)) / (2+3+4+1)

if(avg >= 7.0):
    print('Media: %.1lf' % avg)
    print('Aluno aprovado.')
if(avg >= 5.0 and avg <= 6.9):
    n5 = float(input())
    print('Media: %.1lf' % avg)
    print('Aluno em exame.')
    print('Nota do exame: %.1lf' % n5)
    final_avg = (avg + n5) / 2
    if (final_avg >= 5.0):
        print('Aluno aprovado.')
    if (final_avg <= 4.9):
        print('Aluno reprovado.')
    print('Media final: %.1lf' % final_avg)
if(avg < 5.0):
    print('Media: %.1lf' % avg)
    print('Aluno reprovado.')

