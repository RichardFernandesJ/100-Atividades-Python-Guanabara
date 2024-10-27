partida = dict()

partida['nome'] = str(input("Nome do Jogador: "))
qtd_part = int(input(f"Quantas partidas {partida['nome']} jogou? "))

gol = list()


for c, p in enumerate(range(0,qtd_part)):
    gol.append(int(input(f"Quantos gols na partida {c}? ")))

print("=-"*20)
partida['gols'] = gol
partida['total'] = sum(gol)
print(partida)
print("=-"*20)
for k, v in partida.items():
    print(f"O campo {k} tem o valor {v}")
print("=-"*20)
print(f"O jogador {partida['nome']} jogou {qtd_part} partidas.")
for c, v in enumerate(partida['gols']):
    print(f"=> Na partida {c}, fez {v} gols.")
