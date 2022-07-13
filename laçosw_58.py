import random

escolha = int(input('Qual o número? '))
num = random.randint(0, 11)

cont = 1
while escolha != num:
    escolha = int(input('Errou. Tente novamente, qual número? '))
    cont += 1

print('Acertou. Total de tentativas: {}'.format(cont))
