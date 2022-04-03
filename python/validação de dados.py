Sexo = str(input('Qual o seu sexo [M/F]?:\n')).strip().upper()[0]
while Sexo not in 'MmFf':
    Sexo = str(input('{} não é um sexo, somente m ou f\ndigite novamente:\n'.format(Sexo))).strip().upper()[0]
if Sexo == 'M':
    print('Sexo registrado como masculino.')
else:
    print('Sexo registrado como feminino.')
