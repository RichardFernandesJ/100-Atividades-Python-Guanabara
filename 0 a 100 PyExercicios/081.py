lista_numeros = []
elementos = 0

while True:
    lista_numeros.append(input("Informe um numero: "))
    resposta = input("Deseja continuar ? [S/N]").lower()
    elementos += 1
    if (resposta == "n"):
        break
lista_numeros.sort(reverse=True)
#Podendo utilizar somente o {len(lista_numeros)}
print(f"Foram digitados {elementos} elementos.")
print(f"Os valores em orde decrescente são {lista_numeros}")
numero5 = 0
for numeros in lista_numeros:
    if numeros == '5':
        numero5 += 1
if numero5 > 0:
    print("O valor 5 faz parte da lista!")
else:
    print("O Valor 5 não foi encontrado na lista")