#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
# mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres
# têm menos de 20 anos.

soma_idade = 0
mais_velho = 0
nome_velho = ''
mulher20 = 0
for c in range(1, 5):
    nome = str(input('Qual o nome da pessoa {}? '.format(c))).strip()
    idade = int(input('Qual a idade da pessoa {}? '.format(c)))
    sexo = str(input('Qual o sexo M/F? '.format(c))).strip()
    soma_idade += idade
    if c == 1 and sexo in 'Mm':
        mais_velho = idade
        nome_velho = nome
    else:
        if idade > mais_velho and sexo in 'Mm': # 'Mm' indifere minúsculo de maiúsculo, pode trocar por upper() no for
            mais_velho = idade
            nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
    print('')

med_idade = soma_idade/4
print('Média de idade é: {}'.format(med_idade))
print('Mais velho tem: {} e o nome dele é {}'.format(mais_velho, nome_velho))
print('Existe(m) {} mulher(es) com menos de 20 anos'.format(mulher20))