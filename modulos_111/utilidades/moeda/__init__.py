def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa)/100
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa)/100
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco/2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.',',')

def resumo(preço=0, taxa_aumento=10, taxa_reducao=5):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t\t{moeda(preço):}')
    print(f'Dobro do preço: \t\t{dobro(preço, True)}')
    print(f'Metade do preço: \t\t{metade(preço, True)}')
    print(f'Com {taxa_aumento}% de aumento: \t{aumentar(preço, taxa_aumento, True)}')
    print(f'Com {taxa_reducao}% de redução: \t\t{aumentar(preço, taxa_reducao, True)}')
    print('-' * 35)