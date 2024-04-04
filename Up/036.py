print('=-'*10)
print('EMPRÉSTIMO BANCÁRIO')
print('=-'*10)
val = int(input('Informe o valor da Casa: R$').strip())
sal = int(input('Informe o salário do comprador: R$').strip())
anos = int(input('Quantos anos de Financiamento? ').strip())
tot = (sal * 30) / 100
mes = (12 * anos)
toth = val / mes
print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}!'.format(val, anos, toth))
if toth > tot:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')