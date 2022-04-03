from random import randint
cor = {'cinza':'\033[1;37m'}
TotalTentativas = 1
Tentativa = int(input('{}tente adivinhar o número que estou\npensando entre 1 e 100:\n'.format(cor['cinza'])))
Pc = randint(1,101)
while Tentativa!=Pc:
    TotalTentativas += 1
    if Tentativa < Pc:
        print('mais')
    elif Tentativa > Pc:
        print('menos')
    Tentativa = int(input('tente novamente:\n'))
if Tentativa == Pc:
    print('acertou, miseravi.\ndemorou {} tentativas.'.format(TotalTentativas))