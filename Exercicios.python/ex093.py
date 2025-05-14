'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol, o programa vai ler o nome do jogador e quantas partidadas
ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final isso será guardado em um dicionario o total de gols
feitos durante o campeonato.
'''
jogos = dict()

jogos['nome'] = str(input('Nome do jogador: '))
jogos['partidas'] = int(input(f'Quantas partidas {jogos['nome']} jogou: '))
for i in range(jogos['partidas']):
    gols = int(input(f'Quantidade de gols na {i+1}º partida: '))
    jogos['soma'] = jogos['partidas'] + gols
print(jogos)
print('-=' * 15)
for k, v in jogos.items():
    print(f' - {k} tem o valor {v}')
print('-=' * 15)
print(f'O jogador {jogos["nome"]} partidas')
print('-=' * 15)
print(f'O jogador {jogos["nome"]} jogou {jogos["partidas"]} partidas.')
for i, v in enumerate(jogos['gols']):
    print(f'   => Na partida {i}, fez {v} gols.')