import random
a1 = str(input('primeiro aluno:'))
a2 = str(input('segundo alundo:'))
a3 = str(input('terceiro aluno:'))
a4 = str(input('quarto aluno:'))
lista = [a1,a2,a3,a4]
escolhido = random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))
