print('='*10)
print('Richaelo')
print('='*10)
val = float(input('Digite o valor das compras: R$').strip())
print('FORMAS DE PAGAMENTO')
print('''[ 1 ] á vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual é a opção ? '))
if op == 1:
    tot = val - ((val * 10)/100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(val, tot))
elif op == 2:
    tot = val - ((val * 5)/100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(val, tot))
elif op == 3:
    tot = val / 2
    print('Sua compra de R${:.2f} dividida de 2x no cartão vai sair a {:.2f} cada parcela.'.format(val, tot))
elif op == 4:
    plas = int(input('Quantas Parcelas ?').strip())
    if plas >= 3 and plas <= 12:
        totj = val + ((val * 20) / 100)
        totp = totj / plas
        print('Sua compra será parcelada em {}x de R${:.2f} com JUROS'.format(plas, totp))
        print('Sua compra de RS${:.2f} vai custar R${:.2f} no final.'.format(val, totj))
    elif plas < 3:
        print('''Para parcelas menores que 3x 
Selecione a opção anterior opção [ 3 ] !''')
    else:
        print('Nesta maquininha não é possivel dividir mais de 12x no cartão.')
else:
    print('\033[31m''ESTA OPÇÃO NÃO EXISTE, TENTE NOVAMENTE. ')

    #Dei uma implementada coloque uma cor vermelha na linha 33 para fazer mais jus a opção invalida

