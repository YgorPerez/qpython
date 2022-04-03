s1 = float(input('digite um segmento\npara formar um triângulo: '))
s2 = float(input('outro: '))
s3 = float(input('o último: '))
if s2+s3 > s1 and s3+s1 > s2 and s2+s1 > s3:
    print('é possível formar um triângulo', end='')
    if s1==s2==s3:
        print(' EQUILÁTERO!')
    elif s1==s2 or s2==s3 or s1==s3:
        print(' ISÓCELES!')
    else:
        print(' ESCALENO!')
else:
    print('não é possível formar um triângulo!')