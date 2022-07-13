lista = []
for cont in range(0, 5):
    n = int(input('Qual valor? '))
    if cont == 0 or n>lista[-1]: #valida se é o primeiro ou maior que o último elemento
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n) #insere o valor 'n' em 'pos'
                break
            pos += 1
print('-=' * 30)
print(f'Valores digitados em ordem: {lista}')


