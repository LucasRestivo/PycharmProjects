#conceito: variável que armazena mais de um valor
#tuplas são imutáveis

lanche = ('hambúrguer', 'pizza', 'suco', 'pudim', 'sorvete')
print(lanche[1])
print('==' * 20)

#imprime contando ao contrário
print(lanche[-1])
print('==' * 20)

#imprime a QUANTIDADE de elementos
print(len(lanche))
print('==' * 20)

#imprimindo com for
for comida in lanche:
    print(f'Vou comprar {comida}')

#imprime o total de elementos sem saber a quantidade exata e mostra a posição
for cont in range(0, len(lanche)):
    print(f'Vou comprar {lanche[cont]} na posição {cont}')
print('==' * 20)

#imprime o total de elementos sem saber a quantidade exata (outra forma)
for pos, comida in enumerate(lanche):
    print(f'Vou comprar {comida} na posição {pos}')
print('==' * 20)

#imprime do elemento 1 ao 3
print(lanche[1:3])
print('==' * 20)

#imprime do elemento 2 até o fim
print(lanche[2:])
print('==' * 20)

#imprime do início até o elemento 2
print(lanche[:2])
print('==' * 20)

#imprime do elemento -3 até o final
print(lanche[-3:])
print('==' * 20)

#imprime em ordem (na verdade ele cria uma lista)
print(sorted(lanche))
print('==' * 20)

#concatenação de tuplas (não soma)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5)) #conta quantas vezes aparece o 5 em c
print(c.index(2)) #em que posição está o 2 (a primeira aparição)
print(c.index(2, 1)) #em que posição está o 2 (a partir da posição 1)

