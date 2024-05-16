line = str(input('Digite uma frase: ')).strip().upper()
print('A Letra A aparece {} vezes !'.format(line.count('A')))
print('A letra A aparace primeiro na posição {} !'.format(line.find('A')+1))
print('A Ultima letra A apareceu na posição {}'.format(line.rfind('A')+1))