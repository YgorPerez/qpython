s = float(input('quanto você ganha? R$: '))
if s>1250:
    a = (s*10/100)+s
    aa = 10
else:
    a = (s*15/100)+s
    aa = 15
at = a-s
print('com um aumento de {}%\nvocê passaria a ganhar {} R$'.format(aa,a))
print('ou seja um aumento de {} R$'.format(at))
