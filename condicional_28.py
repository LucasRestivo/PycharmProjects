import random
escolha = int(input('Qual número? '))
num = random.randint(0, 5)

print('O número sorteado foi: {}'.format(num))
print('Você acertou' if escolha == num else 'Você errou')
