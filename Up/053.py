fr = str(input('Digite uma frase: ')).strip().upper()
pl = fr.split()
jt = ''.join(pl)
inv = ''
for letra in range(len(jt) - 1, -1, -1):
    inv += jt[letra]
if inv == jt:
    print('Temos um palídromo!')
else:
    print('A frase digitada não é um palíndromo!')

#inv = jt[::-1]