Salário = float(input('Qual é o salário do funcionário? R$:\n'))
Porcentagem = float(input('Qual foi o aumento que ele recebeu? %:\n'))
Aumento = Salário*Porcentagem/100
Total = Aumento+Salário
print('O salário de {:.2f}R$, com o aumento de {:.2f}%\npassou a ser de {:.2f}R$'.format(Salário, Porcentagem,Total))
