from math import factorial
n = int(input(('Qual número: ')))
fac = factorial(n)
print('Fatorial de {} é {}'.format(n, fac))

print('-=' * 25)

num = int(input(('Qual número: ')))
const = num
fatorial = 1
while const > 0:
    print('{}'.format(const), end=' ')
    print('x' if const > 1 else '= ', end=' ')
    fatorial = fatorial * const
    const -= 1
print (fatorial)
print('\nfim')
