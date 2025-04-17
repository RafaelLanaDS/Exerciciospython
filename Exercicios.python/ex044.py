'''  Elabore um programa que calcule o valor a ser pago por um produto, considerando seu (preço normal e condição de pagamento)
- a vista 10% de desconto
- a vista no cartão 5%
- em ate 2x no cartão preço normal
- 3x ou mais no cartão 20% de juros
'''
valor_produto = float(input('Digite o valor do produto: '))
print('''Escolha a forma de pagamento
[1] avista 10% de desconto
[2] avista no cartão 5% de desconto
[3] 2x no cartão preço normal
[4] 3x ou mais no cartão 20% de juros''')
pagamento = int(input('Digite a forma de pagamento: '))
if pagamento == 1:
    print('Valor avista foi {}' .format(valor_produto - (valor_produto * 0.10)))
elif pagamento == 2:
    print('Valor a ser pago no cartão é {}' .format(valor_produto - (valor_produto * 0.05)))
elif pagamento == 3:
    total = valor_produto
    parcelas = total / 2
    print('Valor normal a ser pago {} com 2x R${}' .format(total, parcelas))
elif pagamento == 4:
    total = valor_produto + (valor_produto * 0.20)
    totalpac = int(input('Digite a quantidade de parcelas: '))
    parcela = total / totalpac
    print('Sua compra parcelada ficara R${} com parcelas {} de {:.2f}' .format(total, totalpac, parcela))
else:
    print('Numero de compra nao reconhecido')
