name = str(input('Digite seu nome: ')).strip()
n = name.split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu ultimo nome é {}'.format(n[len(n)-1]))

