c = 0
soma = 0
while True:
    val = int(input('Digite um valor (999 para parar): '))
    if val == 999:
        break
    c += 1
    soma += val
print(f'A soma dos {c} valores foi {soma}! ')

