c = 0
numb = 0
for count in range(1, 7):
    num = int(input('Digite o °{} numero: '.format(count)))
    if num % 2 == 0:
        numb += num
        c += 1
if c == 1:
    print('Foi informado {} numero PAR e a soma deste numero par digitado foi de {} sendo ele mesmo.'.format(c, numb))

else:
    print('Foi informado {} numeros PARES e a soma dos numeros pares digitados foi de {}.'.format(c, numb))

