from time import sleep
m = 0
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
while m != 5:
    print('=-='*14)
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR NUMERO DIGITADO')
    print('[ 4 ] NOVOS NÚMEROS')
    print('[ 5 ] SAIR DO PROGRAMA')
    m = int(input('>>> Qual é a sua opção? '))
    if m == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}.'.format(n1, n2, soma))
    if m == 2:
        soma = n1 * n2
        print('A multiplicação entre {} x {} é {}.'.format(n1, n2, soma))
    if m == 3:
        if n1 > n2:
            print('O maior numero digitado foi {}.'.format(n1))
        else:
            print('O maior numero digitado foi {}.'.format(n2))
    if m == 4:
        print('Informe os numero novamente:')
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo numero: '))
    if m == 5:
        print('Finalizando...')
        sleep(1)
        print('=-='*14)
        print('Fim do programa! Volte sempre!')
    if m > 5 or m < 1:
        print('Opção inválida. Tente novamente.')

