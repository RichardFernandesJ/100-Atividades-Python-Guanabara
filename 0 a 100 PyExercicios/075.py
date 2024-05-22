n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o ultimo número: '))
num = (n1, n2, n3, n4)
count = 0
nine = 0
print(f'Você digitou os valores {num}')
for c in num:
    if c == 9:
        nine+=1
print(f'O Valor 9 apareceu {nine} vezes')
for pos, c in enumerate(num):
    if 3 == c:
        print(f'O Valor 3 apareceu na {pos+1}° posição')
for c in num:
    if c % 2 == 0:
        count+=1
print(f'Os valores pares digitados foram {count}')



#A Tupla o professor fez da seguinte forma 
#núm = (int(input('Digite um número: ')),int(input('Digite outro número: ')),int(input('Digite mais um número: ')),int(input('Digite o ultimo número: '))
#print(f'Você digitou os valores {núm}')
#print(f'O valor 9 apareceu {núm.count(9)} vezes')
#if 3 in núm:
    #print(f'O Valor 3 apareceu na {núm.index(3+1)° possição}')
#else:
    #print('O valor 3 não foi digitado em nenhuma possição')
#print('Os valores pares digitados foram', end='')
#for n in núm:
    #if n % 2 == 0:
        #print(n end='')