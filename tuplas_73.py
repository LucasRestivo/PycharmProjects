times = ('Palmeiras', 'Athletico-PR', 'Atlético-MG', 'Corinthians', 'Internacional',
         'Fluminense', 'São Paulo', 'Flamengo', 'Santos', 'Botafogo', 'Avaí',
         'Coritiba', 'América-MG', 'Bragantino', 'Ceará', 'Atlético-GO',
         'Goiás', 'Cuiabá', 'Juventude', 'Fortaleza')
print(times)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(f'Os 4 últimos colocados são: {times[-4:]}')
print(f'Ordem alfabética: {sorted(times)}')
busca = str(input('Qual time quer procurar a posição? '))
print(f'O {busca} está na posição: {times.index(busca)+1}')
