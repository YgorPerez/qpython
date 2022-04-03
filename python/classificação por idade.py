from datetime import date
a = int(input('ano de nascimento: '))
i = date.today().year - a
if i<=14:
    print('{} anos é MIRIM'.format(i))
elif i<22:
    print('{} anos é JÚNIOR'.format(i))
elif i<25:
    print('{} anos é SENIOR'.format(i))
else:
    print('{} anos é MASTER'.format(i))