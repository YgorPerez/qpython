import math
a = float(input('digite o ângulo que deseja:'))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('o ângulo de {:.0f}° tem o SENO de {:.0f}°\no ângulo de {:.0f}° tem o COSSENO de {:.0f}°\no ângulo de {:.0f}° tem a TANGENTE de {:.0f}°'.format(a,s,a,c,a,t))
