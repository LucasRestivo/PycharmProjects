soma = 0
cont = 0
for num in range(1, 501, 2):
    if num % 3 == 0:
        print(num)
        soma += num
        cont += 1
print('Soma de {} números é: {}'.format(cont, soma))
print('fim')