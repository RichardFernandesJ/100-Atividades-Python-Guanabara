from random import randint
c = 0
pite = ''
numb = randint(0, 10)
print('Sou seu computador..')
print('Acabei de pensar em um número entre 0 a 10.')
print('Será que você consegue advinhar qual foi ?')
if pite != numb:
    while pite != numb:
        pite = int(input('Qual é seu palpite? ').strip())
        if pite == numb and c == 0:
            print('Você acertou de primeira o numero escolhido foi {} !'.format(numb))
        if numb < pite:
            print('Menos... Tente outra vez.')
        if numb > pite:
            print('Mais.. Tente outra vez.')
        c += 1
        if pite == numb:
            print('Você acertou com {} tentativas. Parabéns !'.format(c))

