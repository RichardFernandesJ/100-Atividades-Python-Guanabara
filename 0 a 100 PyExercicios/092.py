cadastro = dict()
from datetime import datetime

cadastro['nome'] = str(input("Nome: "))
cadastro['nascimento'] = int(input("Ano de Nascimento: "))
idade = datetime.now().year - cadastro['nascimento']
cadastro['idade'] = idade



cadastro['carteira_trabalho'] = int(input("Carteira de Trabalho (0 não tem): "))
for i in range(1):
    if cadastro['carteira_trabalho'] != 0:
        cadastro['contratacao'] = int(input("Ano de Contratação: "))
        cadastro['salario'] = float(input("Salário: R$"))
        #35 anos trabalhados para aposentar 
        anos_trabalhados = cadastro['contratacao'] - datetime.now().year
        aposentar = int(35)
        aposentadoria = aposentar - anos_trabalhados
        cadastro['aposentadoria'] = aposentadoria
    else:
        break

print("=-" * 30)

for k, v in cadastro.items():
    print(f"- {k} tem o valor {v}")


##### fim do codigo 