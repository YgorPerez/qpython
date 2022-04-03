Contador = 1
Número = float(input('digite um número:\n'))
Média1 = Número
Resposta = str(input('quer continuar? [s/n]:\n')).upper().strip()[0]
Maior = Número
Menor = Número
if Resposta == 'S':
    while Resposta == 'S':
        Contador += 1
        Número = float(input('digite um número:\n'))
        Média1 += Número
        if Número >= Maior:
            Maior = Número
        elif Número <= Menor:
            Menor = Número
        Resposta = str(input('quer continuar? [s/n]:\n')).upper().strip()[0]
Média2 = Média1 / Contador
if Resposta == 'N':
    print('a média dos {} números é {:.2f}, o maior é {} e o menor {}.'.format(Contador, Média2, Maior, Menor))
else:
    while Resposta not in 'S' or 'N':
        Resposta = str(input('{} não é uma opção válida, somente [s/n]\ndigite novamente:\n'.format(Resposta))).upper().strip()[0]
