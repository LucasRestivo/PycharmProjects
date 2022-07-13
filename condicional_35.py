r1 = float(input('Qual r1? '))
r2 = float(input('Qual r2? '))
r3 = float(input('Qual r3? '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Forma triângulo')
else:
    print('Não forma triângulo')