from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
ranking = list()
print('Sorteando valores...\n')
for k, v in jogo.items():
    print(f'{k} sorteou {v}')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #key=itemgetter(1) coloca em ordem crescente
print('\nRanking dos jogadores...')
for k, v in enumerate(ranking):
    print(f'Posição {k+1} ficou {v[0]} pois sorteou {v[1]}')
    sleep(0.5)

