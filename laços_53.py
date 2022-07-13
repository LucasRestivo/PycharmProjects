frase = str(input('Digite a frase: ')).strip().lower()
palavras = frase.split()
juntas = ''.join(palavras)
inverso = ''
for letra in range (len(juntas) - 1, -1, -1):
    inverso += juntas[letra]
print(inverso)

print ('Palíndromo' if juntas == inverso else 'Não palíndromo')
