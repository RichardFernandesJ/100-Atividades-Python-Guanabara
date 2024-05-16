print('= '*10)
print('BANCO ELIT')
print('= '*10)
valsac = int(input('Que valor você quer sacar? R$'))
#cedulas = 50, 20, 10, 1
#1000 16 / 50 
total = valsac
cedula = 50
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'Total de {totcedula} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
            break

print('= '*10)
print('Volte sempre ao BANCO ELIT! Tenha um bom dia !') 
