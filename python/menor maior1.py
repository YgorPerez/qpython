Número1 = float(input('digite um número:\n'))
Número2 = float(input('digite outro número:\n'))
if Número1 < Número2:
    print('{:.2f} é maior que {:.2f}.'.format(Número1, Número2))
elif Número1 > Número2:
    print('{:.2f} é maior que {:.2f}.'.format(Número1, Número2))
else:
    print('{:.2f} é igual a {:.2f}.'.format(Número1, Número2))