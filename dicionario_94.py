galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo M/F ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO. M/F aceito somente')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Continuar? S/N ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO. S/N aceito somente')
    if resp == 'N':
        break
print(galera)
print(f'Existem {len(galera)} pessoas cadastradas')
media = soma/len(galera)
print(f'A média das idades é {media:5.2f}')
print(f'As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'As pessoas com idade acima da média são: ', end='')
for p in galera:
    if p['idade'] >= media:
        print(f'{p["nome"]} ', end='')
print()