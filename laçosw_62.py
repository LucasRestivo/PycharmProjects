p_term = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))

termo = 1
soma = p_term
extra = 10
total = 0

while extra != 0:
    total += extra
    while termo <= total:
        print('{} '.format(soma), end='- ')
        soma += razao
        termo += 1
    extra = int(input('\nQuantos termos mostrar a mais? '))
print('Total de {} mostrados'.format(total))