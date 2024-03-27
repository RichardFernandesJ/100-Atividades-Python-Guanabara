print('=-=' * 5 ,'|Radar|','=-=' * 5)
velo = int(input('Informe a velocidade do carro: ').strip())
if velo > 80:
    print('Você foi multado por excesso de velocidade !')
    print('Passou em uma via de 80 Km/h a {}Km/h !'.format(velo))
    print('A multa vai custar R$ 7,00 por cada Km acima do limite.')
    r = velo - 80
    multa = r * 7
    print('Seu total de multa vai ser de R${:.2f}'.format(multa))
else:
    print('Você não foi multado!')

#Radar 