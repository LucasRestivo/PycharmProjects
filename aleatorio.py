import random
import random

aluno1 = str(input('Nome 1: '))
aluno2 = str(input('Nome 2: '))
aluno3 = str(input('Nome 3: '))
lista = [aluno1, aluno2, aluno3]

escolhido = random.choice(lista)
random.shuffle(lista)

print('O escolhido foi: {}'.format(escolhido))
print('Ordem de apresentação: {}'.format(lista))