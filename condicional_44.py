preco_normal = float(input('Qual preço? R$'))
print('''
FORMA DE PAGAMENTO
1) À vista no dinheiro ou cheque
2) À vista no cartão
3) 2x no cartão
4) 3x ou mais no cartão
''')
op_pgto = int(input('Qual opção?'))

if op_pgto == 1:
    preco_final = preco_normal*0.9
    print('Preço final: R${}'.format(preco_final))
elif op_pgto == 2:
    preco_final = preco_normal * 0.95
    print('Preço final: R${}'.format(preco_final))
elif op_pgto == 3:
    preco_final = preco_normal
    print('Preço final: R${} em 2x de R${} sem juros'.format(preco_final, preco_final/2))
elif op_pgto == 4:
    op_pgto_sec = int(input('Quantas parcelas?'))
    preco_final = preco_normal*1.2
    parcelas = preco_final/op_pgto_sec
    print('Preço final: R${} em {} parcelas de R${}'.format(preco_final, op_pgto_sec, parcelas))
else:
    print('Opção inválida')
