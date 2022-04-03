s = 0
cont = 0
n1 = int(input('digite um número para ser o início:\n'))
n2 = int(input('digite um número para ser o final:\n'))
r = int(input('o que quer procurar?\n[ 1 ] para ímpar\n[ 2 ] para par:\n'))
d = int(input('quer que seja múltiplo de quanto?:\n'))
if r == 1:
    for c in range(n1,n2+1):
        if c%d==0 and c%2!=0:
            cont = cont+1
            s = s+c
    print('a soma dos {} números ímpares divisíveis por {}\nentre {} e {} é {}'.format(cont, d, n1, n2, s))
elif r == 2:
    for c in range(n1,n2+1):
        if c % d == 0 and c % 2 == 0:
            cont = cont+1
            s = s+c
    print('a soma dos {} números pares divisíveis por {}\nentre {} e {} é {}'.format(cont, d, n1, n2, s))
else:   
    print('{} não é uma opção válida, somente 1 e 2'.format(r))
