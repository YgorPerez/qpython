print('Quanto custa o valor do aluguel por dia? ')
ValorAluguel = float(input(''))
print('Quanto é pago por km rodado? ')
ValorKm = float(input(''))
print('Por quantos dias foi alugado o carro?')
DiaAlugado = int(input(''))
print('Quantos km foram percorridos\ncom ele durante esse tempo?:')
KmPercorrido = float(input(''))
TotalAluguel = ValorAluguel * DiaAlugado
TotalKm = ValorKm*KmPercorrido
TotalAbsoluto = TotalAluguel + TotalKm
print(f'O total a pagar vai ser {TotalAbsoluto:.2f}R$\nsendo {TotalAluguel:.2f}R$ de aluguel\ne {TotalKm:.2f} de km percorridos')
