num = c = soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    soma = soma + num
    #CONTADOR DE NUMEROS DIGITADOS
    c += 1
    if num == 999:
        soma = soma - num
        c = c - 1

print('Você digitou {} números e a soma entre eles foi de {}.'.format(c, soma))