from random import shuffle
a1 = str(input('Qual o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
list = [a1, a2, a3, a4]
shuffle(list)
print('A Ordem de apresentação será')
print(list)