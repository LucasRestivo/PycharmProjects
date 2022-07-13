num = int(input('Qual o número? '))

for c in range(0, 11):
    print('{} * {} = {}'.format(num, c, num*c))
print('fim')