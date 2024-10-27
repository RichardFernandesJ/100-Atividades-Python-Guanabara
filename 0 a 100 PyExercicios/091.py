from random import randint
from time import sleep
from operator import itemgetter

dict_game = {'jogador1': randint(1,7),
    'jogador2': randint(1,7),
    'jogador3': randint(1,7),
    'jogador4': randint(1,7)

} 

ranking = list()

print("------VALORES SORTEADOS------")
for k, v in dict_game.items():
    print(f"{k} tirou {v} no dado")
    sleep(0.5)
ranking = sorted (dict_game.items(), key=itemgetter(1), reverse=True)

c = 0

#for k, v in enumerate(ranking):
#print(f"{k}° lugar: {v[0]} com {v[1]}.")


print("------RANKING------")
for k, v in ranking:
    c += 1
    print(f"{c}° lugar: {k} com {v}.")
    sleep(0.5)