cor = {'vermelho':'\033[1;31m'}
Maior = 0
Menor = 0
Número = int(input('{}quer digitar quantos pesos?:\n'.format(cor['vermelho'])))
for c in range(1, Número+1):
    Peso = float(input('{}° peso:\n'.format(c)))
    if c == 1:
        Maior = Peso
        Menor = Peso
    else:
        if Peso > Maior:
            Maior = Peso
# o elif da linha 14 poderia ser um if
        elif Peso < Menor:
            Menor = Peso
print('o maior peso foi de {:.2f}kg e o menor de {:.2f}kg.'.format(Maior, Menor))
