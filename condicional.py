nome = str(input('Qual nome? '))
if nome == 'Lucas':
    print('Correto')
else:
    print('Incorreto')
print('Bom dia {}'.format(nome))

n1 = float(input('Qual a nota 1? '))
n2 = float(input('Qual a nota 2? '))
med = (n1+n2)/2
print('Sua média foi: {:.2f}'.format(med))
if med >= 6.0:
    print('Nota boa')
else:
    print('Nota ruim')

print('Aprovado' if med >= 6.0 else 'Reprovado')
