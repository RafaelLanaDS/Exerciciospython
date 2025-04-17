# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
# considere US$1.00 = 5.58

valor_em_real = float(input('Digite o valor que tem na carteira: '))
dolar = valor_em_real  / 5.58

print('voce possui {} reais, e convertendo em dolar voce tera US${:.1f} ' .format(valor_em_real, dolar))