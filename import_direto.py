import math

num = float(input('Digite um número real: '))
cat2 = float(input('Digite o segundo cateto: '))
ang = float(input('Digite um ângulo: '))
ang_rad = math.radians(ang)

print('A parte inteira de {} é igual a {}'.format(num, math.floor(num)))
print('A hipotenusa entre {} e {} é: {}'.format(num, cat2, math.hypot(3,4)))
print('O seno, cosseno e tangente de {} é, respectivamente: {:.2f}, {:.2f} e {:.2f}'.format(ang, math.sin(ang_rad), math.cos(ang_rad), math.tan(ang_rad)))