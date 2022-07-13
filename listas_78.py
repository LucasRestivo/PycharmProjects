lista = []
maior = menor = 0
for cont in range(0, 5):
    lista.append(int(input('Qual valor? ')))
    if cont == 1:
        maior = menor = lista[cont]
    else:
        if lista[cont] < menor:
            menor = lista[cont]
        if lista[cont] > maior:
            maior = lista[cont]

print(lista)

print(f'Maior número é {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'Menor número é {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')
print()