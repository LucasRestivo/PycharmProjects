def teste(b):
    global a  #global mantem o valor da def
    a = 8
    b += 4
    c = 2
    print(f'A de dentro vale {a}')
    print(f'B de dentro vale {b}')
    print(f'C de dentro vale {c}')


a = 5
teste(a)
print(f'A de fora vale {a}')

print('=+'*30)

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3,2,5)
r2 = somar(4,2)
r3 = somar(5)
print(f'As somas são {r1}, {r2} e {r3}')

print('=+'*30)

def fatorial(num=1):
    f = 1
    for cont in range(num, 0, -1):
        f *= cont
    return f

n = int(input('Qual número? '))
print(f'O fatorial de {n} = {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

print('=+'*30)

def par(n=0):
     if n % 2 == 0:
         return True
     else:
         return False


num = int(input('Qual núm? '))
valida = par(num)
if valida == True:
    print('É par')
else:
    print('É impar')

