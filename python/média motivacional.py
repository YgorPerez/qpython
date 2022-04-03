n1 = float(input('qual foi a sua nota no 1° bimestre?: '))
n2 = float(input('qual foi a sua nota no 2° bimestre?: '))
n3 = float(input('qual foi a sua nota no 3° bimestre?: '))
n4 = float(input('qual foi a sua nota no 4° bimestre?: '))
m = (n1+n2+n3+n4)/4
if m<6: 
    print('você tirou {:.2f}?! você ainda pode recuperar,\nse esforce mais\nda próxima vez'.format(m))
elif m>8:
    print('você tirou {:.2f}?! PARABÉNS!!! você é muito foda, inteligente\ne tem um potencial incrível'.format(m))
else: 
    print('você tirou {:.2f}?! parabéns! você é alguém acima da média!'.format(m))
