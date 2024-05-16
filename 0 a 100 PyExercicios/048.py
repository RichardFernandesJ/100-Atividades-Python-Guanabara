t = 0
tot = 0
for count in range(1, 501, 2):
    if count % 3 == 0:
        tot += count
        t += 1
print(tot)
print('A soma total dos {} numeros multiplos de três é {}'.format(t, tot))