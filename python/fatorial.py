Cor = {'Verde':'\033[1;36m'}
from math import factorial
Número = int(input('{}digite um número para ver o seu fatorial:\n'.format(Cor['Verde'])))
#print('{} x {} = {}.'.format(Número, factorial(Número)))
Contador = Número
Fatorial = 1
print('{} ! é = '.format(Contador), end ='')
while Contador > 0:
    print('{}'.format(Contador), end ='')
    print(' x ' if Contador > 1 else ' é = ', end ='')
    Fatorial *= Contador
    Contador -= 1
print('{}.'.format(Fatorial))
    
