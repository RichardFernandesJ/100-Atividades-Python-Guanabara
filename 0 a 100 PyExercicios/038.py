n1 = int(input('Digite o primeiro numero: ').strip())
n2 = int(input('Digite o segundo numero: ').strip())
if n1 > n2:
    print('O primeiro valor que seria {} é maior.'.format(n1))
elif n1 < n2:
    print('O Segundo valor que seria {} é maior.'.format(n2))
elif n1 == n2:
    print('Não existe maior valor, os dois valores são iguais {} '.format(n1),end='')
    print('e {} !'.format(n2))

