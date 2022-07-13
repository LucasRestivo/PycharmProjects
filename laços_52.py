num = int(input('Qual número? '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        print('{} '.format(c), end='')
        cont += 1

print('\nPrimo' if cont == 2 else '\nNão é primo')