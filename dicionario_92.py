from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 se não tem): '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano da contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f'{k} é igual {v}')


