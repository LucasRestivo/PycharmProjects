jogador = dict()
gol = list()
time = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input((f'Quantas partidas {jogador["nome"]} jogou? ')))
    gol.clear()
    for cont in range(0, jogador['partidas']):
        gol.append(int(input(f'Quantos gols na partida {cont+1}? ')))
    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    time.append(jogador.copy())
    while True:
        resp = str(input('Continuar? S/N ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO. S/N aceito somente')
    if resp == 'N':
        break
print('-'*55)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*55)
while True:
    busca = int(input(('Qual jogador quer buscar? 999-parar ')))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro. Jogador inexistente')
    else:
        print(f'Levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'No jogo {i+1} fez {g} gols')
    print('-'*55)
print('fim')