continua = 'S'
soma = qtd = med = 0
maior = menor = 0
while continua in 'Ss':
    num = int(input('Qual o número? '))
    soma += num
    qtd += 1
    if qtd == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
med = soma/qtd
print('Média: {}'.format(med))
print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
print('FIM')