from time import sleep
cor = {'azul':'\033[1;31m'}
n1 = int(input('{}digite um número para contagem regressiva, começo:\n'.format(cor['azul'])))
n2 = int(input('digite outro número para ser o fim:\n'))
print('=_=','^_^ '*4,'início! ','^_^ '*4,'=_=')
print('_'*50,'\n')
for c in range(n1, n2-1, -1):
    print('{}'.format(c, sleep(1)))
print('_'*50,'\n')
print('\o/','^_^ '*4,'FIM! ','^_^ '*4,'\o/')