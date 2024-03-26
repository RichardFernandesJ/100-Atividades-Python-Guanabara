import math
ang = int(input('Informe o Ângulo: '))
rad = math.radians(ang)
seno = math.sin(rad)
coss = math.cos(rad)
tang = math.tan(rad)
print('O Valor de Seno é {:.2}, o valor de Cosseno é {:.2}, a Tangente do angulo de {} é {:.2}'.format(seno, coss, ang, tang))