def maior(*num):
    maior = cont = 0
    print(f'\nAnalisando os valores...')
    for valor in num:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores, e o maior é {maior}')



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 3)
maior(1, 2)
maior()