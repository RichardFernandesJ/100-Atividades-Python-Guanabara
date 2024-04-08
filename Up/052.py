num = int(input('Digite um número: '))
tot = 0
for count in range(1,num+1):
    if num % count == 0:
        print('\033[33m',end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(count),end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('É um numero primo !')
else:
    print('Não é um numero primo !')