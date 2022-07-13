salario = float(input('Qual salário? '))

if salario <= 1250:
    aumento = salario*1.15
    print('Total: {}'.format(aumento))
else:
    aumento = salario*1.10
    print('Total: {}'.format(aumento))