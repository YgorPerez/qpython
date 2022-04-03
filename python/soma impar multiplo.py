s = 0
cont = 0
n1 = int(input('digite um número para ser o início:\n'))
n2 = int(input('digite um número para ser o final:\n'))
for c in range(n1,n2+1):
    if c%3==0 and c%2!=0:
        cont = cont+1
        s = s+c
print('a soma dos {} números ímpares divisíveis por 3\nentre {} e {} é {}'.format(cont, n1, n2, s))
else:   
    print('{} não é uma opção válida'.format(r))
