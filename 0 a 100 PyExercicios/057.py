sexo = ''
sexo = str(input('Digite seu sexo [M/F] : ').upper().strip())
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ').upper().strip())
print('Sexo {} registrado com sucesso.'.format(sexo))
