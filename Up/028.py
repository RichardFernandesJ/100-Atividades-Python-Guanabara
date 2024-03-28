import random
collor = {'amarelo':'\033[33m',
          'vermelho':'\033[31m',
          'clear':'\033[m',
          'negrito':'\033[1m'}

print('\033[31m''========BLAZE==========''\033[m')
print('Bip..Bop...Bip..')
print('Estou pensando em um numero !')
print('Você acha que consegue advinhar qual ?')
print('Bip....°°')
print('\033[31m''========BLAZE==========''\033[m')
resp = str(input('Sim ou Não: ')).strip().upper()
if resp == 'SIM':
    print('Então Vamos lá!')
    print('Bip....Boop..!')
    num = random.randint(0, 5)
    print('Agora é sua vez de responder')
    blaze = int(input('Qual numero eu pensei de 0 a 5 ? '))
    if blaze == num :
        print('Eitcha ! Você acertou eu estava pensando no numero {} !'.format(num))
    else:
        print('Você errou ! Bipp...Bopp..')
else:
    print('Ja correu ! Bipp...Boopp..')
#Meu cassininho
