#Utilizado pare receber o valor
valor = 0
#Uma lista com duas listas internas onde uma vai receber os numeros pares e a outra os numeros impares
numeros = [[], []]
#contador poderia utilizar o range 1,8 ja que anula o ultimo numero 
p = 0

for c in range(0,7):
    p += 1
    valor = int(input(f"Digite o {p}° valor: "))
    if valor % 2 == 0:
        #append feito dentro da lista numeros na sub lista [0]
        numeros[0].append(valor)
    else:
        #append feito dentro da lista numeros na sub lista [1]
        numeros[1].append(valor)
#.sort em cada sublista para não juntar todas. Desta forma os numeros vão ficar em ordem
numeros[0].sort()
numeros[1].sort()
print("Os valores pares digitados foram: ",numeros[0])
print("Os valores ímpares digitados foram: ",numeros[1])
