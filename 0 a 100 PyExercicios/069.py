MaiorId = CadH = CadM = 0
while True:
    print('=-'*20)
    print('CADASTRE UMA PESSOA')
    print('=-'*20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    if idade >= 18:
        MaiorId += 1
    if sexo == 'F':
        CadH += 1
    if idade < 20 and sexo == 'F':
        CadM += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('=-'*20)
print('FIM DO PROGRAMA')
print('=-'*20)
print(f'Total de pessoas com mais de 18 anos: {MaiorId}')
print(f'Ao todo temos {CadH} Homens Cadastrados')
print(f'Temos {CadM} mulheres com menos de 20 anos')