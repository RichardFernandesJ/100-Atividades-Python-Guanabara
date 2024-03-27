city = str(input('Informe o nome da cidade: ')).strip()
print('Esta cidade começa com (SANTO) ? True = Sim / False = Não ')
print('{}'.format('SANTO' in city[:5].upper()))

#print(city[:5].upper() == 'Santo')