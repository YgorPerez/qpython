from math import hypot
''' print('qual é o comprimento do cateto oposto?:')
 catetoOposto = float(input(''))
 print('e do adjacente?:')
 catetoAdjacente = float(input(''))
 hipotenusa = (catetoOposto ** 2 + catetoAdjacente **2) ** (1/2)
 print('a hipotenusa é {:.2f}'.format(hipotenusa))
'''
CatetoOp = float(input('qual é o comprimento do cateto oposto?:'))
CatetoAd = float(input('e do adjacente?:'))
Hipotenusa = hypot(CatetoOp, CatetoAd)
print(f'a hipotenusa é = a {Hipotenusa:.2f}')
