n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))

op = 0

while op != 5:
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair
    ''')
    op = int(input('Qual opção? '))
    if op == 1:
        soma = n1 + n2
        print('A soma é: {}'.format(soma))
    if op == 2:
        mult = n1 * n2
        print('A multiplicação é: {}'.format(mult))
    if op == 3:
        if n2 > n1:
            maior = n2
            print('Maior é: {}'.format(n2))
        else:
            print('Maior é: {}'.format(n1))
    if op == 4:
        n1 = int(input('Valor 1 novo: '))
        n2 = int(input('Valor 2 novo: '))
print('fim')