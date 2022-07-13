nome = str(input('Qual nome? '))
if nome == 'Lucas':
    print('Correto')
elif nome == 'Maria' or nome == 'Paulo':
    print('Nomes secundários')
elif nome in 'Joana Joaquim Juvenal':
    print('Começa com J')
else:
    print('Incorreto')
print('Bom dia {}'.format(nome))