from datetime import date
ano = int(input('Qual ano de nascimento? '))
ano_atual = date.today().year
idade = ano_atual - ano

if idade < 18:
    print('Abaixo da idade. Faltam {} anos'.format(18-idade))
elif idade > 18:
    print('Acima da idade')
else:
    print('Ano de alistamento')