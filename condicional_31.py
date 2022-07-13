dist = float(input('Qual a distância? '))

if dist <= 200:
    print('Total: {}'.format(dist * 0.5))
else:
    print('Total: {}'.format(dist * 0.45))