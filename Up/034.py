print('Calculadora de Aumento Salarial')
sal = float(input('Informe o salario: '))
if sal > 1250:
    tots = (sal * 10) / 100
    print('Aumento de 10%')
    print('O aumento do seu salario será de {} totalizando {} !'.format(tots, sal+tots))
else:
    tots = (sal * 15) / 100
    print('Aumento de 15%')
    print('O aumento do seu salario será de {} totalizando {} !'.format(tots, sal +tots))
