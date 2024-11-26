#situação ruim/razoavel/boa
#quantos numeros possiveis adicionar 

def notas(*valores, sit=True):
    '''-> Função para analisar notas e situações de varios alunos.
    :param valores: uma ou mais notas dos alunos(Aceita varias).
    :param sit: (opcional) indicado se deve ou não adicionar a situação .
    :return: dicionario com varias informaçoes sobre a situação da turma.'''
    
    c = maior_valor = menor_valor = 0
    lista_valor = list()
    notas_alunos = dict()
    soma = 0
    for valor in valores:
        c += 1
        if valor > maior_valor:
            maior_valor = valor
        if valor < menor_valor:
            menor_valor = valor
        if c == 1:
            maior_valor = menor_valor = valor
        #Soma os valores
        soma += valor
    #Calcula a media 
    media = soma / c
    #Total de notas
    total = c
    status = ''
    if media < 6:
        status = 'Ruim'
    if media >= 6 and media <= 7:
        status = 'Razoável'
    if media > 7:
        status = 'Boa'

    notas_alunos['total'] = total
    notas_alunos['maior'] = maior_valor
    notas_alunos['menor'] = menor_valor
    notas_alunos['media'] = media
    if sit:
        notas_alunos['situação'] = status
    else:
        ''
    return notas_alunos



# main
resp = notas(5.5, 5, 10, 3, sit=True)
print(resp)

# professor
#def notas(*n, sit= False)
    #r = dict()
    #r['total'] = len(n)
    #r['maior'] = max(n)
    #r['menor'] = min(n)
    #r['media'] = sum(n)/len(n)
    #if sit:
        #if r['media'] >= 7:
            #r['situação'] = 'BOA'
        #if r['media'] >= 5:
            #r['situação'] = 'RAZOAVEL'
        #else:
            #r['situação'] = 'RUIM'
    #return r
