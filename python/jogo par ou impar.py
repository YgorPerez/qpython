from random import randint
Computador = randint(0, 10)
Contador = 0
while True:
    ParImpar = str(input('Par ou impar? [P/I]:\n')).upper().strip()[0]
    Número = int(input('Digite um número:\n'))
    Total = Computador + Número
    while ParImpar not in 'PI':
        print(f'{ParImpar} não é um carácter válido')
        ParImpar = str(input('Tente novamente [P/I]:\n')).upper().strip()[0]
    print(f'Você jogou {Número} e o computador {Computador}. total = {Total}', end = ' ')
    print('Deu impar' if Total % 2 == 1 else 'deu par')
    if ParImpar == 'P':
        if Total % 2 == 0:
            Contador += 1
            print('Você venceu')
        else:
            print('Perdeste')
            break
    elif ParImpar == 'I':
        if Total % 2 == 1:
            print('Você venceu')
            Contador += 1
        else:
            print('Perdeste')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {Contador} vezes')
