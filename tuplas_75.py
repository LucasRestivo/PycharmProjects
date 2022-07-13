numeros = (int(input('Número 1: ')), int(input('Número 2: ')),
           int(input('Número 3: ')), int(input('Número 4: ')))
print(f'Valores digitados: {numeros}')
#quantas vezes aparece o número 9
print(f'O número 9 apareceu {numeros.count(9)} vezes')
#em que posição apareceu o 3
if 3 in numeros:
    print(f'O número 3 apareceu na posição {numeros.index(3)+1}')
else:
    print('Não existe valor 3')
#quais são pares
print('Números pares: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')

