Cor = {'Azul':'\033[1;34m'}
Número = 21
NúmeroExtenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while Número < 0 or Número > 20:
    Número = int(input('{} digite um número entre 0 e 20:\n'.format(Cor['Azul'])))
print(f'{NúmeroExtenso[Número]}')
while True:
    Resposta = str(input('Você quer continuar?\n S/N:')).upper().strip()
    if Resposta == 'S':
        Número = int(input('digite um número entre 0 e 20:\n'))
        print(f'{NúmeroExtenso[Número]}')
    elif Resposta == 'N':
        break
    else:
        Resposta = str(input('Você quer continuar?\n S/N:')).upper().strip()
