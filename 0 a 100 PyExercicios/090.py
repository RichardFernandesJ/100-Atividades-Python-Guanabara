#Nome
#Media aluno 

#Nome é igual a 
#media é igual a 
#situação é igual a recuperação 5.1 a 6.9/aprovado =>7/reprovado =<5 


prova = dict()


prova['nome'] = str(input("Nome: "))
prova['media'] = float(input(f"Media do {prova['nome']}: "))
if prova['media'] < 6:
    prova['status'] = 'Reprovado'
elif prova['media'] >= 6 and prova['media'] <= 6.5:
    prova['status'] = 'Recuperação'
else:
    prova['status'] = 'Aprovado'




print("-="*30)
for k, v in prova.items():
    print(f"{k} é igual a {v}")
print("-="*30)