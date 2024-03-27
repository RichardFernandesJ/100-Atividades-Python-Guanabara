import random
print('========BLAZE==========')
print('Bip..Bop...Bip..')
print('Estou pensando em um numero !')
print('Você acha que consegue advinhar qual ?')
print('Bip....°°')
print('========BLAZE==========')
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
