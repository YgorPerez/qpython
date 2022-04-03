print('está quantos°c?:')
c = float(input(''))
fc = (c*9)/5+32
print('está {:.2f}°f'.format(fc))
print('está quantos f°?: ')
f = float(input(''))
cf = (f-32)*5/9
print('está {:.2f}c°'.format(cf))
c2 = float(input('está quantos c°?: '))
ck = c2+273
print('está {:.2f}k'.format(ck))
k = float(input('está quantos k?: '))
if k<0:
    print('não existe Kelvin negativo!')
else:
    kc = k-273
    print('está {:.2f}c°'.format(kc))
