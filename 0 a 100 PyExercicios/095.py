#atividade 093 aprimorada 

partida = list()


#Vai repetir a solicitação para adicionar o jogador
while True:
    #dicionario onde vai armazenar os dados do jogador
    jogador = dict()
    
    
    #responsavel por limpar a copia do antigo jogador para cadastrar o outro
    jogador.clear()
    

    #vai receber o nome do jogador
    jogador['nome'] = str(input("Nome do Jogador: "))
    #vai receber a quantidade partidas
    qtd_part = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    #lista de gols
    gol = list()

    #laço responsavel por recebe cada gol de cada partida
    for c, p in enumerate(range(0,qtd_part)):
        gol.append(int(input(f"Quantos gols na partida {c}? ")))

    #jogador recebe a lista de gols no dict
    jogador['gols'] = gol
    #soma os gols e recebe o total de gols no dict
    jogador['total'] = sum(gol)
    #contabiliza mais um no contador de id COD
 
    #responsavel por solicitar se o jogar quer continuar cadastrando outro jogador ou não 
    while True:
        resp = input("Quer continuar? [S/N] ").upper()[0]
        #aceita somente as respostas S ou N, diferente disso vai informar o erro e solicitar uma nova resposta
        if resp in 'SN':
            break
        print("ERRO! Digite uma letra valida entre S ou N !")
    #copia o jogador e adiciona na lista de partida através do append
    partida.append(jogador.copy())
    #resp sendo N para de add novos jogadores
    if resp == 'N':
        break

#laço responsavel por exibir a lista de jogadores, utilizei a da correção.
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f"{i:<15}",end='')
print()
print('-='*30)
for k, v in enumerate(partida):
    print(f"{k:<4}",end='')
    for d in v.values():
        print(f"{str(d):<15}",end='')
    print()
print('-='*30)


#repetição reponsavel por abrir o detalhe de partida de cada jogador informado através da id COD.
while True:
    resp = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    #fim do codigo 
    if resp == 999:
        print("Finalizado....")
        break
    if resp >= len(partida):
        print("ERRO ! Digite um COD valido !")
    #Imprime o levantamento dos jogadores mostrando qual partida marcou cada quantidade de gols.
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {partida[resp]['nome']}")
        for p, g in enumerate(partida[resp]['gols']):
            print(f"   No jogo {p} fez {g} gols.")
#fim do codigo 

