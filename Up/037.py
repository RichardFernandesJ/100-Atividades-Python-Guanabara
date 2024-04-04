print('=-'*10)
print('BASE CONVERTER 1.0')
print('=-'*10)
number = int(input('Digite um número inteiro: ').strip())
print('|Escolha uma das bases para conversão|')
print('[ 1 ] Converter para BINÁRIO')
print('[ 2 ] Converter para OCTAL')
print('[ 3 ] Converter para HEXADECIMAL')
op = int(input('Sua opção: ').strip())
if op == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(number, bin(number)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(number, oct(number)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(number, hex(number)[2:]))
else:
    print('ESTA OPÇÃO É INVALIDA. TENTE NOVAMENTE.')