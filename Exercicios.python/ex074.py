'''
Crie um programa que vai gerar cinco numerós aleatorios e colocar em uma tupla depois disso mostre a lista de numeros  gerados 
e tambem indique o menor e o maior valor que esta na tupla.
'''

import random

numero_escolhido = (random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100))
print('Os cinco numeros escolhidos foram {}' .format(numero_escolhido))
print('O maior valor dos cinco numeros foi {}' .format(max(numero_escolhido)))
print('E o menor valor da lista foi {}' .format(min(numero_escolhido)))