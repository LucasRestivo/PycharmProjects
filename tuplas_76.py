listagem = ('Lápis', 2.00,
            'Boracha', 2.50,
            'Caderno', 18.90,
            'Transferidor', 5.00,
            'Caneta', 7.00,
            'Livro', 80.00,
            'Mochila', 75.90)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}') #mostra a formatação com 2 casas decimais

