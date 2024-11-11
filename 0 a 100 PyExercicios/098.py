from time import sleep
def linha():
    print("=-"*30)


def contador(i, f, p):
       #transforma o numero negativo em positivo, e o 0 em 1
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    linha()
    print(f"Contagem de {i} até {f} de {p} em {p}")

  
    #contador
    if i <= f:
        cont = i
        while cont <= f:
            print(f"{cont} ", end='', flush=True)
            sleep(0.5)
            cont += p
        print("FIM!")
    else:
        cont = i
        while cont >= f:
            print(f"{cont} ", end='', flush=True)
            sleep(0.5)
            cont -= p
        print("FIM!")


# PROGRAMA PRINCIPAL
contador(1,10,1)
contador(10,0,2)
linha()
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
