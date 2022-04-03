Cor = {'Azul':'\033[35m'}
print('{}digite um valor:'.format(Cor['Azul']))
Número = float(input(''))
Início = int(input('qual o início da tabuada?:\n'))
Final = int(input('e o final dela?:\n'))
'''
print('_'*15)
print('{} x {:2} = {}'.format(n,1,n*1)) 
print('{} x {:2} = {}'.format(n,2,n*2))
print('{} x {:2} = {}'.format(n,3,n*3))
print("{} x {:2} = {}".format(n,4,n*4))
print(n,'x  5 =',n*5,'\n{} x {:2} = {}'.format(n,6,n*6))
print('{} x {:2} = {}'.format(n,7,n*7))
print('{} x {:2} = {}'.format(n,8,n*8))
print('{} x {:2} = {}'.format(n,9,n*9))
print('{} x {} = {}'.format(n,10,n*10))
print('_'*15)
,
'''
print('_'*25,'\n')
for X in range (Início,Final+1):
    print ('{:.2f} x {} = {:.2f}'.format(Número, X, Número * X))
print('_'*25,'\n')