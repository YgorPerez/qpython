vm = float(input('qual é o limite de velocidade?: '))
v = float(input('qual a velocidade do carro?: '))
if v>vm:
         m = float(input('qual é o valor da multa por km/h excedido?: '))
         mkm = (v-vm)*m
         print('você recebeu uma multa de {:.2f}R$\npor exceder o limite de velocidade de {:.2f}km/h'.format(mkm,vm))
else:
         print('tenha um bom dia! e continue dirigindo\nabaixo de {:.2f}km/h'.format(vm))