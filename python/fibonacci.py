Cor = {'Vermelho':'\033[1;31m'}
Termo1 = 0
Termo2 = 1
Número = int(input('{}quantos termos quer mostrar?\n'.format(Cor['Vermelho'])))
print('{} ~ {} '.format(Termo1, Termo2), end ='')
while Número-2 > 0:
    Termo3 = Termo1 + Termo2
    print('~ {} '.format(Termo3), end ='')
    Termo1 = Termo2
    Termo2 = Termo3
    Número -= 1
print('Acabou.')