n = int(input('Quantos termos? '))

t1 = 0
t2 = 1
cont = 3


print('{} - {}'.format(t1, t2), end=' ')
while cont <= n:
    t3 = t2 + t1
    print('- {}'.format(t3), end=' ')
    cont += 1
    t1 = t2
    t2 = t3
print('\nFIM')

