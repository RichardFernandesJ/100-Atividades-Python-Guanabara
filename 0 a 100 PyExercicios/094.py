homens = list()
count = 0
lista_pessoas = list()
media = list()
mulheres = list()

#Repete o codigo, para cadastra novas pessoas.
while True:
    #Dicionario que vai receber a pessoa os dados da pessoa.
    dict_pessoa = dict()
    #Count vai contar a quantidade de cadastros.
    count = count + 1
    #Recebe os dados do cadastrado 
    dict_pessoa['nome'] = input("Nome: ")
    dict_pessoa['sexo'] = input("Sexo: [M/F] ").lower() #lower responsavel por transformar os dados informado em minusculo.
    

    #Outra forma de validação
    #while True:
        #dict_pessoa['sexo'] = input("Sexo: [M/F] ")). lower()[0]   <-- O [0] para pegar a primeira letra
        #if dict_pessoa['sexo'] in 'mf':
            #break
        #print("ERRO! Responda apenas M ou F.")    



    #Repete a solicitação e o input caso não receba o valor correto m ou f.
    while dict_pessoa['sexo'] != 'm' and dict_pessoa['sexo'] != 'f':
        print("ERRO! Responda apenas M ou F.")
        dict_pessoa['sexo'] = input("Sexo: [M/F] ").lower()#lower responsavel por transformar os dados informado em minusculo.   
    dict_pessoa['idade'] = input("Idade: ")


    #Responsavel por enviar o dicionario da pessoa cadastrado para a lista, através do append.
    lista_pessoas.append(dict_pessoa)


    #input de seguimento da repetição principal, repete caso não receba o valor correto s ou n.
    resposta = input("Quer continuar? [S/N] ").lower()#lower responsavel por transformar os dados informado em minusculo. 
    while resposta != 's' and resposta != 'n':
        print("ERRO! Responda apenas S ou N.")
        resposta = input("Quer continuar? [S/N] ").lower()#lower responsavel por transformar os dados informado em minusculo. 


    #Responsavel por finalizar o codigo caso receba n como resposta.
    if resposta == 'n':
        break


#For, responsavel por pegar a idade de todos cadastrados. 
for c, idade in enumerate(lista_pessoas):
    idade = lista_pessoas[c]['idade']
    #transforma a str em int
    idade_int = int(idade)
    #Vai dar um append na idade para a lista media 
    media.append(idade_int)
#vai calcular a media de idade.
media_tot = sum(media) / count


#Imprime os dados count = quantidade de pessoas cadastradas.
print("=-"*20)
print(f"A) Ao todo temos {count} pessoas cadastradas.")
#Imprime a media de idade das pessoas cadastradas.
print(f"B) A média de idade é de {media_tot:.2f} anos.")
#For, responsavel por separar pessoas cadastradas com sexo [f]
for c, sexo in enumerate(lista_pessoas):
    if lista_pessoas[c]['sexo'] == 'f':
        #Vai dar um append, inserindo a mulher da lista de pessoas em lista de mulher.
        mulheres.append(lista_pessoas[c]['nome'])


#Imprime as mulheres cadastradas
print(f"C) As mulheres cadastradas foram ", end='')
#For responsavel por mostrar as mulheres cadastradas. 
for mulher in mulheres:
    print(f" {mulher}", end=',')
print("\n")


#Imprime as pessoas que estão acima da media
print(f"D) Lista das pessoas que estão acima da média: ")
#For, repsonsavel por separar as pessoas que tem a idade acima da media.
for c, idade in enumerate(lista_pessoas):
    idade = lista_pessoas[c]['idade']
    #Transforma em inteiro e vai exibir caso a idade seja maior que a media. 
    idade_int = int(idade)
    if idade_int >= media_tot:
        print(f"    nome = {lista_pessoas[c]['nome']}; sexo = {lista_pessoas[c]['sexo']}; idade = {lista_pessoas[c]['idade']};")

#Encerra o codigo
print("<<ENCERRADO>>")

