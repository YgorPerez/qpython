print('quanto custa o produto? R$:')
p = float(input(''))
print('quanto você tem de desconto? %:')
d = float(input(''))
r = p*d/100
t = p-r
print('o produto que custava {:.2f}reais\nÁgora custa {:.2f} reais\ndevido á promoção de {:.2f}% de desconto'.format(p,t,d))