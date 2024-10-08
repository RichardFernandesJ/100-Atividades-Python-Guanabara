lista_numeros= []

for count in range(0,5):
    numero = (input("Digite um numero: "))
    if count == 0 or numero > lista_numeros[-1]:
        lista_numeros.append(numero)
        print("Adicionando ao final da lista...")
    else:
        pos = 0 
        while pos < len(lista_numeros):
            if numero <= lista_numeros[pos]:
                lista_numeros.insert(pos, numero)
            print(f"Adicionado na posição {pos} da lista...")
            break
        pos += 1
print("=*" * 30)
print(f"Os valores digitados em ordem foram {lista_numeros}")

       
