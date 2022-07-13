n1 = float(input('Qual a nota 1? '))
n2 = float(input('Qual a nota 2? '))
med = (n1+n2)/2
print('Sua média foi: {:.2f}'.format(med))

if med < 5.0:
    print('Reprovado')
elif med >= 5.0 and med < 7.0:
    print('Recuperação')
else:
    print('Aprovado')
