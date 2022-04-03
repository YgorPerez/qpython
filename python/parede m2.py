print('a largura da parede?:')
l = float(input(''))
print('a altura da parede?:')
a = float(input(''))
mq = l*a
x = float(input('quantos litros você gasta por m2?: '))
t = mq/x
print('{} x {} sua parede têm {:.2f}m2\nserá necessário {:.2f}litros de tinta para pintala'.format(l,a,mq,t))
