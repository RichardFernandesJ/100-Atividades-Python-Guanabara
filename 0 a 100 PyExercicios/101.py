from datetime import date
ano_atual = date.today().year#Vai chamar o ano atual
def voto(ano_nascimento=ano_atual):
    val = ano_atual - ano_nascimento
    return val


def temvoto(num):
    if num >= 18 and num <= 64:
        return ("VOTO OBRIGATORIO!")
    elif num < 18:
        return ("NÃO VOTA!")
    elif num >= 65:
        return ("VOTO OPCIONAL!")
    

#Main
ano = int(input("Em que ano você nasceu? "))
idade = voto(ano)
status = temvoto(idade)
print(f"Com {idade} anos: {status}")

#-----------------------------------------------------------------------
# Professor
#def voto(ano):
#   from datetime import date
#   atual = date.today().year  
#   idade = atual - ano
#if idade < 16: 
#   return f'Com {idade} anos : NÃO VOTA.'
#elif 16 <= idade < 18 or idade > 6: 
#   return f'Com {idade} anos : VOTO OPCIONAL.'
#else: 
#   return f'Com {idade} anos : VOTO OBRIGATORIO.'
##Programa principal
#nasc = int(input("Em que ano você nasceu? "))
#print(voto(nasc))
#-----------------------------------------------------------------------