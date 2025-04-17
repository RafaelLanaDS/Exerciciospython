# Escreva um programa que escreva a quantidade de km percorridos por um carro e a quantidade de dias pelos quais ele foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa por dia e 0.15 por km rodado.

carro_dia = 60
km_rodado = 0.15

dias = int(input('Quantos dias alugara o carro?: '))
km = float(input('Quantos km foram rodados?: '))

pago = dias * carro_dia + km * km_rodado

print('Voce rodou {}km, em {}dias.' .format(km, dias))
print('e o valor a ser pago sera de R${}' . format(pago))
