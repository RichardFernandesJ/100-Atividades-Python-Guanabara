from random import randint


def sorteioNumeros(lista):

    for cont in range(0, 5):
        numero = randint(1,10)
        lista.append(numero)


    print(f"Sorteando 5 valores da lista: ", end='')
    for valor in lista:
        print(valor, end=' ')
    print("PRONTO!")
    


def somarPares(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
           soma += valor
    print(f"Somando os valores pares de {lista}, temos {soma}")


numeros = list()
sorteioNumeros(numeros)
somarPares(numeros)