aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['med'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['med'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['med'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'
print('-='*20)
for k, v in aluno.items():
    print(f'{k} é igual {v}')
