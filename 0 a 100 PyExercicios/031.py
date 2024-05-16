print('=-=' * 5 ,'|Buser|', '=-=' * 5)
dist = float(input('Informe a distancia da viagem em Km :').strip())
if dist <= 200:
    r = 0.50 * dist
    print('Esta viagem tem menos de 200 Km,')
    print('será cobrado R$0,50 por Km !')
    print('O preço da passagem é de R${} !'.format(r))
else:
    r = 0.45 * dist
    print('Esta viagem tem mais de 200 Km,')
    print('será cobrado R$0,45 por Km !')
    print('O preço da passagem é de R${} !'.format(r))

