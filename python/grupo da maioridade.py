Cor = {'Azul':'\033[1;34m'}
from datetime import date
Número = int(input('{}digite o número de pessoas que quer\nsaber se são maior de idade:\n'.format(Cor['Azul'])))
Maioridade = 0
DeMenor = 0
DataHoje = 0 + date.today().year
for c in range(Número, 0, -1):
    DataNasc = int(input('digite a data de nascimento de {} pessoas:\n'.format(c)))
    Idade = DataHoje - DataNasc
    if Idade >= 18 and DataNasc <= DataHoje:
        Maioridade += 1
    elif Idade < 18 and DataNasc <= date.today().year:
        DeMenor += 1
    else:
        print('{} não chegou ainda estamos em {}'.format(DataNasc, DataHoje))
print('{} pessoas são maior de idade e {} São menor de idade'.format(Maioridade, DeMenor))
