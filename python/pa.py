Contador = 1
Total = 0
Número = int(input('primeiro termo:\n'))
Termo = Número
Razão = int(input('razão:\n'))
Até = int(input('vai até qual termo?:\n'))
while Contador <= Total:
    print('{} ~'.format(Termo), end ='')
    Termo += Razão
    Contador += 1
    print('{} ~'.format(Termo), end ='')
while Até != 0:
    Total = Total + Até
    while Contador <= Total:
        print('{} ~'.format(Termo), end ='')
        Termo += Razão
        Contador += 1
    Até = int(input('quer mostrar mais quantos termos?:\n'))
print('progressão finalizada com {} termos.'.format(Total))
    