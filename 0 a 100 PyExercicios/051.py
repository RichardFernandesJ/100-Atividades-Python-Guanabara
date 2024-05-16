print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
pr = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
dec = pr + (10 - 1) * ra
for count in range(pr, dec + ra, ra):
    print(count, end='-> ')
print('Acabou')