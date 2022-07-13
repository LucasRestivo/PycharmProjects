numeros = list()
while True:
    n = int(input('Qual valor? '))
    numeros.append(n)
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua in 'Nn':
        break
print(f'A lista digitada foi: {numeros}')
print(f'O total de números inserido foi: {len(numeros)}')
numeros.sort(reverse=True)
print(f'Em ordem descrescente: {numeros}')

if 5 in numeros:
    print('O valor 5 faz parte da lista')
else:
    print('Não há 5 na lista')