vel = float(input('Qual a velocidade? '))

if vel > 80.0:
    print('Você foi multado em R${}'.format(7*(vel - 80.0)))
