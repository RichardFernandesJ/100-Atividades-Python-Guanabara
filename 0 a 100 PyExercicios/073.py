tabela = ('Athletico-PR', 'Bahia', 'Flamengo', 'Botafogo', 'São Paulo', 
          'Cruzeiro', 'Atletico MG', 'Bragantino', 'Palmeiras', 'Internacional', 
          'Fortaleza', 'Grêmio', 'Vasco da Gama', 'Criciúma', 'Juventude', 'Corinthians', 
          'Fluminense', 'Vitoria', 'Atletico GO', 'Cuiabá')
print('=-'*40)
print(f'Lista de times do Brasileirão {tabela}')
print('=-'*40)
print(f'Os 5 primeiros são {tabela[0:5]}')
print('=-'*40)
print(f'Os 4 últimos são {tabela[16:20]}')
print('=-'*40)
print(f'Times em ordem alfabética {sorted(tabela)}')
print('=-'*40)
print(f'O {tabela[6]} está na {tabela.index('Atletico MG')}° possição')