jogador = dict()
gol = list()
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input((f'Quantas partidas {jogador["nome"]} jogou? ')))

for cont in range(0, jogador['partidas']):
    gol.append(int(input(f'Quantos gols na partida {cont+1}? ')))
jogador['gols'] = gol[:]
jogador['total'] = sum(gol)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} é igual {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas e tem um total de gols igual a {jogador["total"]}')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i+1}, fez {v} gols')
