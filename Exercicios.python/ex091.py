'''
Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatorios. guarde esses resultados em um dicionario no Python.
No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero de dado 
'''

from random import randint
from time import sleep
from operator import itemgetter
jogo = dict({
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
})
ranking = list()
for k, v in jogo.items(): #O método .items() pega o dicionário e transforma em pares de chave-valor. No exemplo acima, ele se comporta como se fosse isso:
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('   == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}º Lugar: {v[0]} com {v[1]}')
    sleep(1)    