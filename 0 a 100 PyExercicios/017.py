import math
co = int(input('Informe o cateto oposto:'))
ca = int(input('Informe o cateto adjacente:'))
n1 = co ** 2
n2 = ca ** 2
c = (n1 + n2)
hip = math.sqrt(c)
print('O Comprimeito a Hipotenusa é de {} cm'.format(hip))

