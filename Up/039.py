from datetime import datetime
print('-'*10)
print('CENTRAL SERVIÇO MILITAR')
print('-'*10)
ano = int(input('Informe seu ano de nascimento: ').strip())
anoa = datetime.now().year
id = anoa - ano
print(id)
if id == 18:
    print('Esta na hora de se alistar !')
elif id < 18:
    print('Esta quase na hora de se alistar no SERVIÇO MILITAR !')
elif id > 18:
    print('Passou do tempo de alistamento !')
