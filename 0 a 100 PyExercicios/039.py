from datetime import datetime
print('-'*10)
print('CENTRAL SERVIÇO MILITAR')
print('-'*10)
ano = int(input('Informe seu ano de nascimento: ').strip())
anoa = datetime.now().year
id = anoa - ano
temp = 18 - id
tempp = id - 18
if id == 18:
    print('Esta na hora de se alistar !')
    print('Realize o Alistamento através do nosso site http://juntamilitarmg.gov')
elif id < 18:
    print('Esta quase na hora de se alistar no SERVIÇO MILITAR !')
    print('Falta {} anos para se Alistar!'.format(temp))
elif id > 18:
    print('Passou do tempo de alistamento !')
    print('Ja se passou {} anos para seu alistamento !'.format(tempp))
