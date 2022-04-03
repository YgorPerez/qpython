print('_' * 35)
while True:
    print('_' * 35)
    Número = float(input('quer ver a tabuada de qual número?\n'))
    if Número < 0:
        break
    Início = int(input('quando ela começa?\n'))
    Final = int(input('e o fim dela?\n'))
    for X in range(Início, Final+1):
        print(f'{Número:.2f} x {X} = {Número * X:.2f}')
    print('_' * 35)
