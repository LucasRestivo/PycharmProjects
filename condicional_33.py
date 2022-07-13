n1 = float(input('Qual número 1? '))
n2 = float(input('Qual número 2? '))
n3 = float(input('Qual número 3? '))

menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print('O menor é {} e o maior é {}.'.format(menor, maior))