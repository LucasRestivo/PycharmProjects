#Diferença entre for e while é que no for tem limite, no while pode ser infinito ou com limite

c = 1
while c < 10:
    print(c)
    c += 1
print('fim')
print('-=' * 10)

#analisa se um número não nulo é par ou ímpar
n = 1
par = impar = 0
while n != 0:
    n = int(input('Qual valor? '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Total de pares é {} e de ímpares é {}'.format(par, impar))
print('fim')
