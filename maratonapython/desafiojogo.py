'''
Desafio: Cadastro de Jogadores (com listas e dicionários)

Objetivo:
Você vai montar um programa que:

1. Pede o nome de 3 jogadores.


2. Para cada jogador, peça quantos gols ele fez em 2 partidas.


3. Guarde tudo isso num dicionário e coloque dentro de uma lista de jogadores.


4. No final, mostre:

O nome de cada jogador.

Os gols que ele fez em cada partida.

E o total de gols.
'''


principal = []
jogadores = []
gols = []
for c in range(1, 4):
    jogadores.append (str(input('Nome jogador {}: ' .format(c))))
    for c in range(1, 3):
        gols.append (int(input('gols na partida {}:' .format(c))))

print('jogadores {}' .format(jogadores))
print('gols {}' .format(gols))