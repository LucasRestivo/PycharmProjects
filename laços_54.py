from datetime import date
menor = 0
maior = 0

for c in range(1, 8):
    ano = int(input('Qual ano de nascimento {}? '.format(c)))
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1

print('Total de menores: {}'.format(menor))
print('Total de maiores: {}'.format(maior))