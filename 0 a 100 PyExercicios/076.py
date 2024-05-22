tabela_preços = ('Lápis', 1.75,'Borracha', 2.00, 'Caderno', 15.90, 
                 'Estojo', 25.00,'Transferidor',4.20, 'Compasso', 9.99, 
                 'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)
print('---'*20)
print(f'{'TABELA DE PREÇOS':^60}')
print('---'*20)
for item in range(0, len(tabela_preços)):
    if item % 2 == 0:
        print(f'{tabela_preços[item]:.<48}', end= '')
    else:
        print(f'R${tabela_preços[item]:>10.2f}')
print('---'*20)

