continua = 'S'
cont_idade = cont_sexo = cont_mulher_20 = 0
sexo = ' '
while continua in 'Ss':
    nome = str(input('Qual o nome? '))
    idade = int(input('Qual a idade? '))
    if idade >= 18:
        cont_idade += 1
    sexo = str(input('Qual o sexo [M/F]? ')).upper()
    if sexo == 'M':
        cont_sexo += 1
    elif sexo == 'F' and idade < 20:
        cont_mulher_20 += 1
    continua = str(input('*Quer continuar? [S/N] ')).strip().upper()[0]
    print('=-' * 30)
print(f'Maiores de 18 anos: {cont_idade}')
print(f'Homens: {cont_sexo}')
print(f'Mulher com menos que 20 anos: {cont_mulher_20}')
