from random import randint
lista_jogos = list()
qtd = int(input("Quantos jogos vocÊ quer que eu sorteie ? "))
print(f"======= SORTEANDO {qtd} JOGOS =======")
qtd += 1
for c in range(1,qtd):
    jogos = []
    for j in range(1,7):
        num = randint(1,60)
        if num not in jogos:
            jogos.append(num)
    lista_jogos.append(jogos)
    jogos.sort()
c= 0 
for jogos in lista_jogos:
    c += 1
    print(f"Jogo {c}: ",jogos)
print("======== <BOA SORTE! > =========")
