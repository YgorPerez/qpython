cor = {'verde':'\033[1;36m'}
r = int(input('{}digite:\n[ 1 ] de °c para °f\n[ 2 ] de °c para k\n[ 3 ] de °f para °c\n[ 4 ] de °f para k\n[ 5 ] de k para c°\n[ 6 ] de k para °f\n'.format(cor['verde'])))
if r == 1:
    c = float(input('está quantos°c?:\n'))
    if c < - 273:
        print('não existe {:.2f}.°c'.format(c))
    elif c >= - 273:
        cf = (c*9)/5+32
        print('está {:.2f}°f'.format(cf))
elif r == 2:
    c = float(input('está quantos°c?:\n'))
    if c < - 273:
        print('não existe {:.2f}°c.'.format(c))
    elif c>=-273:
        ck = c+273
        print('está {:.2f}k.'.format(ck))
elif r ==3 :
    f = float(input('está quantos °f?:\n'))
    if f < - 459.40:
        print('não existe {:.2f}°f.'.format(f))
    elif f >= - 459.40:
        fc = (f-32)*5/9
        print('está {:.2f}c°'.format(fc))
elif r == 4:
    f = float(input('está quantos °f?:\n'))
    if f < - 459.40:
        print('não existe {:.2f}.'.format(f))
    elif f >= - 459.40:
        fk = (f-32)*5/9+273
        print('está {:.2f}k.'.format(fk))
elif r == 5:
    k = float(input('está quantos k?:\n'))
    if k < 0:
        print('não existe k negativo.')
    elif k>=0:
        kc = k-273
        print('está {:.2f}c°.'.format(kc))
elif r == 6:
    k = float(input('está quantos k?:\n'))
    if k < 0:
        print('não existe k negativo.')
    elif k >= 0:
        kf = (k-273)*9/5+32
        print('está {:.2f}f°.'.format(kf))
else:
    print('{} não é uma opção válida.'.format(r))
    