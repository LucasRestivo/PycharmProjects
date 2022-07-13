sexo = str(input('Qual o sexo? [M/F]')).strip().upper()[0] #upper()[0] caso digite "Masculino" pega só o M

while sexo not in 'MmFf': #MmFf poderia tirar o upper()
    sexo = str(input('Valor incorreto. Qual o sexo? '))
print('obrigado')