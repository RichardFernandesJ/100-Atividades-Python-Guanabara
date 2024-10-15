boletim = []

while True:
    aluno = []
    aluno.append(str(input("Nome: ")))
    aluno.append(float(input("Nota 1: ")))
    aluno.append(float(input("Nota 2: ")))
    boletim.append(aluno)
    resposta = str(input("Quer continuar? [S/N] ").upper())
    if resposta == 'N':
        break
print("=-"*30)
print(f"{"No.":<4} {"NOME":<10}        {"MÉDIA":>8}")
print("--"*30)

for p,l in enumerate(boletim): 
    n1 = boletim[p][1]
    n2 = boletim[p][2]
    media = n1 + n2
    print(f"{p:<4}     {boletim[p][0]:<10}     {media:>8.1f}")

while True:
    search_aluno = int(input("Mostrar notas de qual aluno:  (press 999 para sair): "))
    print(f"Notas de {boletim[search_aluno][0]} são {boletim[search_aluno][1], boletim[search_aluno][2]}")
    print("-="*20)
    if search_aluno == 999:
        print("Saindo.....")
        break

