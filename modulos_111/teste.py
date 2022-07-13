from utilidades import moeda
from utilidades import dado

p = dado.leiaDinheiro('Qual o preço? R$')
#passando como parâmetros o preço, taxa de aumento e taxa de redução
moeda.resumo(p, 22, 5)