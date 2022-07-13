p_term = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))

soma = p_term
for c in range(0, 10):
    print('{} '.format(soma), end='- ')
    soma += razao
print('fim')
