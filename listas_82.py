numeros = list()
numeros_pares = list()
numeros_impares = list()
while True:
    numeros.append(int(input('Qual valor? ')))
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua in 'Nn':
        break
print(f'A lista digitada foi: {numeros}')
for i, v in enumerate(numeros):
    if v % 2 == 0:
        numeros_pares.append(v)
    elif v % 2 == 1:
        numeros_impares.append(v)
print(f'Lista dos pares: {numeros_pares}')
print(f'Lista dos ímapres: {numeros_impares}')