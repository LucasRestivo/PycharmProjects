from random import randint

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = str(input('Par ou Ímpar [P/I]? ')).upper()
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P' and total % 2 == 0: #poderia ser while tipo not in 'PpIi'
        print('Você ganhou')
    elif tipo == 'I' and total % 2 != 0:
        print('Você ganhou')
    else:
        print('Você perdeu')
        break
print('fim')
