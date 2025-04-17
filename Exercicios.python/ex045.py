''' CRIE um programa que faça o computador jogar jokenpo com voce  '''

from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('''Suas opçoes
[0] PEDRA 
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Escolha a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
print('-=' *12)
print('O computador jogou {}' .format(itens[computador]))
print('O jogador jogou {}' .format(itens[jogador]))
print('-=' * 12)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada invalida!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada invalida!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida!')