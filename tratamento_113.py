def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Problema com tipo de dados inserido')
            continue
        except KeyboardInterrupt:
            print('\nUsuário não informou os dados')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Problema com tipo de dados inserido')
            continue
        except KeyboardInterrupt:
            print('\nUsuário não informou os dados')
            return 0
        else:
            return n


num1 = leiaInt('Qual número Int? ')
num2 = leiaFloat('Qual número Float? ')
print(f'Você digitou o número inteiro: {num1}')
print(f'Você digitou o número real: {num2}')
