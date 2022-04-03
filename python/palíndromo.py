Cor = {'Rosa':'\033[1;35m', 'Amarelo':'\033[1;33m', 'Limpa':'\033[m', 'Invertido':'\033[7m'}
Frase = str(input('{}digite uma frase para vela ao contrário\ne saber se ela é um palíndromo:\n'.format(Cor['Rosa']))).strip().lower()
FraseSeparada = Frase.split()
FraseJunta1 = ' '.join(FraseSeparada)
FraseJunta2 = ''.join(FraseSeparada)
FraseInversa1 = FraseJunta1[::-1]
FraseInversa2 = FraseJunta2[::-1]
print('{}a frase {} ao\ncontrário é {}.'.format(Cor['Limpa'], Frase, FraseInversa1))
if FraseInversa2 == FraseJunta2:
    print('{}{} é um palíndromo.'.format(Cor['Amarelo'], Frase))
else:
    print('{}{} não é um palíndromo.'.format(Cor['Invertido'], Frase))
