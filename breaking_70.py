total = cont_preco = menor = cont_prod = 0
barato = ' '

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont_prod += 1
    total += preco
    if preco > 1000:
        cont_preco += 1
    if cont_prod == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN': #valida se a resposta é somente S ou N, não possibilitando J, por ex
        resp = str(input('Quer continuar? S/N ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total da compra foi de R${total}')
print(f'Total de produtos que custaram mais que R$1000,00: {cont_preco}')
print(f'Produto mais barato ({barato}) custou R${menor:.2f}')
print('{:-^40}'.format('FIM DO PROGRAMA'))
