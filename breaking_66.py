num = soma = cont = 0
while True:
    num = int(input('Qual número? [999 para parar] '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Soma: {soma}')
print(f'Total de entradas: {cont}')
