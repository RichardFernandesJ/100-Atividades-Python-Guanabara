maP = 0
meP = 0
for p in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maP = peso
        meP = peso
    else:
        if peso > maP:
            maP = peso
        if peso < meP:
            meP = peso
print('O maior peso lido foi de {}Kg !'.format(maP))
print('O menor peso lido foi de {}Kg !'.format(meP))