Cor = {'Limpa':'\033[m','Azul':'\033[1;34;47m','Verde':'\033[4;32;0m','Vermelho':'\033[4;31m'}
Km = float(input('{}Qual é a distância da viagem? km: '.format(Cor['Azul'])))
if Km < 200:
    Velocidade = Km / 2
else:
    Velocidade = Km / 2.25
print(f''Uma viagem de {Cor}{Km:.0f} Km vai dar {Velocidade:.2f} R$'')