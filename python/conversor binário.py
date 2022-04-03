r = int(input('escolha uma base de conversão\n1 para binário\n2 para hexadecimal\n3 pata octal:\n'))
n = int(input('digite um número: '))
if r==1:
    print('{} em binário é {}'.format(n,bin(n)[2:]))
elif r==2:
    print('{} em hexadecimal é {}'.format(n,hex(n)[2:]))
elif r==3:
    print('{} em octal é {}'.format(n,oct(n)[2:]))
else:
    print('{} não é um carácter válido.'.format(r))