'''Faça um programa que jogue par ou impar com o computador. O jogo so sera intenrronpido quando
o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo
'''

from random import randint
V = 0
while True:
    jogador = int(input('Digite um numero: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ''
       