#Usuario vai digitar a quantidade de numeros que desejar e o cotigo vai perguntar se ele deseja continuar
#ao final vai mostrar em ordem crescente o valor e anular os valores repetidos


lista_numeros = [ ]


while True:
    numero = int(input("Digite um valor: "))
    if numero not in lista_numeros:
        lista_numeros.append(numero)
    else:
        print("Valor duplicado")

    resposta = input("Quer continuar? [Y/N]")
    if resposta in "Nn":
        break
lista_numeros.sort()
print(f"Seus numeros",lista_numeros)