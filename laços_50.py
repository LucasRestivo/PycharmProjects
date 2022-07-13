soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Qual número {}? '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma do(s) {} número(s) par(es) é: {}'.format(cont, soma))
