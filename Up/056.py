mvel = 0
nvel = ''
mID = 0
mm = 0
for p in range(1,5):
    print('='*6,p,'ª PESSOA','='*6)
    nome = str(input('Digite o Nome: ').strip())
    idade = int(input('Digite a Idade: ').strip())
    sexo = str(input('Informe o Sexo [M/F]: ').upper().strip())
    mID += idade
    if idade < 20 and sexo == 'F':
        mm += 1
    elif idade > mvel:
        nvel = nome
        mvel = idade
    print(mm)
media = mID / 4
print('A média de idade do grupo é de {:.1f} anos.'.format(media))
print('O mais velho tem {} e se chama {}.'.format(mvel, nvel))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mm))