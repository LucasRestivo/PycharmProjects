matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s_par = maior = s_col = 0
#for de alimentação de dados
for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite um valor para [{lin},{col}]: '))
#for de impressão + validação soma é par
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^5}]', end='') #^5 centraliza
        if matriz[lin][col] % 2 == 0:
            s_par += matriz[lin][col]
    print()
print(f'Soma dos pares é: {s_par}')

#for para soma da terceira coluna
for lin in range(0, 3):
    s_col += matriz[lin][2]
print(f'Soma da terceira coluna: {s_col}')

#for que avalia o maior na segunda linha
for col in range(0, 3):
    if col == 0:
        maior = matriz[1][col]
    elif matriz[1][col] > maior:
        maior = matriz[1][col]
print(f'Maior elemento da segunda linha: {maior}')