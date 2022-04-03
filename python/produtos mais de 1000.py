ProdutoMenor = PreçoMenor = Total = Mais = Contador = 0
while True:
    Produto = input('Digite o nome do produto:\n')
    Preço = float(input('Quanto foi o produto:\n'))
    Total += Preço
    Contador += 1
    if Preço > 1000:
        Mais += 1
    if Contador == 1 or Preço < PreçoMenor:
        PreçoMenor = Preço
        ProdutoMenor = Produto
    Continuar = str(input('Quer continuar? [S/N]:\n')).strip().upper()[0]
    if Continuar == 'S':
        Nada = 0
    else:
        break
print(f'Você gastou {Total:.2f}R$\n{Mais} produtos custam mais de 1000.00R$\nO produto mais barato foi {ProdutoMenor} custando {PreçoMenor}R$.')
    