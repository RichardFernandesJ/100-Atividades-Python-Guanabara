m = 0
while m != 5:
    n1 = int(input('Primeiro numero: '))
    n2 = int(input('Segundo numero: '))
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR NUMERO DIGITADO')
    print('[ 4 ] NOVOS NÚMEROS')
    print('[ 5 ] SAIR DO PROGRAMA')
    m = int(input('>>> Qual é a sua opção? '))
    if m == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}.'.format(n1, n2, soma))
        print('-='*20)
    if m == 2:
        soma = n1 * n2
        print('A multiplicação entre {} x {} é {}.'.format(n1, n2, soma))