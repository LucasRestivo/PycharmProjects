valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o valor do salário? '))
anos = int(input('Em quantos anos? '))

prest_total = anos*12
prest_mes = valor/prest_total
print('Total de prestações: {}'.format(prest_total))
print('Por mês: {:.2f}'.format(prest_mes))

if prest_mes > 0.3*salario:
    print('Não aprovado. Prestação maior que 30% do salário')
else:
    print('Aprovado')

