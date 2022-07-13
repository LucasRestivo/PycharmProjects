from random import randint
from time import sleep

print ('''
0) Pedra
1) Papel
2) Tesoura
''')
op = int(input('Qual opção? '))
if op == 0 or op == 1 or op == 2:
    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PO!')
    opcoes = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)
    print('*=' * 16)
    if op == computador:
        print('O PC escolheu {}. Empatou'.format(opcoes[computador]))
    elif op == 0 and computador == 1:
        print('O PC escolheu {}. Você perdeu'.format(opcoes[computador]))
    elif op == 0 and computador == 2:
        print('O PC escolheu {}. Você ganhou'.format(opcoes[computador]))
    elif op == 1 and computador == 2:
        print('O PC escolheu {}. Você perdeu'.format(opcoes[computador]))
    elif op == 1 and computador == 0:
        print('O PC escolheu {}. Você ganhou'.format(opcoes[computador]))
    elif op == 2 and computador == 0:
        print('O PC escolheu {}. Você perdeu'.format(opcoes[computador]))
    else: #2 e 1
        print('O PC escolheu {}. Você ganhou'.format(opcoes[computador]))
else:
    print("Opção inválida")