num = [[], []]
valor = 0
for cont in range(1, 8):
    valor = int(input(f'Qual o {cont}o valor? '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'Todos os valores: {num}')
num[0].sort()
num[1].sort()
print(f'Todos os valores pares: {num[0]}')
print(f'Todos os valores ímapres: {num[1]}')