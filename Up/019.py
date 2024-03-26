from random import choice
al1 = input('Informe o nome do aluno: ')
al2 = input('Informe o nome de outro aluno: ')
al3 = input('Informe o nome de mais um aluno: ')
al4 = input('Informe o nome do ultimo aluno: ')
list = [al1, al2, al3, al4]
select = choice(list)
print('O aluno escolhido foi {}'.format(select))




