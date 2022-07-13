estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())  #não existe fatiamento para dicionário que pode copiar, mas tem a função interna copy()
print(brasil)
print('-'*30)
for e in brasil: #corre a lista que contem os estados
    print(e)
print('-'*30)
for e in brasil: #corre a lista que contem os estados
    for v in e.values(): #corre o dicionário que está em cada estado
        print(v, end=' ')
    print()
