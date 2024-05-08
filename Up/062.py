print('Gerador de PA')
print('=-'*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
tot = 0
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
    tot += 1
print('PAUSA')
num = int(input('Quantos termos você quer mostrar a mais? '))
while num != 0:
    cont = 0
    while cont <= num -1:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
        tot += 1
    print('PAUSA')
    num = int(input('Quantos termos você quer mostrar a mais? '))
print('Progessão finaliza com {} termos mostrados.'.format(tot))