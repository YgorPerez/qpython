from random import choice
n1 = int(input('digite um número: '))
n2 = int(input('digite outro número maior que o primeiro: '))
print('tente adivinhar o número que\neu estou pensando,entre {} e {} digite: '.format(n1,n2))
lista = []
for x in range (n1,n2+1,1):
    lista.append(x)
ls = choice(lista)
ns = int(input(''))
if ns == ls:
    print('parabens você acertou!!!\no número que tinha pensado era {}'.format(ls))
else:
     print('o número que tinha pensado era {} tente novamente'.format(ls))
