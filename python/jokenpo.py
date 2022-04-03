from random import randint
from time import sleep
cor = {'azul':'\033[1;34m'}
print('{}digite:\n[ 0 ] para pedra\n[ 1 ] para papel\n[ 2 ] para tesoura: '.format(cor['azul']))
r = int(input(''))
l = ['pedra','papel','tesoura']
c = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('_'*35)
if c==0 and r==1 or c==1 and r==2 or c==2 and r==0:
    print('o computador escolheu {}'.format(l[c]))
    print('você jogou {}, jogador vence!'.format(l[r]))
elif r==c:
    print('o computador escolheu {}'.format(l[c]))
    print('você jogou {}, empatou!'.format(l[r]))
elif c==0 and r==2 or c==1 and r==0 or c==2 and r==1:
    print('o computador escolheu {}'.format(l[c]))
    print('você jogou {}, computador vence!'.format(l[r]))
else:
    print('{} não é um carácter válido.'.format(r))
print('_'*35)
