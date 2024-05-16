peso = float(input('Qual é o peso ? (KG) '))
alt = float(input('Qual é a altura ? (M) '))
imc = peso / (alt ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você esta abaixo do Peso !')
elif imc <= 25:
    print('Você esta no peso ideal PARABÉNS !')
elif imc <= 30:
    print('Você esta acimda do peso ideal SOBREPESO !')
elif imc <= 40:
    print('Você esta muito acimda do peso ideal OBESO ')
else:
    print('Você se encontra em OBESIDADE MÓRBIDA !')