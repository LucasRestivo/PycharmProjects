def fatorial(num, show=False):
    """ 
    - Cálculo de fatorial de um número
    :param num: o número que será calculado
    :param show: (opcional) se irá mostrar ou não a conta
    :return: o valor do fatorial de 'num'
    """ #docstring

    f = 1
    for cont in range(num, 0, -1):
        if show:
            print(cont, end='')
            if cont > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= cont
    return f


print(fatorial(9, show=True))
help(fatorial)