Número = int(input('Digite um número para ver se ele é primo:\n'))
NúmeroD = Número / 2
NúmeroI = Número % 2
if Número <= 2 or NúmeroD == NúmeroI:
    print(f'{Número} não é primo')
