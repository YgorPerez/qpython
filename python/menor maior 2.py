Número1 = float(input('digite um número:\n'))
Número2 = float(input('digite outro:\n'))
Número3 = float(input('digite mais um número:\n'))
Menor = Número1
''' dá para reduzir uma linha de código se 
    você já assumir um número como < ou > 
    exemplo: linha 4 '''
if Número2 <= Número1 and Número1 <= Número3:
    Menor = Número2
elif Número3 <= Número1 and Número3 <= Número2:
    Menor = Número3
print('o menor é {:.2f}.'.format(Menor))
if Número1 >= Número2 and Número2 >= Número3:
    Maior = Número1
elif Número2 >= Número1 and Número2 >= Número3:
    Maior = Número2
else:
    Maior = Número3
print('e o maior é {:.2f}.'.format(Maior))
# código feito de duas maneiras
