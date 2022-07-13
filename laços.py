#laço regular simples
for c in range(1, 6):
    print('Teste')
print('fim')

#contagem
for c in range(1, 6):
    print(c)
print('fim')

#contagem invertida (-1 é o passo)
for c in range(6, 0, -1):
    print(c)
print('fim')

#somatório
s = 0
for c in range(0, 4):
    n = int(input('Valor: '))
    s = s + n #ou s += n
print('Soma total é {}'.format(s))
