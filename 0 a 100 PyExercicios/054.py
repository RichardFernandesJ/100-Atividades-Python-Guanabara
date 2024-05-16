from datetime import datetime
data = datetime.now().year
c = 0
mID = 0
meID = 0
for count in range(0, 7):
    c = count + 1
    ano = int(input('Em que ano a {}ª pessoa nasceu ? '.format(c)))
    if (data - ano) >= 21:
        mID += 1
    else:
        meID += 1
print('Ao todo tivemos {} pessoa maiores de idade.!'.format(mID))
print('E também tivemos {} pessoas menores de idade.!'.format(meID))