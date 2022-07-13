def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(2, 4)
soma(4, 5)
soma(2, 1)
soma(a=3, b=5)
print('-='*30)

#contador com número de parâmetros variados
def contador(*num):
    for valor in num:
        print(valor, end=' ')
    print('fim')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

#quantidade de elementos
def cont(*num2):
    tam = len(num2)
    print(f'Valores inseridos {num2} e possuem {tam} números')


cont(2, 1, 7)
cont(8, 0)
cont(4, 4, 7, 6, 2)

#funções com lista
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [5, 2, 3, 8, 12, 2]
print(valores)
dobra(valores)
print(valores)

#desempacotamento
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(2, 4)
soma(5, 2, 1)