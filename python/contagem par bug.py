Total = 0
r = int(input('o que deseja contar?:\n[ 1 ] para ímpares\n[ 2 ] para pares:\n'))
if r == 2:
    n = int(input('digite um número de início para contar os pares:\n'))
    n2 = int(input('digite um número para ser o fim:\n'))
    for c in range(n+1,n2+1):
        Total += 1
        if c%2!=0:
            Nada = 0
            print('{}.'.format(c))
print('o total de número pares foi {}.'.format(Total))
if r == 1:
    n = int(input('digite um número de início para contar os ímpares:\n'))
    n2 = int(input('digite um número para ser o fim:\n'))
    for c in range(n,n2+1):
        Total += 1
        if c%2 == 0:
            print('{}.'.format(c))
print('o total de número impares foi {}.'.format(Total))
if r!=1 or r!=2:
    print('{} não é uma opção válida, somente 1 ou 2'.format(r))
print('_'*5)