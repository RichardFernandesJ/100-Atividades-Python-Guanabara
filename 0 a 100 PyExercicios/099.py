#import somente o sleep vai ser utilizado somente uma vez no codigo
from time import sleep

#função declarada somente para imprimir a linha
def linha():
    print("=~"*30)

#função maior responsavel pelo maior numero
def maior_numero(*valores):
    linha()
    print("Analisando os valores passados...")
    #maior numero começa com 0
    maior_num = 0
    for valor in valores:
        #maior_num recebe o primeiro numero dos valores
        if maior_num == 0:
            maior_num = valor
        #Se o valor for maior que o maior numero, maior numero recebe o valor
        if valor >= maior_num:
            maior_num = valor
        #End quebra a linha, flush responsavel por não deixar o sleep dar buffer.
        print(f"{valor} ", end='', flush=True)
        sleep(0.5)
    print(f"Foram informados {len(valores)} valores ao todo.")
    print(f"O maior valor informado foi {maior_num}.")
        
#Main
maior_numero(2, 9, 4, 5, 7, 1)
maior_numero(4, 7, 0)
maior_numero(1, 2)
maior_numero(6)
maior_numero()