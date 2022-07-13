from modulos_115.lib.interface import *
from modulos_115.lib.arquivo import *
from time import sleep

arq = 'curso.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver cadastrados', 'Cadastrar pessoas', 'Sair'])
    if resposta == 1:
        #listando o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        #cadastrando uma nova entrada
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('tchau')
        break
    else:
        print('Erro. Digite uma opção válida')
    sleep(2)


