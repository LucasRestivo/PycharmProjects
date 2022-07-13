#loop com break
num = soma = 0
while True:
    num = int(input('Qual número? '))
    if num == 999:
        break
    soma += num
print(f'Soma: {soma}')  #atualizado fstring
print('-+' * 30)

#loop regular
cont = 1
while cont <= 10:
    print(cont, '->', end=' ')
    cont += 1
print('FIM')
print('-+' * 30)

#loop simples usando flag
n = s = 0
while n != 999:
    n = int(input('Qual número? '))
    s += n
print('Soma: {}'.format(s))
print('-+' * 30)




