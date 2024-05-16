print('=-=' *5,'|PAR OU IMPAR ?|','=-=' *5)
number = int(input('Digite o numero: ').strip())
r = number % 2
if r == 0:
    print('O numero {} é PAR !'.format(number))
else:
    print('O numero {} é IMPAR !'.format(number))


#PAR OR IMPAR ?