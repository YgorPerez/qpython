Cor = {'Azul':'\033[1;34m'}
Velho = 0
Novo = 0
SomaIdade = 0
MédiaIdade = 0
MulherIdade = 0
Número = int(input('{}digite quantas pessoas quer analisar:\n'.format(Cor['Azul'])))
for X in range(1, Número+1):
    Idade = int(input('qual a idade da {}° pessoa?:\n'.format(X)))
    Nome = str(input('qual o nome da {}° pessoa?:\n'.format(X)))
    Sexo = str(input('qual o sexo da {}° pessoa?[ M/F ]:\n'.format(X))).upper()
    SomaIdade += Idade
    if X == 1 and Sexo in 'M' or Sexo == 'm':
         Velho = Idade
         NomeVelho = Nome
    elif Idade > Velho and Sexo in 'M' or Sexo == 'm':
         Velho = Idade
         NomeVelho = Nome
    elif Idade < Velho and Sexo in 'M' or Sexo == 'm':
        Nada = 0
    elif Idade < 20 and Sexo in 'F' or Sexo == 'f' and Idade < 20:
        MulherIdade += 1
    elif Idade >= 20 and Sexo in 'F' or Sexo == 'f' and Idade < 20:
        Nada = 0
#if Sexo == 'M' or 'm':
#    Sexo = 'homem'
#elif Sexo == 'F' or 'f':
#    Sexo = 'mulher'
    else:    
        print('{} não existe é F ou M'.format(Sexo))
MédiaIdade = SomaIdade / Número
print('a média de idade foi de {:.2f}.'.format(MédiaIdade))
if Sexo == 'M' or Sexo == 'm':
    print('o homem mais velho tem {} anos e se chama {}.'.format(Velho, NomeVelho))
if MulherIdade > 1:
    Plural1 = 'es '
   # Plural2 = 'ê'
else:
    Plural1 = ' '
#    Plural2 = ''
print('{} mulher{}tem menos de 20 anos.'.format(MulherIdade, Plural1))
