nt1 = float(input('Digite a primeira nota: ').strip())
nt2 = float(input('Digite a segunda noda: ').strip())
m1 = (nt1 + nt2) / 2
print('A Media foi de {:.1f}'.format(m1))
if m1 <= 5.0:
    print('REPROVADO')
elif m1 >= 5.0 and m1<= 6.9:
    print('RECUPERAÇÃO')
elif m1 >= 7.0:
    print('APROVADO')