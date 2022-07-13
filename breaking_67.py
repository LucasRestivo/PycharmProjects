while True:
    c = 0
    num = int(input('Tabuada de qual o número? '))
    if num < 0:
        break
    while c < 11:
        print('{} * {} = {}'.format(num, c, num*c))
        c += 1
print('fim')