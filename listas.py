num = (2, 5, 9, 1) #tupla
print(num)
#num[2] = 3 daria um erro pois tupla é imutável

num2 = [2, 5, 9, 1] #lista
print(num2)
num2[2] = 3
print(num2)
print('=-'*20)

#adicionar um valor no final
num2.append(7)
print(num2)

#ordena a lista
num2.sort()
print(num2)

#ordena a lista ao contrário
num2.sort(reverse=True)
print(num2)

#contagem de elementos
print(f'A lista tem {len(num2)} elementos')

#inserir o valor 19 na posição 2
num2.insert(2, 19)
print(num2)

#remove elementos da posição 2
num2.pop(2)
print(num2)

#remove um elemento no qual eu sei o valor, no caso a primeira aparição
num2.remove(2)
print(num2)

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
print(valores) #amostragem em forma de lista

#amostragem sem a forma da lista
for v in valores:
    print(f'{v}... ', end='')
print('fim')

#amostragem sem a forma da lista descritiva
for c, v in enumerate(valores):
    print(f'Na posição {c} existe o valor {v}')
print('fim')

#inserir valores para a lista
lista = []
for cont in range(0, 5):
    lista.append(int(input('Qual valor? ')))
print(lista)

#ligação de listas (as listas se espelham)
a = [2, 3, 4, 5]
b = a
b[2] = 10
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#cópia de listas (as listas não se espelham)
a = [2, 3, 4, 5]
b = a[:]
b[2] = 10
print(f'Lista A: {a}')
print(f'Lista B: {b}')

