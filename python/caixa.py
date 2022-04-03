Cor = {'Azul':'\033[1;34m','Limpa':'\033[m'}
print('_' * 50)
print('{:^50}'.format('Banco python'))
print('{}'.format(Cor ['Azul']))
''' o jeito que eu fiz
Contador50 = Contador20 = Contador10 = Contador1 = 0
Dinheiro = int(input('quanto você quer sacar? R$:\n'))
while Dinheiro !=0:
    if Dinheiro >= 50:
        Contador50 += 1
        Dinheiro -= 50
    elif Dinheiro < 50 and Dinheiro >= 20:
        Contador20 += 1
        Dinheiro -= 20
    elif Dinheiro < 20 and Dinheiro >= 10:
        Contador10 += 1
        Dinheiro -= 10
    elif Dinheiro < 10 and Dinheiro >= 1:
        Contador1 += 1
        Dinheiro -= 1
print(f'foram necessárias\n{Contador50} notas de 50R$\n{Contador20} notas de 20R$\n{Contador10} notas de 10R$\n{Contador1} notas de 1R$\n')
print('{}{:^50}'.format(Cor ['Limpa'],'Obrigado e volte sempre'))
print('_' * 50)
''' # o jeito do Guanabara
TotalCédula = 0
Cédula = 100
Valor = int(input('quanto você quer sacar? R$:\n'))
Total = Valor
while True:
    if Total >= Cédula:
        Total -= Cédula
        TotalCédula += 1
    else:
        if TotalCédula > 0:
            print(f'Total de {TotalCédula} cédulas de R${Cédula}\n')         
        if Cédula == 100:
            Cédula = 50   
        elif Cédula == 50:
            Cédula = 20
        elif Cédula == 20:
            Cédula = 10
        elif Cédula == 10:
            Cédula = 5
        elif Cédula == 5:
            Cédula = 1
        TotalCédula = 0
        if Total == 0:
            break
print('{}{:^50}'.format(Cor ['Limpa'],'Obrigado e volte sempre'))
print('_' * 50)
