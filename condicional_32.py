from datetime import date
ano = int(input('Qual o ano? Ou pressione 0 para importar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Bissexto')
else:
    print('Não bissexto')