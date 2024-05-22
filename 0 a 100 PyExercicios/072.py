ext = ('Zero', 'Um', 'Dois','Três','Quatro','Cinco','Seis',
       'Sete','Oito','Nove','Dez','Onze','Doze','Treze','catorze',
       'Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    while True:
        num = int(input('Digite um numero entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        else:
            print('Numero invalido digite novamente! ', end='')
    print(f'Você digitou o número {ext[num]}')
    resp = str(input('Você quer continuar [ S / N ] ? ')).strip()[0].upper()
    if resp == 'N':
        print('Saindo...')
        break
    else:
        print('Informe um novo numero !')