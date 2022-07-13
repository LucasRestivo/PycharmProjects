p_term = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))

soma = p_term
termo = 10

while termo > 0:
    print('{} '.format(soma), end='- ')
    soma += razao
    termo -= 1
print('fim')
