palavras = ('aprender', 'programar', 'linguaguem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais:', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

