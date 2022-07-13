numeros = list()
while True:
    n = int(input('Qual valor? '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado')
    else:
        print('Valor duplicado')
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua in 'Nn':
        break
print(f'A lista digitada foi: {numeros}')
numeros.sort()
print(f'A lista, em ordem, digitada foi: {numeros}')