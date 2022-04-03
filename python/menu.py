Cor = {'Verde':'\033[1;32m'}
from time import sleep
Resposta = 0
print('_'*40)
Número1 = float(input('{}digite um número:\n'.format(Cor['Verde'])))
Número2 = float(input('digite outro número:\n'))
while Resposta != 5:
    sleep(1)
    print('_'*40)
    Resposta = int(input('o que você quer fazer?:\n[ 1 ] para somar\n[ 2 ] para multiplicar\n[ 3 ] para ver o maior\n[ 4 ] para digitar novos números\n[ 5 ] para sair:\n'))
    if Resposta == 1:
        print('{} + {} é = {}.'.format(Número1, Número2, Número1 + Número2))
    elif Resposta == 2:
        print('{} x {} é = {}.'.format(Número1, Número2, Número1 * Número2))
    elif Resposta == 3:
        if Número1 > Número2:
            Maior = Número1
            Menor = Número2
        elif Número2 > Número1:
            Maior = Número2
            Menor = Número1
        else:
            Número1 = Número2
        if Número1 == Número2:
            print('{} é = {}.'.format(Número1, Número2))
        elif Maior == Número1 or Maior == Número2:
            print('entre {} e {} o maior é {}.'.format(Número1, Número2, Maior))
    elif Resposta == 4:
        Número1 = float(input('digite um número:\n'))
        Número2 = float(input('digite outro número:\n'))
    elif Resposta == 5:
        print('fim do programa, volte sempre.')
    else:
        print('{} não é uma opção válida.'.format(Resposta))
