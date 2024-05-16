c = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor ? '))
    print('-'*38)
    if n < 0:
        break
    while c < 10:
        c+= 1
        result = n * c
        print(f'{n:^3} x {c:^3} = {result:^3}')
    print('-'*38)
    c = 0
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
