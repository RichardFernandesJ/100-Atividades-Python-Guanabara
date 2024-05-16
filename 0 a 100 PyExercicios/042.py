print('-u'*20)
print('Analisador de Triângulo')
print('-u'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1+ r3 and r3 < r2 + r1:
    print('Os segmentos podem formar um triangulo !')
    if r1 == r2 and r2 == r3:
        print('Podem formar um triangulo EQUILÁTERO !')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Podem formar um triangulo ISÓSCELES !')
    elif r1 > r2 or r2 > r3 or r3 > r1:
        print('Podem formar um triangulo ESCALENO !')

else:
    print('Os segmentos não podem formar um triangulo !')

#no escaleno o professor utilizou uma forma diferente
# elif r1 != r2 != r3 != r1:    utilizando por sua vez o != simbolo de diferença em python