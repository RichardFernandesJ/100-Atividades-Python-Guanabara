#cor branco \030[0:30:40m
print('\033[7;40mbranco\033[m')
#cor verde\033[7;42mverde\033[m
print('\033[1;30;42mverde\033[m')
#cor azul\033[34;40mazul\033[m
print('\033[1;30;44mazul\033[m')
while True:
    func = input("Função ou Biblioteca >")
    if func == 'fim':
        break
    print('\033[1;30;44m~~'*30)
    print(f"Acessando o manual do comando '{func}'")
    print('~~\033[m'*30)
    desc = help(func)
    print(f"\033[7;40m{desc}\033[m")
