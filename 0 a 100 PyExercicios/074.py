from random import randint

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), 
           randint(0, 10), randint(0, 10))
mVal = sorted(numeros)
print(f'Os valores sorteados foram : {numeros}')
print(f'O maior valor sorteado foi {mVal[4]}')
print(f'O menor valor sorteado foi {mVal[0]}')


#Forma realizada pelo professor.
#for n in numeros:
    #print(f'{n}', end='')
#print(f'\nO maior valor sorteado foi {max(numeros)}')
#print(f'\nO menor valor sorteado foi {min(numeros)}')
