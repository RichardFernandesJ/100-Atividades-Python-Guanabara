import random
print('{:=^20}'.format(' JOKENPO '))
op = int(input('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA
Qual é a sua jogada ? '''))
print('''JO
KEN
PO !!''')
print('=-'*15)
joken = random.randint(0,2)
if joken == 0:
    print('Computador jogou PEDRA !')
elif joken == 1:
    print('Computador jogou PAPEL !')
elif joken == 2:
    print('Computador jogou TESOURA !')
if op == 0:
    print('Jogador jogou PEDRA !')
elif op == 1:
    print('Jogador jogou PAPEL !')
elif op == 2:
    print('Jogador jogou TESOURA !')
print('=-'*15)
jog = op
cup = joken
if jog == 0 and cup == 2 or jog == 1 and cup == 0 or jog == 2 and cup == 1:
    print('JOGADOR VENCE !')
elif jog == cup:
    print('OCORREU UM EMPATE')
else:
    print('COMPUTADOR VENCE !')

#professor utilizou outra forma para realizar a tarefa começando por colocar os itens em variaveis
#como itens = ('pedra', 'papel', 'tesoura')
# computador = randint(0,2) professor importou somente o modulo randint
# e na string o .format foi feito da seguinte forma
#.format(itens[computador])