
lista_numeros = []
maior_numero = 0
menor_numero = 0
for cont in range(0, 5):
    lista_numeros.append(int(input("Digite um valor: ")))
    if cont == 0:
        maior_numero = menor_numero = lista_numeros[cont]
    else: 
        if lista_numeros[cont] > maior_numero:
            maior_numero = lista_numeros[cont]
        if lista_numeros[cont] < menor_numero:
            menor_numero = lista_numeros[cont]
print(f"Sua lista = {lista_numeros}")
print(f"O maior valor digitado foi {maior_numero} nas posições ", end='')
for p, numero in enumerate(lista_numeros):
    if numero == maior_numero:
        print(f"{p}..", end='')
print()
print(f"O menor valor digitado foi {menor_numero} nas posições ", end='')
for p, numero in enumerate(lista_numeros):
    if numero == menor_numero:
        print(f"{p}..", end='')

