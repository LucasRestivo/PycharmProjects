princ = list()
temp = list()
maior = menor = 0
while True:
    temp.append(str(input('Qual nome? ')))  #armazenará o nome
    temp.append(float(input('Qual peso? ')))  #armazenará o peso
    if len(princ) == 0:  #primeira validação
        maior = menor = temp[1]  #armazena o primeiro peso
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])  #coloca no mesmo vetor [nome, peso] para todas as entradas, copiando o vetor
    temp.clear()  #elimina
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua in 'Nn':
        break
print(f'Dados cadastrados: {princ}')
print(f'A lista tem {len(princ)} pessoas cadastradas.')
print(f'O maior peso foi de {maior}kg. Peso de ',  end='')
for p in princ: #varre todos os valores na lista
    if p[1] == maior: #vê se o peso é igual que o maior armazenado já validado
        print(f'[{p[0]}] ', end='') #imprime o nome correspondente ao peso
print()
print(f'O menor peso foi de {menor}kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()