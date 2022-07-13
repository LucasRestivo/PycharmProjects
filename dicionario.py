#dicionário {}, tupla (), lista []
pessoas = {'Nome': 'Lucas', 'Sexo': 'M', 'Idade': 29}
print(pessoas)
print(pessoas['Nome']) #não existe em dicionários pessoas[0] pois este foi alocado para 'Nome'

#aspas duplas para referenciar
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')

#imprime as keys
print(pessoas.keys())

#imprime os valores das keys
print(pessoas.values())

#imprime o conjunto
print(pessoas.items())

#acessando por laços a key ou values
for k in pessoas.keys():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')

#troca de valores
pessoas['Nome'] = 'João'
print(pessoas['Nome'])

#adiciona elemento
pessoas['Peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')



