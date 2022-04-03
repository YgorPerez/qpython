kg = float(input('quanto você pesa?: '))
a = float(input('qual a sua altura?: '))
imc = kg/ (a**2)
if imc<10:
    print('imc = {:.2f}, 40 anos sem comer!!!'.format(imc))
elif imc<15:
    print('imc = {:.2f}, muito abaixo do peso, CUIDADO!'.format(imc))
elif imc<18.5:
    print('imc = {:.2f}, abaixo do peso, cuidado!'.format(imc))
elif imc<25:
    print('imc = {:.2f}, peso ideal!'.format(imc))
elif imc<30:
    print('imc = {:.2f}, sobrepeso.'.format(imc))
elif imc<35:
    print('imc = {:.2f}, semi-obeso, cuidado!'.format(imc))
elif imc<40:
    print('imc = {:.2f}, obeso, CUIDADO!'.format(imc))
elif imc<50:
    print('imc = {:.2f}, obesidade mórbida, MUITO CUIDADO!!!'.format(imc))
else:
    print('imc = {:.2f}, não enxerga nada, por causa que\nsua gordura entrou nos próprios olhos!'.format(imc))
print('de 10 para baixo é muito, muito magro\nentre 10 e 15 é muito magro\nentre 15 e 18.5 é magro\nentre 18.5 e 25 é o peso ideal\nentre 25 e 30 é sobrepeso\nentre 30 e 35 é semi-obeso\nentre 35 e 40 é obeso\n40 pra cima é obesidade mórbida.')
