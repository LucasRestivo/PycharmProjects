nome = str(input('Nome? ')).strip() #strip retira espaços laterais
print('Em maiúscula é: {}'.format(nome.upper()))
print('Em minúscula é: {}'.format(nome.lower()))
print('Tamanho é: {}'.format(len(nome) - nome.count(' ')))
print('Primeiro nome tem {} letras'.format(nome.find(' '))) #acha o primeiro espaço
dividido = nome.split()
print('Primeiro nome é {} e tem {} letras'.format(dividido[0], len(dividido[0])))
