frase = str(input('Qual a frase: ')).strip()
print('A quantidade de "a" é: {}'.format(frase.lower().count('a'))) #pode passar o.lower() para o input para não ter que repetir
print('A posição da primeira é: {}'.format(frase.lower().find('a')))
print('A posição da última é: {}'.format(frase.lower().rfind('a')))
