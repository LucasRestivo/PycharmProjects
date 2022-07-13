soma = num = cont = 0
num = int(input('Qual o número? '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Qual o número? '))
print('Soma total: {}. Total de números para soma: {}'.format(soma, cont))
print('FIM')