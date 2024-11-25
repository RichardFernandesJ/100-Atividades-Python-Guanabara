def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print(f"\033[0;31mERRO! DIGITE UM NUMERO VALIDO!\033[m")
    return valor



# main
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar um número {n}')


