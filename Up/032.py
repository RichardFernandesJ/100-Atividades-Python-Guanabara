from datetime import date
print('-' * 5,'|ANO BISSEXTO ?|','-' * 5)
year = int(input('Informe o Ano que deseja analisar ou digite 0 para analisar o ano atual:').strip())
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year% 400 == 0:
    print('Este ano é bissexto!')
else:
    print('Este ano não é bissexto')

# F
