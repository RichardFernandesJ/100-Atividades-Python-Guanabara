from datetime import datetime
print('-='*13)
print('QUAL A CATEGORIA DO ATLETA ')
print('-='*13)
ano = int(input('Informe o Ano de Nascimento: ').strip())
idade = datetime.now().year - ano
print('O atleta tem {} anos.'.format(idade))
if idade > 0 and idade < 9:
    print('Classificação: MIRIM')
elif idade >= 9 and idade < 14:
    print('Classificação: INFANTIL')
elif idade >= 14 and idade < 19:
    print('Classificação: JUNIOR')
elif idade >= 19 and idade < 25:
    print('Classificação: SÊNIOR')
elif idade >= 25:
    print('Classificação: MASTER')

#PROFESSOR FEZ DA SEGUINTE FORMA
#IF IDADE <=9:
    #PRINT('....')
# ELIF IDADE <=14:
    # PRINT('....')
# ELIF IDADE <=19:
    # PRINT('....')
# ELIF IDADE <=25:
    # PRINT('....')
#ELSE:
    #PRINT('......')
