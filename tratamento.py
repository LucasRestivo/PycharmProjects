try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Problema com tipo de dados inserido')
except ZeroDivisionError:
    print('Divisão impossível')
except KeyboardInterrupt:
    print('Usuário não informou os dados')
except Exception as erro:
    print(f'Erro encontrado: {erro.__cause__}')
else:
    print(f'Resultado: {r}')
finally:
    print('FIM')

