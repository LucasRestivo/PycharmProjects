from math import sqrt, floor

num = int(input('Qual número? '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))