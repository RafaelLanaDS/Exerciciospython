''' Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
ex: digite um numero: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
'''

numero = int(input('Digite um numero: '))

uni = numero % 10
dez = (numero // 10) % 10
cen = (numero // 100) % 10
mil = (numero // 1000) % 10

print('Unidade: {}' .format(uni))
print('Dezena: {}' .format(dez))
print('Centena: {}'.format(cen))
print('Milhar: {}' .format(mil))