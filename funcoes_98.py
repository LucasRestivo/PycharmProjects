from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}...')
    sleep(1)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            cont += passo
            sleep(0.4)
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            cont -= passo
            sleep(0.4)


    print('\nFIM')


contador(0, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Personalize a contagem...')
inicio_p = int(input('Início: '))
fim_p = int(input('Fim: '))
passo_p = int(input('Passo: '))
contador(inicio_p, fim_p, passo_p)