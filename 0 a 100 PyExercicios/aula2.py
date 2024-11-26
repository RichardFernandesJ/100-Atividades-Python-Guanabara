#interactive help
#help(input)

#docstrings
#'''text'''

#Parâmetro opcionais
#def somar(a=0, b=0, c=0)
#no caso se não houver valor informado vai preencher com o 0

#Escopo De Variaveis
#Escopo local e global
#Dentro da função seria a variavel local e declarada no progrma principal variavel global

#Retornando valores
#return 
# def somar(a=0, b=0, c=0):
    #s = a + b + c
    #return s
#r1 = somar(3, 2, 5)
#r2 = somar(2, 2)
#r3 = somar(6)
#print(f"Os resultados foram {r1} {r2} {r3}")

valores = [3,5,6]
count = 0
for valor in valores:
    count += 1
    print(valor)
total = count
print("==_"*10)
print(total)