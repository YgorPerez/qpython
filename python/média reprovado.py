cor ={'azul':'\033[1;34m'}
n1 = float(input('{}primeira nota: '.format(cor['azul'])))
n2 = float(input('segunda nota: '))
m = (n1+n2)/2
if m<6 and m>3:
    print('tirando {} e {} a média é {:.2f}, aluno de recuperação'.format(n1, n2, m))
elif m<=3:
    print('tirando {} e a média é {:.2f}, aluno reprovado'.format(n1 ,n2, m))
elif n1>10 or n2>10:
    print('a nota máxima é 10, não minta')
else:
    print('tirando {} e {} a média é {:.2f} aluno aprovado'.format(n1, n2, m))