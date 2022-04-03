from datetime import date
Ano = int(input('Em que ano você nasceu?: '))
Mês = int(input('Em que mês você nasceu?: '))
Dia = int(input('Em que dia você nasceu?: '))
Idade = date.today().year - Ano + 1 - Mês / 12 - Dia / 365
if Idade < 18:
    print(f'Você tem {Idade:.2f} anos e irá precisar\nse alistar em {Ano + 18}\ndaqui a {18 - Idade:.2f} anos')
elif Idade >= 18 and Idade < 19:
    print('Você já tem 18 anos e precisa se\nalistar imediatamente!')
else:
    print(f'Você tem {Idade:.2f} anos e já deveria\nter se alistado em {Ano + 18}, {Idade - 18:.2f} anos atrás')
