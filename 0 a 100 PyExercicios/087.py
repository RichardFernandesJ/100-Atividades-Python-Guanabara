matriz = [[0 ,0 ,0], [0 ,0 ,0], [0 ,0 ,0]]
mai = soma_par = 0
pares = []



for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para [{l},{c}]: "))
        if matriz[l][c] % 2 == 0:
            pares.append(matriz[l][c])
soma_terceira_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
#for l in range(0,3):
#soma_terceira_coluna += matriz[l][2]
for par in pares:
     soma_par = soma_par + par

print("*=" * 30)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end='')
    print()

for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
     
print()
print(f"A soma dos valores pares é {soma_par}.")
print(f"A soma dos valores a terceira coluna é {soma_terceira_coluna}.")
print(f"O maior valor da segunda linha é {mai}.")