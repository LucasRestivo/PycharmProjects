
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: não pode votar'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: voto opcional'
    else:
        return f'Com {idade} anos: voto obrigatório'

ano_pergunta = int(input('Qual ano? '))
print(voto(ano_pergunta))