from datetime import date
ano = int(input('Qual ano de nascimento? '))
ano_atual = date.today().year
idade = ano_atual - ano

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')