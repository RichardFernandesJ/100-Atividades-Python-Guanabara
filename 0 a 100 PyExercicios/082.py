lista_numeros = []
numeros_pares = []
numeros_impares = []
while True:
    lista_numeros.append(int(input("Digite um numero:")))
    resp= str(input("Quer continuar ? [S/N]").upper())
    if resp == "N":
        break
for numero in lista_numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)
print("A lista completa é",lista_numeros)
print("A lista de pares é ",numeros_pares)
print("A lista de ímpares é ",numeros_impares)