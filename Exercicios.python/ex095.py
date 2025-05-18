'''
Aprimore o desafio 93 para que ele funcione com varios jogadores incluindo um sistema de vizualização de detalhes do aproveitamento de cada jogador
'''

jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols fez na partida {c}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.itens():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} paridas. ')
for i, v in enumerate(jogador['gols']):
    print(f'     => Na partida {i}, fez {v} gols. ')
print(f'Foi um total de {jogador["total"]} gols. ')