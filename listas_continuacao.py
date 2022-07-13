#listas dentro de listas
teste = list()
teste.append('Lucas')
teste.append(29)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 30
galera.append(teste[:])
print(galera)

print('='*30)

galera = ['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]
#pega só o primeiro item da primeira parte
print(galera[0][0])

#pega cada parte e separa
for p in galera:
    print(p)

#pega cada parte e separa só uma parte
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')

#cria o vetor com mais de uma posição, depois cria uma cópia (turma) para amostragem
turma = list() #estrutura principal
dado = list() #estrutura auxiliar
cont_maior = cont_menor = 0
for c in range(0, 3):
    dado.append(str(input(('Nome: '))))
    dado.append(int(input(('Idade: '))))
    turma.append(dado[:])
    dado.clear()
print(turma)
for p in turma: #para cada termo em turma
    if p[1] >= 18:  #se a idade for maior que 18, imprime o nome
        print(f'{p[0]} é maior de idade')
        cont_maior += 1
    else:
        print(f'{p[0]} é menor de idade')
        cont_menor += 1
print(f'Total de maiores: {cont_maior}')
print(f'Total de menores: {cont_menor}')
