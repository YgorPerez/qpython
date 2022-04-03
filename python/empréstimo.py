beleza = '\033[1;34m'
v = float(input('{}qual é o valor do empréstimo? R$: '.format(beleza)))
s = float(input('qual é o salário do funcionário? R$: '))
t = int(input('em quantos anos pretende pagar?: '))
ta = v/(t*12)
sa = s*30/100
if ta>sa:
    print('para pagar o empréstimo de\n{:.2f} R$ em {} anos a prestação seria de\n{:.2f} R$ empréstimo negado!'.format(v,t,ta))
    print('pois anlisamos que a fatura está muito\nalta para o seu salário de {:.2f} R$'.format(s))
else:
    print('para pagar o empréstimo de {:.2f} R$\nem {} anos a prestação seria de {:.2f} R$\nempréstimo liberado!'.format(v,t,ta,s), end='')
    print(' pois analisamos que\na fatura poderá ser paga!\npor causa do seu salário de {:.2f} R$'.format(s))