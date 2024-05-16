from random import randint
maquina = randint(0,11)
val = c = 0
while True:
    print('')
    print('=-'*20)
    print('VAMOS JOGAR \033[31mPAR\033[m OU \033[32mÍMPAR\033[m')
    print('=-'*20)
    val = int(input('Digite um valor: '))
    #Enquanto não for P OU I ele repete o codigo esperando a str valida
    pi = ' '
    while pi not in 'PI':
        pi = str(input('\033[31mPAR\033[m OU \033[32mÍMPAR\033[m ? [\033[31mP\033[m/\033[32mI\033[m] ')).upper().strip()[0]
    #------------------------------------------------------------------
    print('--'*20)
    result = val + maquina
    if result % 2 == 0:
        rpi = 'PAR'
    if result % 2 != 0:
        rpi = 'ÍMPAR'
    print(f'Você jogou {val} e o computador {maquina}. Total deu {result} deu {rpi}')
    print('--'*20)
    if pi == 'P' and rpi == 'PAR' or pi == 'I' and rpi == 'ÍMPAR':
        print('Você VENCEU !')
        print('Vamos jogar novamente...')
        print('=-'*20)
        c += 1
    else:
        print('Você PERDEU !')
        print('=-'*20)
        print(f'GAME OVER! Você venceu {c} vezes.')
        break


    
