n = int(input('digite um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('o número {} têm\n{} unidade de milhar\n{} unidade de centena\n{} unidades de dezenas\ne {} unidades'.format(n,m,c,d,u))
