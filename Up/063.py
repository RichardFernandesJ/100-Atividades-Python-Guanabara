n = int(input('Quantos termos você quer mostrar ? '))
ter1 = 0
ter2 = 1
print('=-'*20)
print('{} -> {}'.format(ter1, ter2), end='')
cont = 3
while cont <= n:
    ter3 = ter1 + ter2
    print(' -> {}'.format(ter3), end='')
    ter1 = ter2
    ter2 = ter3
    cont += 1
print(' FIM')
print('=-'*20)
