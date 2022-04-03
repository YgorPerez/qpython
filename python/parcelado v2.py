p = float(input('qual o valor da compra?: R$\n'))
print('digite:\n[ 1 ] para pagar a vista\n[ 2 ] em cheque\n[ 3 ] em 2x no cartão\n[ 4 ] 3x ou mais no cartão: ')
r = int(input(''))
if r==1:
    d = p*10/100
    print('{:.2f} R$ à vista vai dar {:.2f} R$ por causa\ndo desconto de {:.2f} R$ ou seja 10%.'.format(p, p-d, d))
elif r==2:
    d = p*5/100
    print('{:.2f} R$ no cheque vai dar {:.2f} R$ por causa\ndo desconto de {:.2f} R$ ou seja 5%.'.format(p, p-d, d))
elif r==3:
    print('{:.2f} R$ parcelado em 2x vai dar duas parcelas de {:.2f} R$.'.format(p,p/2))
elif r==4:
    pp = int(input('quantas parcelas?: '))
    d = p*20/100
    t = (p+d)/pp
    print('{:.2f} R$ parcelado em {}x vai dar'.format(p, pp, end =''))
    print('{} parcelas de {:.2f} R$ totalizando {:.2f} R$.'.format(pp, t, p+d))
    print('por causa do juros de {:.2f} R$ ou seja 20%.'.format(pp))
else:
    print('{} não é um carácter válido.'.format(r))