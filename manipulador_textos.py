#frase = str(input('Entre com a frase: '))
frase = 'Isso só pode ser um teste, não pode?  '

# deixa tudo em maiúsculo
print(frase.upper())
#verifica o tamanho da frase sem os espaços
print(len(frase.strip()))
#substitui palavras
print(frase.replace('teste', 'curso'))
#verifica se pertence
print('pode' in frase)
#verifica em que posição está
print('Procura pela esquerda: {}'.format(frase.find('pode')))
#verifica em que posição está a partir da direita
print('Procura pela direita: {}'.format(frase.rfind('pode')))
#cria separação das palavras com objeto
dividido = frase.split()
print(dividido) #mostra toda a lista
print(dividido[0]) #mostra o primeiro item da lista
print(dividido[2][3]) #pega o segundo item (pode) e mostra a terceira posição
#aspas tripla para textos longos
print('''Nessa aula, vamos aprender operações com String no Python.
As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações com replace(), upper(),
lower(), capitalize(), title(), strip(), junção com join().''')
#comprimento
print(len(frase))