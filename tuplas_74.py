from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
           randint(0, 10), randint(0, 10))
for n in numeros:
    print(f'{n} ', end=' ')

print(f'\nMaior valor: {max(numeros)}')
print(f'Menor valor: {min(numeros)}')
