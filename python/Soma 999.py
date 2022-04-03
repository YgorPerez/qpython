Contador = Total = 0
while True:   
    Número = float(input('digite números para serem somados\n[999 para o programa]:\n'))
    if Número == 999:
        break
    Total += Número
    Contador += 1
print('a soma deu {} e você digitou {} números.'.format(Total, Contador))
