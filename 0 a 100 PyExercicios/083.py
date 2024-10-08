#Digite uma expressão!
expressao = list()
barra_abertura = []
barra_fechamento = []
expressao.append(input("Digita uma expressão: "))

for barra in expressao:
    for b in barra:
        if b == "(":
            barra_abertura.append(b)
        elif b == ")":
            barra_fechamento.append(b)
if len(barra_abertura) == len(barra_fechamento):
    print("Sua expressão esta valida!")
else:
    print("Sua expressão esta invalida!")
