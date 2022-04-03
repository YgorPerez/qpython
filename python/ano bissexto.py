from datetime import date
Ano = int(input('Digite um ano para saber se ele é bissexto\ncoloque 0 para ver o ano atual: '))
while Ano > 9999999999999 or Ano < 0
    print('Você precisa digitar um número válido')
    Ano = int(input('Digite um ano para saber se ele é bissexto\ncoloque 0 para ver o ano atual: '))
if Ano == 0:
        Ano = date.today().year
if Ano % 4 == 0 and Ano % 100 != 0 or Ano % 400 == 0:
    print(f'O ano de {Ano} é bissexto!')
else:
    print (f'O ano de {Ano} não é bissexto!')
