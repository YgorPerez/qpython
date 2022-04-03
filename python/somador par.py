cont = 0
s = 0
n = int(input('quantos números pares quer somar?:\n'))
for c in range(1, n+1):
    n2 = int(input('digite o {} número de {}:\n'.format(c,n)))
    if n2 % 2 == 0:
        s = s+n2
        cont = cont+1
print('a soma dos {} números pares deu {}'.format(cont, s))
