TotC = TotM = c = 0
MVal = ' '
MPre = 0

print('--'*20)
print('LOJA SUPER BARATÃO')
print('--'*20)
while True:
    prod = str(input('Nome do Produto: ')).strip()
    val = float(input('Preço: '))
    c += 1
    TotC += val
    if c == 1:
        MPre = val
    if val > 1000:
        TotM += 1
    if val < MPre:
        MPre = val
        Mval = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('--'*20)
print('FIM DO PROGRAMA')
print('--'*20)
print(f'O Total da compra foi {TotC:.2f}')
print(f'Temos {TotM} produtos custando mais de R$1000.00')
print(f'O Produto mais barato foi {Mval} que custa R${MPre:.2f}')
