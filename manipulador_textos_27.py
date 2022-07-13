nome = str(input('Nome: ')).strip()
divide = nome.split()

print('Primeiro nome: {}'.format(divide[0]))
print('Último nome: {}'.format(divide[len(divide)-1]))
