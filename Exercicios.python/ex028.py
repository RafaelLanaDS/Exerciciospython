''' Escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 a 5 e peça para o ususario
 tentar descobrir qual foi o numero escolhido pelo computador.
O programa devera escrever na tela se o usuario venceu ou perdeu
'''

import random

numero_escolhido = random.randint(0,5)

palpite = int(input('Palpite um numero de 0 a 5: '))

if palpite == numero_escolhido:
    print('Parabens voce acertou o numero escolhido.')
else:
    print('Voce nao acertou o numero tente de novo')
print('o numero que a maquina escolheu foi {}' . format(numero_escolhido))